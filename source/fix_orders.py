"""Comprehensive fix for orders.md.

1. Fix the small unfenced field references in the Note section.
2. Convert the "Valid Statuses" plain list to a bullet list.
3. Rewrite section 4 (POST /orders) — the source docx applied Heading 2 to
   every line in this section, breaking the structure. Replace lines 669..1017
   (the entire section 4 range) with a clean, properly-formatted version.
4. Wrap the PUT and DELETE HTTP request lines that aren't already fenced.
"""
import re

PATH = '/app/docs/orders.md'

with open(PATH) as f:
    src = f.read()

# ---------------------------------------------------------------------------
# Fix 1: Inline field references in the Note paragraph
# ---------------------------------------------------------------------------
src = src.replace(
    'When you are using the updated_at_min filter or updated_at_max filter, '
    'you should compare not with the shopping cart/marketplace date but with '
    'the parameters that we have added namely:\n'
    '"octopus_created_at":\n'
    '"octopus_updated_at":\n',
    'When you are using the updated_at_min filter or updated_at_max filter, '
    'you should compare not with the shopping cart/marketplace date but with '
    'the parameters that we have added namely `octopus_created_at` and '
    '`octopus_updated_at`.\n',
)

# ---------------------------------------------------------------------------
# Fix 2: Valid Statuses list -> bullet list
# ---------------------------------------------------------------------------
old_statuses = (
    'Below are all the Valid Statuses that Octopus API uses after Translating from various Shopping carts:\n'
    'Authorized\n'
    'Authorization\n'
    'PAID\n'
    'Refunded\n'
    'Refund\n'
    'Partially_Refunded\n'
    'Capture\n'
    'Sale\n'
    'Void\n'
    'Voided\n'
)
new_statuses = (
    'Below are all the Valid Statuses that Octopus API uses after Translating from various Shopping carts:\n\n'
    '- Authorized\n'
    '- Authorization\n'
    '- PAID\n'
    '- Refunded\n'
    '- Refund\n'
    '- Partially_Refunded\n'
    '- Capture\n'
    '- Sale\n'
    '- Void\n'
    '- Voided\n'
)
src = src.replace(old_statuses, new_statuses)

