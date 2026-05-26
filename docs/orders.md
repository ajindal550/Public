# Orders

## 10.1 Overview

The Orders resource provides full CRUD support for managing orders in the connected shop. The GET endpoints allow partners to retrieve order lists and individual order details. POST, PUT, and DELETE enable programmatic order creation, editing, and removal.

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | /orders | List all orders with filters |
| GET | /orders/{order_id} | Retrieve a single order by ID |
| POST | /orders | Create a new order |
| PUT | /orders/{order_id} | Update an existing order |
| DELETE | /orders/{order_id} | Delete an order (restricted) |

## 10.2 GET /orders

## An order is a customer's completed request to purchase one or more products from a shop. An order is created when a customer completes the checkout process, during which time they provide an email address or phone number, billing address and payment information.

GET   /orders  List all orders with optional filters

This endpoint implements pagination by using links that are provided in the response header. Sending the page parameter will return an error.

### Query Parameters

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| ids | Retrieve only orders specified by a comma-separated list of order IDs. | ids | Retrieve only orders specified by a comma-separated list of order IDs. |
| limit | The maximum number of results to show on a page. (default: 50, maximum: 250) | limit | The maximum number of results to show on a page. (default: 50, maximum: 250) |
| created_at_min | Show orders created at or after date (format: 2014-04-25T16:15:47) | created_at_min | Show orders created at or after date (format: 2014-04-25T16:15:47) |
| created_at_max | Show orders created at or before date (format: 2014-04-25T16:15:47) | created_at_max | Show orders created at or before date (format: 2014-04-25T16:15:47) |
| updated_at_min | Show orders last updated at or after date (format: 2014-04-25T16:15:47) | updated_at_min | Show orders last updated at or after date (format: 2014-04-25T16:15:47) |
| updated_at_max | Show orders last updated at or before date (format: 2014-04-25T16:15:47) | updated_at_max | Show orders last updated at or before date (format: 2014-04-25T16:15:47) |
| since_id | Show orders on or after the specified ID | since_id | Show orders on or after the specified ID |
| location_id | Get orders of a specific fulfillment location | location_id | Get orders of a specific fulfillment location |
| financial_status | Get orders of a specific finacial_status e.g. paid, refunded, pending etc. | financial_status | Get orders of a specific finacial_status e.g. paid, refunded, pending etc. |

Sample Request:

```http
GET /admin/api/2020-01/orders.json
```

Sample Response (200 OK):

