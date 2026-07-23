# Purchase Orders

> **📌 Retail Advisor integrations only.** The Purchase Orders endpoints are used **only** when the downstream destination is [Retail Advisor](/#/?id=retail-advisor-integration). Pushing PO activity from a merchant's POS lets Retail Advisor build **vendor performance insights**, **reorder recommendations**, and answer questions like *"Which vendors need a PO?"* and *"What should I reorder today?"*. If you are integrating with Shopify, BigCommerce, or any non-RA destination, you do **not** need this section.

## 11.1 Overview

The Purchase Orders resource enables creation and management of purchase orders and their associated line items within the connected shop. Purchase orders track inbound inventory from suppliers, including ordered, received, and arrival dates, as well as line-item-level pricing and receipt confirmation.

| Method | Endpoint | Description |
| --- | --- | --- |
| POST | /admin/api/2025-09/PurchaseOrder/CreateOrder.json | Create a new purchase order |
| POST | /admin/api/2025-09/PurchaseOrder/Purchaseorderline.json | Add a line item to an existing purchase order |

NOTE: Purchase Order endpoints use the /admin/api/2025-09/ base path and are versioned independently from the core /v1/ endpoints. Include your standard X-API-Key and X-API-Secret authentication headers on all requests.

## 11.2 POST /PurchaseOrder/CreateOrder.json

```http
POST   /admin/api/2025-09/PurchaseOrder/CreateOrder.json  Create a new purchase order
```

| Property | Value |
| --- | --- |
| HTTP Method | POST |
| URL | https://octopusapi.24sevencommerce.com/admin/api/2025-09/PurchaseOrder/CreateOrder.json |
| Content-Type | application/json |
| Auth Required | Yes - X-API-Key / X-API-Secret |
| Required OAuth Scope | write_orders |
| Success Response | 200 OK |
| Idempotent | No - each call creates a new purchase order |

### Request Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| orderedDate | datetime | Yes | Date and time the purchase order was placed (ISO 8601). |
| receivedDate | datetime | No | Date and time inventory was received at the warehouse (ISO 8601). |
| arrivalDate | datetime | No | Expected or actual arrival date at destination (ISO 8601). |
| shopID | integer | Yes | ID of the connected shop this purchase order belongs to. |
| Pos_OrderID | integer | No | Reference ID from the Point of Sale or external system. |
| complete | boolean | No | Indicates whether the purchase order is fully received. Default: false. |
| archived | boolean | No | Indicates whether the purchase order is archived. Default: false. |
| discount | decimal | No | Per-unit or order-level discount amount. |
| totalDiscount | decimal | No | Total discount amount applied across all line items. |
| totalQuantity | integer | No | Total number of units across all line items on this order. |
| createTime | datetime | No | Timestamp when the purchase order record was created (ISO 8601). |
| timeStamp | datetime | No | Last modification timestamp for the purchase order (ISO 8601). |

Sample Request:

```http
POST /admin/api/2025-09/PurchaseOrder/CreateOrder.json HTTP/1.1
Host: octopusapi.24sevencommerce.com
X-API-Key: your_api_key
X-API-Secret: your_api_secret
Content-Type: application/json
```

Request Body:

```json
{
"orderedDate":   "2026-03-20T10:00:00",
"receivedDate":  "2026-03-22T10:00:00",
"arrivalDate":   "2026-03-25T10:00:00",
"shopID":        101,
"Pos_OrderID":   5001,
"complete":      false,
"archived":      false,
"discount":      5.00,
"totalDiscount": 10.00,
"totalQuantity": 50,
"createTime":    "2026-03-20T09:00:00",
"timeStamp":     "2026-03-20T09:00:00"
}
```

Response (200 OK):

```json
{
"status":  "Success",
"message": "Purchase order created successfully.",
"orderId": 3021
}
```

### Response Fields

| Field | Type | Description |
| --- | --- | --- |
| status | string | Result of the operation. Success indicates the purchase order was created. |
| message | string | Human-readable confirmation message. |
| orderId | integer | The system-generated ID of the newly created purchase order. Use this ID when creating line items via POST /PurchaseOrder/Purchaseorderline.json. |

## 11.3 POST /PurchaseOrder/Purchaseorderline.json

```http
POST   /admin/api/2025-09/PurchaseOrder/Purchaseorderline.json  Add a line item to a purchase order
```

| Property | Value |
| --- | --- |
| HTTP Method | POST |
| URL | https://octopusapi.24sevencommerce.com/admin/api/2025-09/PurchaseOrder/Purchaseorderline.json |
| Content-Type | application/json |
| Auth Required | Yes - X-API-Key / X-API-Secret |
| Required OAuth Scope | write_orders |
| Success Response | 200 OK |

NOTE: The OrderID in the request body must match a valid purchase order ID returned from POST /PurchaseOrder/CreateOrder.json. Create the purchase order header first, then add line items using the returned orderId.

### Request Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| OrderID | integer | Yes | ID of the parent purchase order. Must match a valid orderId returned from CreateOrder. |
| ItemID | string | Yes | SKU or item identifier for the product being ordered. |
| Quantity | integer | Yes | Number of units ordered for this line item. Must be a positive integer. |
| Price | decimal | Yes | Unit cost price for this line item (e.g., 29.99). |
| OriginalPrice | decimal | No | Original list price before any discounts are applied. |
| Total | decimal | No | Total line item cost (Price × Quantity). Calculated as Quantity * Price. |
| ShippingCost | decimal | No | Shipping cost allocated to this line item. |
| NumReceived | integer | No | Number of units physically received for this line item. |
| CheckedIn | boolean | No | Indicates whether this line item has been checked in at the warehouse. Default: false. |
| CreateTime | datetime | No | Timestamp when the line item record was created (ISO 8601). |
| TimeStamp | datetime | No | Last modification timestamp for this line item (ISO 8601). |

Sample Request:

```http
POST /admin/api/2025-09/PurchaseOrder/Purchaseorderline.json HTTP/1.1
Host: octopusapi.24sevencommerce.com
X-API-Key: your_api_key
X-API-Secret: your_api_secret
Content-Type: application/json
```

Request Body:

```json
{
"OrderID":       3021,
"ItemID":        "SKU-78923",
"Quantity":      10,
"Price":         29.99,
"OriginalPrice": 34.99,
"Total":         299.90,
"ShippingCost":  5.00,
"NumReceived":   10,
"CheckedIn":     true,
"CreateTime":    "2026-03-20T09:30:00",
"TimeStamp":     "2026-03-20T09:30:00"
}
```

Response (200 OK):

```json
{
"status":  "Success",
"message": "Order line created successfully.",
"orderId": 0
}
```

### Response Fields

| Field | Type | Description |
| --- | --- | --- |
| status | string | Result of the operation. Success indicates the line item was created. |
| message | string | Human-readable confirmation message. |
| orderId | integer | Returns 0 for line item creation. The parent purchase order ID is not echoed here. |

### Typical Workflow

Purchase orders are created in two steps. First, create the purchase order header to obtain an orderId, then add one or more line items referencing that orderId:

// Step 1 - Create the purchase order header
```http
POST /admin/api/2025-09/PurchaseOrder/CreateOrder.json
```
→ Response: { "orderId": 3021 }

// Step 2 - Add line items using the returned orderId
```http
POST /admin/api/2025-09/PurchaseOrder/Purchaseorderline.json
Body: { "OrderID": 3021, "ItemID": "SKU-78923", ... }
```

// Repeat Step 2 for each additional line item on the same order