# ---------------------------------------------------------------------------
# Fix 3: Rewrite the corrupted section 4 (POST /orders)
#        Detect the range by stable boundary markers and replace.
# ---------------------------------------------------------------------------
SECTION_4_NEW = """## 4. POST /orders - Create Order

### 4.1 Endpoint Definition

```http
POST   /orders   Create a new order in the connected shop
```

| Property | Value |
| --- | --- |
| HTTP Method | POST |
| URL | https://octopusapi.24sevencommerce.com/admin/api/2020-01/orders.json |
| Content-Type | application/json |
| Auth Required | Yes - X-API-Key / X-API-Secret or Bearer token |
| Required OAuth Scope | write_orders |
| Success Response | 201 Created |
| Idempotent | No - each call creates a new order |

### 4.2 Request Fields

#### Top-Level Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| email | string | Yes | Customer email address. Must be a valid email format. |
| phone | string | No | Customer phone in E.164 format (e.g., +14155550123). |
| line_items | array | Yes | Array of one or more line item objects. See Line Item Fields below. |
| shipping_address | object | No | Shipping destination. Required if any line item requires_shipping. |
| billing_address | object | No | Billing address. Defaults to shipping_address if omitted. |
| customer | object | No | Associate with an existing customer: `{"id": "cust_jane01"}`. |
| financial_status | string | No | pending, authorized, paid. Default: pending. |
| currency | string | No | ISO 4217 currency code. Defaults to shop default currency. |
| shipping_lines | array | No | Shipping method(s) to apply. |
| discount_codes | array | No | Discount codes to apply. Code must exist in the shop. |
| note | string | No | Order note or special instructions (max 5,000 chars). |
| tags | string | No | Comma-separated order tags (max 255 chars total). |
| source_name | string | No | Order source: api, web, pos, mobile. Default: api. |
| send_receipt | boolean | No | Send order confirmation email to customer. Default: false. |
| send_fulfillment_receipt | boolean | No | Send fulfillment emails when items are shipped. Default: false. |

#### Line Item Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| variant_id | string | Yes | ID of the product variant to add. Must exist in the shop. |
| quantity | integer | Yes | Number of units to order. Must be a positive integer. |
| price | string | No | Override price per unit as decimal string. Defaults to variant price. |
| title | string | No | Override line item title. Defaults to product + variant title. |
| requires_shipping | boolean | No | Override shipping requirement. Defaults to variant setting. |
| taxable | boolean | No | Override taxable status. Defaults to variant setting. |
| discount_allocations | array | No | Array of {amount, discount_application_index} objects for line-level discounts. |

#### Address Object Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| first_name | string | Yes | Recipient first name. |
| last_name | string | Yes | Recipient last name. |
| address1 | string | Yes | Street address, first line. |
| address2 | string | No | Apartment, suite, unit number, etc. |
| city | string | Yes | City name. |
| province | string | No | Full state or province name. |
| province_code | string | No | State/province abbreviation (e.g., CA, NY, ON). |
| zip | string | Yes | Postal or ZIP code. |
| country | string | No | Full country name. |
| country_code | string | Yes | ISO 3166-1 alpha-2 country code (e.g., US, GB, CA). |
| phone | string | No | Phone number for this address in E.164 format. |
| company | string | No | Company name for B2B orders. |

#### Shipping Line Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| title | string | Yes | Display name for the shipping method (e.g., Standard Shipping). |
| price | string | Yes | Shipping cost as decimal string (e.g., "8.95"). Use "0.00" for free shipping. |
| code | string | No | Internal shipping method code. |
| carrier_identifier | string | No | Carrier identifier: fedex, ups, usps, dhl. |

### 4.3 Sample Requests & Responses

#### Example A - Standard Order with Customer Reference

**Request:**

```http
POST /orders HTTP/1.1
Host: octopusapi.24sevencommerce.com
X-API-Key: your_api_key
X-API-Secret: your_api_secret
Content-Type: application/json
```

**Request Body:**

```json
{
  "email": "jane.doe@example.com",
  "phone": "+14155550123",
  "customer": { "id": "cust_jane01" },
  "financial_status": "pending",
  "source_name": "api",
  "send_receipt": true,
  "note": "Please use eco-friendly packaging",
  "tags": "eco, api-order",
  "line_items": [
    {
      "variant_id": "var_002",
      "quantity": 2
    },
    {
      "variant_id": "var_010",
      "quantity": 1,
      "price": "99.00"
    }
  ],
  "shipping_address": {
    "first_name": "Jane",
    "last_name": "Doe",
    "address1": "456 Elm Street",
    "city": "San Francisco",
    "province": "California",
    "province_code": "CA",
    "zip": "94102",
    "country_code": "US",
    "phone": "+14155550123"
  },
  "shipping_lines": [
    {
      "title": "Standard Shipping",
      "price": "8.95",
      "code": "STANDARD",
      "carrier_identifier": "ups"
    }
  ],
  "discount_codes": [
    { "code": "SAVE10" }
  ]
}
```

**Response (201 Created):**

```json
{
  "order": {
    "id": "ord_1010",
    "order_number": 1010,
    "email": "jane.doe@example.com",
    "phone": "+14155550123",
    "status": "open",
    "financial_status": "pending",
    "fulfillment_status": "unfulfilled",
    "currency": "USD",
    "subtotal_price": "158.98",
    "total_discounts": "10.00",
    "total_tax": "13.32",
    "total_shipping": "8.95",
    "total_price": "171.25",
    "source_name": "api",
    "note": "Please use eco-friendly packaging",
    "tags": "eco, api-order",
    "customer": {
      "id": "cust_jane01",
      "email": "jane.doe@example.com"
    },
    "line_items": [
      {
        "id": "li_020",
        "variant_id": "var_002",
        "quantity": 2,
        "price": "29.99",
        "total": "59.98",
        "requires_shipping": true,
        "taxable": true
      },
      {
        "id": "li_021",
        "variant_id": "var_010",
        "quantity": 1,
        "price": "99.00",
        "total": "99.00",
        "requires_shipping": true,
        "taxable": true
      }
    ],
    "shipping_address": {
      "first_name": "Jane", "last_name": "Doe",
      "address1": "456 Elm Street",
      "city": "San Francisco", "province": "California",
      "zip": "94102", "country_code": "US"
    },
    "shipping_lines": [
      { "id": "shp_021", "title": "Standard Shipping", "price": "8.95", "code": "STANDARD" }
    ],
    "discount_codes": [
      { "code": "SAVE10", "amount": "10.00", "type": "fixed_amount" }
    ],
    "fulfillments": [],
    "refunds": [],
    "created_at": "2024-07-15T11:00:00Z",
    "updated_at": "2024-07-15T11:00:00Z",
    "closed_at": null,
    "cancelled_at": null
  }
}
```

#### Example B - Paid B2B Order with Billing Address

**Request Body:**

```json
{
  "email": "procurement@widgetcorp.com",
  "financial_status": "paid",
  "source_name": "api",
  "tags": "b2b, wholesale",
  "line_items": [
    { "variant_id": "var_003", "quantity": 50, "price": "22.50" }
  ],
  "shipping_address": {
    "first_name": "Alice",
    "last_name": "Nguyen",
    "company": "Widget Corp",
    "address1": "100 Industrial Park Blvd",
    "city": "Austin",
    "province_code": "TX",
    "zip": "78701",
    "country_code": "US"
  },
  "billing_address": {
    "first_name": "Alice",
    "last_name": "Nguyen",
    "company": "Widget Corp",
    "address1": "200 Finance Ave, Suite 400",
    "city": "Austin",
    "province_code": "TX",
    "zip": "78702",
    "country_code": "US"
  },
  "shipping_lines": [
    { "title": "Free Freight", "price": "0.00" }
  ]
}
```

**Response (201 Created):**

```json
{
  "order": {
    "id": "ord_1011",
    "order_number": 1011,
    "email": "procurement@widgetcorp.com",
    "status": "open",
    "financial_status": "paid",
    "fulfillment_status": "unfulfilled",
    "currency": "USD",
    "subtotal_price": "1125.00",
    "total_discounts": "0.00",
    "total_tax": "92.81",
    "total_shipping": "0.00",
    "total_price": "1217.81",
    "tags": "b2b, wholesale",
    "line_items": [
      {
        "id": "li_030",
        "variant_id": "var_003",
        "quantity": 50,
        "price": "22.50",
        "total": "1125.00"
      }
    ],
    "created_at": "2024-07-15T14:00:00Z",
    "updated_at": "2024-07-15T14:00:00Z"
  }
}
```

#### Example C - Validation Error Response

**Request Body (missing required fields):**

```json
{
  "note": "This order has no line items or email"
}
```

**Response (422 Unprocessable Entity):**

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Request validation failed.",
    "status": 422,
    "errors": [
      { "field": "email", "message": "Email is required." },
      { "field": "line_items", "message": "At least one line item is required." }
    ]
  }
}
```

### 4.4 Validation Rules

- `email` is required and must be a valid email format.
- `line_items` is required and must contain at least one item.
- Each line item must have a valid `variant_id` that exists in the shop.
- `quantity` must be a positive integer (minimum: 1).
- `price` overrides, if provided, must be positive decimal strings.
- If any line item has `requires_shipping: true`, `shipping_address` is required.
- `country_code` in address objects must be a valid ISO 3166-1 alpha-2 code.
- `currency`, if provided, must be a valid ISO 4217 code.
- `discount_codes` entries must reference codes that exist and are active in the shop.
- `financial_status` must be one of: `pending`, `authorized`, `paid`.
- `source_name` must be one of: `api`, `web`, `pos`, `mobile`.

### 4.5 Business Logic & Side Effects

- Inventory is decremented for each line item at the shop's default location when the order is created with `financial_status: paid`. For pending/authorized orders, inventory is reserved but not decremented.
- If `send_receipt` is true, a confirmation email is dispatched to the provided email address.
- If a `customer.id` is provided, the order is associated with that customer record and their `orders_count` and `total_spent` are updated.
- `discount_codes` are validated at creation time. An invalid or expired code returns a 422 error.
- Tax is calculated automatically based on shop tax settings and the `shipping_address` jurisdiction.
- The order is created with `status: open` and `fulfillment_status: unfulfilled`.
- A webhook event `orders/create` is dispatched to all registered webhook subscribers.

"""