```json
{
"id": 8,
"source": "BIGCOMMERCE",
"email": "tauret@test.com",
"closed_at": null,
"created_at": "2023-01-04T16:00:02-00:00",
"updated_at": "2023-01-04T16:11:20-00:00",
"number": 105,
"note": "",
"token": "ee91b9f9-d6ce-4afe-8a18-a7a9cb76feb4",
"gateway": "manual",
"test": false,
"total_price": "5997.0000",
"subtotal_price": "5997.0000",
"total_weight": 0.0,
"total_tax": "0.0000",
"taxes_included": false,
"currency": "INR",
"financial_status": "paid",
"confirmed": true,
"total_discounts": "0.0000",
"total_line_items_price": "5997.0000",
"cart_token": "ee91b9f9-d6ce-4afe-8a18-a7a9cb76feb4",
"buyer_accepts_marketing": false,
"name": "#105",
"referring_site": null,
"landing_site": null,
"cancelled_at": null,
"cancel_reason": null,
"total_price_usd": "5997.0000",
"checkout_token": null,
"reference": "Demo1",
"user_id": 1,
"location_id": "",
"source_identifier": null,
"source_url": "https://api.bigcommerce.com/stores/3htoz893mb/v2/orders",
"processed_at": null,
"device_id": "0",
"phone": "",
"customer_locale": "en",
"app_id": 0,
"browser_ip": "157.35.82.16",
"landing_site_ref": null,
"order_number": 105,
"discount_applications": [],
"discount_codes": [],
"note_attributes": [],
"payment_gateway_names": [
"manual"
],
"processing_method": "",
"checkout_id": 0,
"source_name": "manual",
"fulfillment_status": null,
"tax_lines": [],
"tags": "",
"contact_email": "tauret@test.com",
"order_status_url": "https://api.bigcommerce.com/stores/3htoz893mb/v2/orders",
"presentment_currency": "INR",
"total_line_items_price_set": {
"shop_money": {
"amount": "5997.0000",
"currency_code": "INR"
},
"presentment_money": {
"amount": "5997.0000",
"currency_code": "INR"
}
},
"total_discounts_set": {
"shop_money": {
"amount": "0.0000",
"currency_code": "INR"
},
"presentment_money": {
"amount": "0.0000",
"currency_code": "INR"
}
},
"total_shipping_price_set": {
"shop_money": {
"amount": "0.0000",
"currency_code": "INR"
},
"presentment_money": {
"amount": "0.0000",
"currency_code": "INR"
}
},
"subtotal_price_set": {
"shop_money": {
"amount": "5997.0000",
"currency_code": "INR"
},
"presentment_money": {
"amount": "5997.0000",
"currency_code": "INR"
}
},
"total_price_set": {
"shop_money": {
"amount": "5997.0000",
"currency_code": "INR"
},
"presentment_money": {
"amount": "5997.0000",
"currency_code": "INR"
}
},
"total_tax_set": {
"shop_money": {
"amount": "0.0000",
"currency_code": "INR"
},
"presentment_money": {
"amount": "0.0000",
"currency_code": "INR"
}
},
"line_items": [{
"id": 9,
"variant_id": 79,
"title": "Samshield Custom Miss Shield Black Matt Trim & Blazon 6 7/8M 5 Frontal Swarovski Jet Black Top & Frontal Band Crystal Fine Medley",
"quantity": 3,
"sku": "210000013357",
"variant_title": "Samshield Custom Miss Shield Black Matt Trim & Blazon 6 7/8M 5 Frontal Swarovski Jet Black Top & Frontal Band Crystal Fine Medley",
"vendor": "Samshield Custom Miss Shield Black Matt Trim & Blazon 6 7/8M 5 Frontal Swarovski Jet Black Top & Frontal Band Crystal Fine Medley",
"fulfillment_service": null,
"product_id": 113,
"requires_shipping": false,
"taxable": false,
"gift_card": false,
"name": "Samshield Custom Miss Shield Black Matt Trim & Blazon 6 7/8M 5 Frontal Swarovski Jet Black Top & Frontal Band Crystal Fine Medley",
"variant_inventory_management": "bigcommerce",
"properties": [],
"product_exists": true,
"fulfillable_quantity": 3,
"grams": 50,
"price": "1999.0000",
"total_discount": "0.000",
"fulfillment_status": "fulfilled",
"price_set": {
"shop_money": {
"amount": "5997.0000",
"currency_code": "INR"
},
"presentment_money": {
"amount": "5997.0000",
"currency_code": "INR"
}
},
"total_discount_set": {
"shop_money": {
"amount": "0.0000",
"currency_code": "INR"
},
"presentment_money": {
"amount": "0.0000",
"currency_code": "INR"
}
},
"discount_allocations": [],
"admin_graphql_api_id": null,
"tax_lines": [],
"origin_location": null
}],
"fulfillments": [{
"id": 7,
"Is_octopus_fulfillment": false,
"order_id": 8,
"status": "success",
"created_at": "2023-01-04T16:00:02-00:00",
"service": "BigCommerce",
"updated_at": "2023-01-04T16:11:20-00:00",
"tracking_company": "",
"shipment_status": "success",
"location_id": 0,
"line_items": [{
"id": 9,
"variant_id": 79,
"title": "Samshield Custom Miss Shield Black Matt Trim & Blazon 6 7/8M 5 Frontal Swarovski Jet Black Top & Frontal Band Crystal Fine Medley",
"quantity": 3,
"sku": "210000013357",
"variant_title": "Samshield Custom Miss Shield Black Matt Trim & Blazon 6 7/8M 5 Frontal Swarovski Jet Black Top & Frontal Band Crystal Fine Medley",
"vendor": "Samshield Custom Miss Shield Black Matt Trim & Blazon 6 7/8M 5 Frontal Swarovski Jet Black Top & Frontal Band Crystal Fine Medley",
"fulfillment_service": null,
"product_id": 113,
"requires_shipping": false,
"taxable": false,
"gift_card": false,
"name": "Samshield Custom Miss Shield Black Matt Trim & Blazon 6 7/8M 5 Frontal Swarovski Jet Black Top & Frontal Band Crystal Fine Medley",
"variant_inventory_management": "bigcommerce",
"properties": [],
"product_exists": true,
"fulfillable_quantity": 3,
"grams": 50,
"price": "1999.0000",
"total_discount": "0.000",
"fulfillment_status": "fulfilled",
"price_set": {
"shop_money": {
"amount": "5997.0000",
"currency_code": "INR"
},
"presentment_money": {
"amount": "5997.0000",
"currency_code": "INR"
}
},
"total_discount_set": {
"shop_money": {
"amount": "0.0000",
"currency_code": "INR"
},
"presentment_money": {
"amount": "0.0000",
"currency_code": "INR"
}
},
"discount_allocations": [],
"admin_graphql_api_id": null,
"tax_lines": [],
"origin_location": null
}],
"tracking_number": "",
"tracking_numbers": [
""
],
"tracking_url": "",
"tracking_urls": [
""
],
"receipt": "",
"name": "",
"admin_graphql_api_id": "",
"octopus_delivery_method": null
}],
"refunds": [{
"id": 8,
"admin_graphql_api_id": "",
"created_at": "2023-01-04T16:00:02-00:00",
"note": "",
"order_id": 8,
"processed_at": null,
"restock": true,
"total_duties_set": {
"shop_money": {
"amount": "0.00",
"currency_code": "INR"
},
"presentment_money": {
"amount": "0.00",
"currency_code": "INR"
}
},
"user_id": 0,
"order_adjustments": [{
"id": 8,
"amount": "5997.0000",
"amount_set": {
"shop_money": {
"amount": "5997.0000",
"currency_code": "INR"
},
"presentment_money": {
"amount": "5997.0000",
"currency_code": "INR"
}
},
"kind": "",
"order_id": 8,
"reason": "",
"refund_id": 8,
"tax_amount": "0.00",
"tax_amount_set": {
"shop_money": {
"amount": "0.00",
"currency_code": "INR"
},
"presentment_money": {
"amount": "0.00",
"currency_code": "INR"
}
}
},
{
"id": 8,
"amount": "-5997.0000",
"amount_set": {
"shop_money": {
"amount": "-5997.0000",
"currency_code": "INR"
},
"presentment_money": {
"amount": "-5997.0000",
"currency_code": "INR"
}
},
"kind": "",
"order_id": 8,
"reason": "",
"refund_id": 8,
"tax_amount": "0.00",
"tax_amount_set": {
"shop_money": {
"amount": "0.00",
"currency_code": "INR"
},
"presentment_money": {
"amount": "0.00",
"currency_code": "INR"
}
}
}
],
"transactions": [{
"id": 105,
"order_id": 8,
"kind": "",
"gateway": "manual",
"status": "Refunded",
"message": "",
"created_at": "2023-01-04T16:00:02-00:00",
"test": false,
"authorization": "",
"location_id": null,
"user_id": null,
"parent_id": null,
"processed_at": null,
"device_id": 1,
"receipt": "5997.0000",
"error_code": null,
"source_name": "manual",
"amount": "5997.0000",
"currency": "INR",
"admin_graphql_api_id": "",
"payment_details": null
}],
"refund_line_items": [
{

"id": 357262622829,

"line_item_id": 11886729068653,

"location_id": 36187996269,

"quantity": 3,

"restock_type": "return",

"subtotal": 5997.0,

"subtotal_set": {

"shop_money": {

"amount": "5997.00",

"currency_code": "CAD"

},

"presentment_money": {

"amount": "5997.00",

"currency_code": "CAD"

}

},

"total_tax": 0.0,

"total_tax_set": {

"shop_money": {

"amount": "0.00",

"currency_code": "CAD"

},

"presentment_money": {

"amount": "0.00",

"currency_code": "CAD"

}

},
],
"duties": []
}],
"total_tip_received": "0",
"admin_graphql_api_id": null,
"shipping_lines": [{
"id": 6,
"title": "None",
"price": "0.0000",
"code": "None",
"source": "bigcommerce",
"phone": "",
"requested_fulfillment_service_id": "None",
"delivery_category": "",
"carrier_identifier": "",
"discounted_price": "0.0000",
"price_set": {
"shop_money": {
"amount": "0.0000",
"currency_code": "INR"
},
"presentment_money": {
"amount": "0.0000",
"currency_code": "INR"
}
},
"discounted_price_set": {
"shop_money": {
"amount": "0.0000",
"currency_code": "INR"
},
"presentment_money": {
"amount": "0.0000",
"currency_code": "INR"
}
},
"discount_allocations": [],
"tax_lines": []
}],
"billing_address": {
"first_name": "Tauret",
"address1": "Address 1",
"phone": "",
"city": "Noida",
"zip": "201306",
"province": "Uttar Pradesh",
"country": "India",
"last_name": "Akhtar",
"address2": "",
"company": "",
"latitude": 46.266042,
"longitude": -79.436514,
"name": "Tauret Akhtar",
"country_code": "IN",
"province_code": null
},
"shipping_address": {
"first_name": "Tauret",
"address1": "Address 1",
"phone": "",
"city": "Noida",
"zip": "201306",
"province": "Uttar Pradesh",
"country": "India",
"last_name": "Akhtar",
"address2": "",
"company": "",
"latitude": 46.266042,
"longitude": -79.436514,
"name": "Tauret Akhtar",
"country_code": "IN",
"province_code": null
},
"client_details": {
"browser_ip": "157.35.82.16",
"accept_language": "",
"user_agent": "",
"session_hash": "",
"browser_width": 0,
"browser_height": 0
},
"customer": {
"id": 2,
"email": "tauret@test.com",
"accepts_marketing": "False",
"created_at": "2022-11-30T11:16:33-00:00",
"updated_at": "2022-11-30T11:16:33-00:00",
"first_name": "Tauret",
"last_name": "Akhtar",
"orders_count": 6,
"state": "enabled",
"total_spent": "13102.9",
"last_order_id": 105,
"note": "",
"verified_email": true,
"multipass_identifier": null,
"tax_exempt": false,
"phone": "",
"tags": null,
"last_order_name": "105",
"currency": "INR",
"accepts_marketing_updated_at": null,
"marketing_opt_in_level": null,
"default_address": {
"id": 3,
"customer_id": 2,
"first_name": "Tauret",
"last_name": "Akhtar",
"company": "",
"address1": "Address 1",
"address2": "",
"city": "Noida",
"province": "Uttar Pradesh",
"country": "India",
"zip": "201306",
"phone": "",
"name": "Tauret Akhtar",
"province_code": null,
"country_code": "IN",
"country_name": "India",
"default": true
}
},
"octopus_created_at": "2023-01-04T16:01:10-00:00",
"octopus_updated_at": "2023-01-04T16:13:07-00:00"
}
```

