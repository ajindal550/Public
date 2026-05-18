# Customers

## 12.1 Overview

The Customers resource provides read access to customer records in the connected shop. Customer records include contact information, order history summaries, and address data.

## 12.2 GET /customers

GET   /customers  Retrieve a list of customers

| Property | Value |
| --- | --- |
| HTTP Method | GET |
| URL | https://api.octopusbridge.com/v1/customers |
| Auth Required | Yes |
| Required OAuth Scope | read_customers |
| Success Response | 200 OK |

### Query Parameters

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| limit | integer | No | Number of results per page. Default: 50, Max: 250. |
| page | integer | No | Page number. Default: 1. |
| since_id | string | No | Return customers with ID after this value. |
| email | string | No | Filter by customer email address (exact match). |
| created_at_min | datetime | No | Return customers created at or after this datetime. |
| created_at_max | datetime | No | Return customers created at or before this datetime. |
| fields | string | No | Comma-separated list of fields to include. |
| ids | string | No | Comma-separated list of specific customer IDs. |

Sample Request:

GET /customers?limit=5 HTTP/1.1
Host: api.octopusbridge.com
X-API-Key: your_api_key
X-API-Secret: your_api_secret

Sample Response (200 OK):

{
"customers": [
{
"id": "cust_jane01",
"first_name": "Jane",
"last_name": "Doe",
"email": "jane.doe@example.com",
"phone": "+14155550123",
"orders_count": 7,
"total_spent": "457.43",
"currency": "USD",
"tags": "vip, repeat-customer",
"verified_email": true,
"accepts_marketing": true,
"default_address": {
"address1": "456 Elm Street",
"city": "San Francisco",
"province_code": "CA",
"zip": "94102",
"country_code": "US"
},
"created_at": "2022-03-10T09:00:00Z",
"updated_at": "2024-07-10T14:30:00Z"
}
],
"pagination": { "total": 1540, "page": 1, "limit": 5, "pages": 308 }
}