# Find the start of section 4 and the start of section 5 (PUT)
m_start = re.search(r'^## 4\. POST /orders - Create Order\s*$', src, re.MULTILINE)
m_end = re.search(r'^## PUT /orders/\{order_id\} - Update Order\s*$', src, re.MULTILINE)
assert m_start and m_end, "Section boundaries not found"

before = src[:m_start.start()]
after = src[m_end.start():]
src = before + SECTION_4_NEW + after

# ---------------------------------------------------------------------------
# Fix 4: Make section 5/6 top headings consistent (currently `## PUT`, `## 6. DELETE`)
# Demote sub-section ## 5.1 etc to ### where they are sub-sections, plus demote
# the `## 5.x Validation Rules` / `## 5.x Business Logic` etc.
# We will only touch a few known-bad heading levels.
# ---------------------------------------------------------------------------
heading_demote = [
    ('## PUT /orders/{order_id} - Update Order', '## 5. PUT /orders/{order_id} - Update Order'),
    ('## 5.1 Endpoint Definition', '### 5.1 Endpoint Definition'),
    ('## 5.2 Updatable Fields', '### 5.2 Updatable Fields'),
    ('## 5.3 Sample Requests & Responses', '### 5.3 Sample Requests & Responses'),
    ('## 5.4 Validation Rules', '### 5.4 Validation Rules'),
    ('## 5.5 Business Logic & Side Effects', '### 5.5 Business Logic & Side Effects'),
    ('## 6. DELETE /orders/{order_id} - Delete Order', '## 6. DELETE /orders/{order_id} - Delete Order'),
    ('## 6.1 Endpoint Definition', '### 6.1 Endpoint Definition'),
    ('## 6.2 Sample Requests & Responses', '### 6.2 Sample Requests & Responses'),
    ('## 6.3 Deletion Rules & Constraints', '### 6.3 Deletion Rules & Constraints'),
    ('## 6.4 Business Logic & Side Effects', '### 6.4 Business Logic & Side Effects'),
    ('## 7. Error Reference for Order Endpoints', '## 7. Error Reference for Order Endpoints'),
    ('## 7.1 Order-Specific Error Codes', '### 7.1 Order-Specific Error Codes'),
]
for old, new in heading_demote:
    src = src.replace(old, new)