Note:
Rate: Depending on a given point of sale system, we send tax rate as it is received in the order. In some POS, the order does not download to POS due to mismatch such as Lightspeed. You can handle it as you see fit.

Location_ID: In case of some shopping carts/marketplaces like Woocommerce and Amazon, we do not receive any location_id in the fulfillments node. The location_id can not be left blank as it is mandatory. Therefore, in this instance we pass "location_id": 0.
If you want to GET orders after a specific date, you can use the updated_at_min or updated_at_max filter. When you are using the updated_at_min filter or updated_at_max filter, you should compare not with the shopping cart/marketplace date but with the parameters that we have added namely:
"octopus_created_at":
"octopus_updated_at":

While using the created_at_min and created_at_max filter, you will get the result based on octopus_created_at and octopus_updated_at only.
You need to pass your system date. The dates shown on the orders will be of the Shopping cart/marketplace but the orders will be filtered on the basis of dates in octopus_created_at and octopus_updated_at fields.

In the case of Amazon, Walmart and eBay,in the case of Amazon, Walmart, and eBay, the tax is paid by them on behalf of the customer. Hence, the order total does not contain the tax. Therefore, the subtotal_price and total_price have the same values.
Although the tax is given separately, you need to ignore the tax in the case of these three.You will have to ignore the "total_tax" field only in case of orders coming from Amazon, Walmart and eBay.
In the order JSON, there is a field called "Source" which tells you the order source.
No need to do anything for other platforms such as Shopify, Bigcommerce or LocalExpress.
So, if you get Amazon, Walmart or eBay in the "Source", you know that you have to ignore the tax_total.

