# Transactions

## 13.1 Overview

Transactions represent payment events associated with an order - such as authorizations, captures, refunds, and voids. Transactions are read-only through this API; payment processing is handled by the connected payment gateway.

## 13.2 GET /orders/{order_id}/transactions

GET   /orders/{order_id}/transactions  Retrieve all transactions for a specific order

| Property | Value |
| --- | --- |
| HTTP Method | GET |
| URL | https://octopusapi.24sevencommerce.com/admin/api/2020-01/orders/{order_id}/transactions.json |
| Auth Required | Yes |
| Required OAuth Scope | read_orders |
| Success Response | 200 OK |

Sample Request:

GET /orders/ord_1001/transactions HTTP/1.1
Host: octopusapi.24sevencommerce.com
X-API-Key: your_api_key
X-API-Secret: your_api_secret

Sample Response (200 OK):

{
"transactions": [
{
"id": "txn_001",
"order_id": "ord_1001",
"kind": "authorization",
"status": "success",
"amount": "68.88",
"currency": "USD",
"gateway": "stripe",
"authorization": "auth_abc123",
"created_at": "2024-07-10T14:30:00Z"
},
{
"id": "txn_002",
"order_id": "ord_1001",
"kind": "capture",
"status": "success",
"amount": "68.88",
"currency": "USD",
"gateway": "stripe",
"parent_id": "txn_001",
"created_at": "2024-07-10T14:31:00Z"
}
]
}

### Transaction Object Fields

| Field | Type | Description |
| --- | --- | --- |
| id | string | Unique transaction identifier. |
| order_id | string | ID of the order this transaction belongs to. |
| kind | string | Transaction type: authorization, capture, sale, refund, void. |
| status | string | Transaction result: success, failure, pending, error. |
| amount | string | Transaction amount as a decimal string. |
| currency | string | ISO 4217 currency code for this transaction. |
| gateway | string | Payment gateway that processed the transaction. |
| authorization | string | Authorization code returned by the payment gateway. |
| parent_id | string | ID of the parent transaction (e.g., authorization for a capture). |
| created_at | datetime | Timestamp when the transaction was created (ISO 8601). |