# Convert bullet-prose in 5.4/5.5/6.4 sections from line-per-statement to actual bullets
# These appear as consecutive sentences without bullets. Detect by surrounding heading.
def bulletify_block(text, heading_marker, next_heading_marker):
    """Find the block between two headings and turn each non-empty line into '- ...'."""
    i = text.find(heading_marker)
    j = text.find(next_heading_marker, i + 1) if i != -1 else -1
    if i == -1 or j == -1:
        return text
    block_start = text.find('\n', i) + 1
    block = text[block_start:j].strip('\n')
    # First line is usually intro prose — keep as-is if it doesn't look like a bullet candidate
    lines = block.split('\n')
    new_lines = []
    for ln in lines:
        s = ln.strip()
        if not s:
            new_lines.append('')
        elif s.startswith(('- ', '* ', '| ')) or s.startswith(('WARNING:', 'CAUTION:')):
            new_lines.append(ln)
        elif s.startswith('The ') or s.startswith('An order') or s.endswith(':'):
            # likely intro prose
            new_lines.append(ln)
        else:
            new_lines.append('- ' + s)
    return text[:block_start] + '\n'.join(new_lines) + '\n\n' + text[j:]

src = bulletify_block(src, '### 5.4 Validation Rules', '### 5.5 Business Logic')
src = bulletify_block(src, '### 5.5 Business Logic & Side Effects', '## 6. DELETE')
src = bulletify_block(src, '### 6.4 Business Logic & Side Effects', '## 7. Error')

# Collapse excessive blank lines
src = re.sub(r'\n{3,}', '\n\n', src)

with open(PATH, 'w') as f:
    f.write(src)

print('Done.')
print('File now has', len(src.split('\n')), 'lines.')