Below are all the Valid Statuses that Octopus API uses after Translating from various Shopping carts:
Authorized
Authorization
PAID
Refunded
Refund
Partially_Refunded
Capture
Sale
Void
Voided

Retrieves all orders after a specific ID

Request:

GET /admin/api/2020-01/orders.json?since_id=2

Response:

This end point will return a list of orders generated after since id. The model of sales order is represented in the above request.

Response

HTTP/1.1 200 OK

Retrieves an order count

Request:

Get /admin/api/2020-01/orders/count.json

Response:

Copy
HTTP/1.1 200 OK
{
"count": 620
}

## Order Object Schema

## The following table defines every field in the Order object. Fields marked as System-set are automatically managed by the server and must not be included in POST or PUT request bodies.

| Field | Type | Writable | Description |
| --- | --- | --- | --- |
| id | string | System-set | Unique order identifier. Auto-generated on creation. |
| order_number | integer | System-set | Sequential human-readable order number. |
| email | string | POST, PUT | Customer email address. |
| phone | string | POST, PUT | Customer phone number in E.164 format. |
| status | string | System-set | open, closed, cancelled. Managed via dedicated endpoints. |
| financial_status | string | POST | pending, authorized, paid. Defaults to pending. |
| fulfillment_status | string | System-set | fulfilled, unfulfilled, partial, restocked. |
| currency | string | POST | ISO 4217 code. Defaults to shop currency if omitted. |
| subtotal_price | string | System-set | Sum of line item prices before tax, shipping, discounts. |
| total_discounts | string | System-set | Total of all applied discounts. |
| total_tax | string | System-set | Total tax charged on the order. |
| total_shipping | string | System-set | Total shipping charges. |
| total_price | string | System-set | Grand total: subtotal + tax + shipping - discounts. |
| line_items | array | POST | Array of line item objects. Required on create. |
| shipping_address | object | POST, PUT | Destination address for physical shipment. |
| billing_address | object | POST, PUT | Billing address for the order. |
| customer | object | POST | Customer reference object (id) or inline customer fields. |
| shipping_lines | array | POST | Array of shipping line objects defining shipping method. |
| discount_codes | array | POST | Array of discount code objects to apply. |
| note | string | POST, PUT | Internal order note or special instructions. |
| tags | string | POST, PUT | Comma-separated list of order tags. |
| source_name | string | POST | Order source: web, pos, mobile, api. Default: api. |
| send_receipt | boolean | POST | Send order confirmation email to customer. Default: false. |
| send_fulfillment_receipt | boolean | POST | Send fulfillment notification email. Default: false. |
| fulfillments | array | System-set | Fulfillment records. Managed via Fulfillment API. |
| refunds | array | System-set | Refund records. Managed via Transaction API. |
| created_at | datetime | System-set | Timestamp when the order was created (ISO 8601). |
| updated_at | datetime | System-set | Timestamp of last modification (ISO 8601). |
| closed_at | datetime | System-set | Timestamp when the order was closed. Null if open. |
| cancelled_at | datetime | System-set | Timestamp when the order was cancelled. Null if not. |
| cancel_reason | string | System-set | Cancellation reason: customer, inventory, fraud, other. |

## 4. POST /orders - Create Order

## 4.1 Endpoint Definition

## POST   /orders   Create a new order in the connected shop

| Property | Value |
| --- | --- |
| HTTP Method | POST |
| URL | https://octopusapi.24sevencommerce.com/admin/api/2020-01/orders.json |
| Content-Type | application/json |
| Auth Required | Yes - X-API-Key / X-API-Secret or Bearer token |
| Required OAuth Scope | write_orders |
| Success Response | 201 Created |
| Idempotent | No - each call creates a new order |

## 4.2 Request Fields

## Top-Level Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| email | string | Yes | Customer email address. Must be a valid email format. |
| phone | string | No | Customer phone in E.164 format (e.g., +14155550123). |
| line_items | array | Yes | Array of one or more line item objects. See Line Item Fields below. |
| shipping_address | object | No | Shipping destination. Required if any line item requires_shipping. |
| billing_address | object | No | Billing address. Defaults to shipping_address if omitted. |
| customer | object | No | Associate with an existing customer: {"id": "cust_jane01"}. |
| financial_status | string | No | pending, authorized, paid. Default: pending. |
| currency | string | No | ISO 4217 currency code. Defaults to shop default currency. |
| shipping_lines | array | No | Shipping method(s) to apply. |
| discount_codes | array | No | Discount codes to apply. Code must exist in the shop. |
| note | string | No | Order note or special instructions (max 5,000 chars). |
| tags | string | No | Comma-separated order tags (max 255 chars total). |
| source_name | string | No | Order source: api, web, pos, mobile. Default: api. |
| send_receipt | boolean | No | Send order confirmation email to customer. Default: false. |
| send_fulfillment_receipt | boolean | No | Send fulfillment emails when items are shipped. Default: false. |

## Line Item Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| variant_id | string | Yes | ID of the product variant to add. Must exist in the shop. |
| quantity | integer | Yes | Number of units to order. Must be a positive integer. |
| price | string | No | Override price per unit as decimal string. Defaults to variant price. |
| title | string | No | Override line item title. Defaults to product + variant title. |
| requires_shipping | boolean | No | Override shipping requirement. Defaults to variant setting. |
| taxable | boolean | No | Override taxable status. Defaults to variant setting. |
| discount_allocations | array | No | Array of {amount, discount_application_index} objects for line-level discounts. |

## Address Object Fields

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

## Shipping Line Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| title | string | Yes | Display name for the shipping method (e.g., Standard Shipping). |
| price | string | Yes | Shipping cost as decimal string (e.g., "8.95"). Use "0.00" for free shipping. |
| code | string | No | Internal shipping method code. |
| carrier_identifier | string | No | Carrier identifier: fedex, ups, usps, dhl. |

## 4.3 Sample Requests & Responses

## Example A - Standard Order with Customer Reference

## Request:

## POST /orders HTTP/1.1
Host: octopusapi.24sevencommerce.com
X-API-Key: your_api_key
X-API-Secret: your_api_secret
Content-Type: application/json

## Request Body:

## {
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

## Response (201 Created):

## {
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
      "first_name": "Jane",
      "last_name": "Doe",
      "email": "jane.doe@example.com"
    },
    "line_items": [
      {
        "id": "li_021",
        "variant_id": "var_002",
        "title": "Classic Cotton T-Shirt",
        "variant_title": "Medium / White",
        "sku": "TS-M-WHT",
        "quantity": 2,
        "price": "29.99",
        "total": "59.98",
        "requires_shipping": true,
        "taxable": true
      },
      {
        "id": "li_022",
        "variant_id": "var_010",
        "title": "Merino Wool Sweater",
        "variant_title": "Small / Oatmeal",
        "sku": "MW-S-OAT",
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

## Example B - Paid B2B Order with Billing Address

## Request Body:

## {
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

## Response (201 Created):

## {
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

## Example C - Validation Error Response

## Request Body (missing required fields):

## {
  "note": "This order has no line items or email"
}

## Response (422 Unprocessable Entity):

## {
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

## 4.4 Validation Rules

## email is required and must be a valid email format

## line_items is required and must contain at least one item

## Each line item must have a valid variant_id that exists in the shop

## quantity must be a positive integer (minimum: 1)

## price overrides, if provided, must be positive decimal strings

## If any line item has requires_shipping: true, shipping_address is required

## country_code in address objects must be a valid ISO 3166-1 alpha-2 code

## currency, if provided, must be a valid ISO 4217 code

## discount_codes entries must reference codes that exist and are active in the shop

## financial_status must be one of: pending, authorized, paid

## source_name must be one of: api, web, pos, mobile

## 4.5 Business Logic & Side Effects

## Inventory is decremented for each line item at the shop's default location when the order is created with financial_status: paid. For pending/authorized orders, inventory is reserved but not decremented.

## If send_receipt is true, a confirmation email is dispatched to the provided email address.

## If a customer.id is provided, the order is associated with that customer record and their orders_count and total_spent are updated.

## discount_codes are validated at creation time. An invalid or expired code returns a 422 error.

## Tax is calculated automatically based on shop tax settings and the shipping_address jurisdiction.

## The order is created with status: open and fulfillment_status: unfulfilled.

## A webhook event orders/create is dispatched to all registered webhook subscribers.

## PUT /orders/{order_id} - Update Order

## 5.1 Endpoint Definition

PUT   /orders/{order_id}   Update fields on an existing order

| Property | Value |
| --- | --- |
| HTTP Method | PUT |
| URL | https://octopusapi.24sevencommerce.com/admin/api/2020-01/orders/{order_id}.json |
| Content-Type | application/json |
| Auth Required | Yes - X-API-Key / X-API-Secret or Bearer token |
| Required OAuth Scope | write_orders |
| Success Response | 200 OK |
| Idempotent | Yes - same request body produces same result |
| Partial Updates | Supported - only fields included in the body are updated |

## 5.2 Updatable Fields

The following fields may be updated via PUT. System-managed fields (id, order_number, totals, fulfillment_status, timestamps) are read-only and ignored if included in the request body.

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| email | string | No | Update the contact email address for this order. |
| phone | string | No | Update the contact phone number (E.164 format). |
| shipping_address | object | No | Update the shipping destination. Only allowed if order is unfulfilled. |
| billing_address | object | No | Update the billing address. Allowed at any order status. |
| note | string | No | Update the internal order note (max 5,000 chars). |
| tags | string | No | Replace all order tags with this new comma-separated value. |
| email_notif | boolean | No | Trigger a notification email to the customer about the update. |

WARNING:  Line items, discount codes, and shipping lines cannot be modified after order creation. To change order contents, cancel and recreate the order, or use the Refund API.

## 5.3 Sample Requests & Responses

### Example A - Update Email, Tags, and Note

Request:
PUT /orders/ord_1010 HTTP/1.1
Request Body:
{
  "email": "jane.new@example.com",
  "note": "Customer updated delivery instructions: ring doorbell twice",
  "tags": "eco, api-order, updated",
  "email_notif": false
}
Response (200 OK):
{
  "order": {
    "id": "ord_1010",
    "order_number": 1010,
    "email": "jane.new@example.com",
    "status": "open",
    "financial_status": "pending",
    "fulfillment_status": "unfulfilled",
    "note": "Customer updated delivery instructions: ring doorbell twice",
    "tags": "eco, api-order, updated",
    "total_price": "171.25",
    "updated_at": "2024-07-15T13:00:00Z"
  }
}

### Example B - Update Shipping Address (before fulfillment)

Request Body:
{
  "shipping_address": {
    "first_name": "Jane",
    "last_name": "Doe",
    "address1": "789 Pine Street",
    "address2": "Apt 3B",
    "city": "San Francisco",
    "province": "California",
    "province_code": "CA",
    "zip": "94115",
    "country_code": "US",
    "phone": "+14155550999"
  },
  "email_notif": true
}
Response (200 OK):
{
  "order": {
    "id": "ord_1010",
    "order_number": 1010,
    "shipping_address": {
      "first_name": "Jane",
      "last_name": "Doe",
      "address1": "789 Pine Street",
      "address2": "Apt 3B",
      "city": "San Francisco",
      "province": "California",
      "zip": "94115",
      "country_code": "US",
      "phone": "+14155550999"
    },
    "updated_at": "2024-07-15T13:30:00Z"
  }
}

### Example C - Attempt to Update a Cancelled Order

Request Body:
{
  "note": "Trying to update after cancellation"
}
Response (422 Unprocessable Entity):
{
  "error": {
    "code": "ORDER_NOT_EDITABLE",
    "message": "Order ord_1005 cannot be updated because it has been cancelled.",
    "field": "status",
    "status": 422
  }
}

### Example D - Attempt to Update Shipping on a Fulfilled Order

Response (422 Unprocessable Entity):
{
  "error": {
    "code": "SHIPPING_ADDRESS_LOCKED",
    "message": "Shipping address cannot be changed after fulfillment has begun.",
    "field": "shipping_address",
    "status": 422
  }
}

## 5.4 Validation Rules

The order_id in the URL must refer to an existing order; returns 404 if not found
email, if provided, must be a valid email format
phone, if provided, must be in E.164 format
shipping_address updates are blocked if fulfillment_status is fulfilled or partial
System-set fields included in the request body are silently ignored (not treated as errors)
An empty request body (no updatable fields) returns 200 OK with the unchanged order

## 5.5 Business Logic & Side Effects

If email_notif: true is included, an order update notification email is sent to the order's email address after a successful update.
Updating shipping_address does not recalculate shipping costs. If the new address would incur different charges, cancel and recreate the order.
Tag updates are a full replacement - the existing tag string is overwritten by the new value. To append tags, retrieve the current tags first.
A webhook event orders/updated is dispatched to all registered webhook subscribers on every successful update.

## 6. DELETE /orders/{order_id} - Delete Order

## 6.1 Endpoint Definition

DELETE   /orders/{order_id}   Permanently delete an order

| Property | Value |
| --- | --- |
| HTTP Method | DELETE |
| URL | https://octopusapi.24sevencommerce.com/admin/api/2020-01/orders/{order_id}.json |
| Auth Required | Yes - X-API-Key / X-API-Secret or Bearer token |
| Required OAuth Scope | write_orders |
| Success Response | 200 OK with deleted order summary |
| Idempotent | Yes - deleting an already-deleted order returns 404 |
| Reversible | No - deletion is permanent and cannot be undone |

CAUTION:  DELETE is restricted to test/sandbox orders only. Orders that have payment transactions, fulfillments, or refunds attached must be cancelled (POST /orders/{id}/cancel) instead of deleted. Attempting to delete a live order with financial activity returns a 422 error.

## 6.2 Sample Requests & Responses

### Example A - Successful Deletion of a Test Order

Request:
DELETE /orders/ord_test_999 HTTP/1.1
Host: octopusapi.24sevencommerce.com
X-API-Key: your_api_key
X-API-Secret: your_api_secret
Response (200 OK):
{
  "deleted": true,
  "id": "ord_test_999",
  "order_number": 9999,
  "deleted_at": "2024-07-15T16:00:00Z",
  "message": "Order ord_test_999 has been permanently deleted."
}

### Example B - Order Not Found

Response (404 Not Found):
{
  "error": {
    "code": "RESOURCE_NOT_FOUND",
    "message": "No order found with ID ord_xxxxxx.",
    "field": "order_id",
    "status": 404
  }
}

### Example C - Order Has Financial Transactions (Cannot Delete)

Response (422 Unprocessable Entity):
{
  "error": {
    "code": "ORDER_NOT_DELETABLE",
    "message": "Order ord_1010 cannot be deleted because it has associated payment transactions.",
    "hint": "Use POST /orders/ord_1010/cancel to cancel this order instead.",
    "status": 422
  }
}

### Example D - Order Already Cancelled (Safe to Delete)

A cancelled order with no transaction history (e.g., cancelled before payment) can be deleted:
Request:
DELETE /orders/ord_cancelled_test HTTP/1.1
Response (200 OK):
{
  "deleted": true,
  "id": "ord_cancelled_test",
  "deleted_at": "2024-07-15T16:05:00Z",
  "message": "Order ord_cancelled_test has been permanently deleted."
}

## 6.3 Deletion Rules & Constraints

An order may only be deleted if ALL of the following conditions are true:

| Condition | Allowed | Notes |
| --- | --- | --- |
| Order has no payment transactions | YES | Zero transactions - typically a test order or cancelled before payment |
| Order has no fulfillments | YES | No items have been shipped or marked fulfilled |
| Order has no refunds | YES | No refund records exist on the order |
| Order has payment transactions | NO | Cancel instead using POST /orders/{id}/cancel |
| Order has been fulfilled | NO | Cannot delete once fulfillment has started |
| Order has refunds | NO | Cannot delete orders with existing refund records |

WARNING:  In the production environment, only orders created via the API (source_name: api) with no financial activity can be deleted. All other orders should be cancelled using the POST /orders/{id}/cancel endpoint.

## 6.4 Business Logic & Side Effects

Deletion is permanent and irreversible. There is no soft-delete or recycle bin.
If the order was associated with a customer record, the customer's orders_count is decremented by 1 after deletion.
Inventory is not automatically restocked on deletion. Use POST /orders/{id}/cancel with restock: true if inventory should be returned.
A webhook event orders/delete is dispatched to all registered webhook subscribers with the deleted order ID.
Deleted orders are excluded from all reporting and analytics data.

## 7. Error Reference for Order Endpoints

All errors follow the standard Octopus Bridge error envelope. Below is the complete reference for errors specific to the POST, PUT, and DELETE order endpoints.

| HTTP Code | Status | Description |
| --- | --- | --- |
| 201 | Created | POST - Order created successfully. |
| 200 | OK | PUT / DELETE - Order updated or deleted successfully. |
| 400 | Bad Request | Malformed JSON body. Ensure Content-Type: application/json is set. |
| 401 | Unauthorized | Missing or invalid API credentials. |
| 403 | Forbidden | API key lacks write_orders scope. |
| 404 | Not Found | PUT / DELETE - The specified order_id does not exist. |
| 422 | Unprocessable | Validation failed, order not editable, or deletion not permitted. See errors array. |
| 429 | Rate Limited | Request rate limit exceeded. Wait for Retry-After seconds. |
| 500 | Internal Error | Unexpected server error. Retry with exponential backoff; contact support if persistent. |

## 7.1 Order-Specific Error Codes

| Error Code | Endpoint | Description |
| --- | --- | --- |
| VALIDATION_ERROR | POST, PUT | One or more request fields failed validation. See errors[] array for field-level details. |
| ORDER_NOT_FOUND | PUT, DELETE | No order exists with the provided order_id. |
| ORDER_NOT_EDITABLE | PUT | Order cannot be updated - it has been cancelled or closed. |
| SHIPPING_ADDRESS_LOCKED | PUT | Shipping address cannot be changed after fulfillment has started. |
| ORDER_NOT_DELETABLE | DELETE | Order cannot be deleted due to existing transactions, fulfillments, or refunds. |
| INVALID_VARIANT | POST | One or more variant_id values in line_items do not exist in the shop. |
| INVALID_DISCOUNT_CODE | POST | One or more discount_codes do not exist or have expired. |
| INSUFFICIENT_INVENTORY | POST | Insufficient stock for one or more line items at the requested location. |
| INVALID_CURRENCY | POST | The specified currency code is not a valid ISO 4217 code. |
| INVALID_COUNTRY_CODE | POST, PUT | The country_code in an address is not a valid ISO 3166-1 alpha-2 code. |
