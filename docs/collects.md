# Collects

## 9.1 Overview

The Collect resource connects a product to a custom collection. Collects are meant for managing the relationship between products and custom collections. For every product in a custom collection there is a collect that tracks the ID of both the product and the custom collection.

Note: First you need to send updates to all custom collections if there are many.
Once all calls to custom collections are done then you need to send the collects call to all products related to those affected collections.

| Method | Endpoint | Description |
| --- | --- | --- |
| POST | /collects | Add a product to a custom collection |
| GET | /collects | List all collect associations |
| DELETE | /collects/{collect_id} | Remove a product from a collection |
| POST | /collects/bulk | Add multiple products to collections in one request |

## 9.2 POST /collects

POST /admin/api/2020-01/collects.json

Note:
Mandatory fields - Product_id, Collection_id
This call creates a new link between an existing product and an existing collection

| Property | Value |
| --- | --- |
| HTTP Method | POST |
| URL | https://api.octopusbridge.com/v1/collects |
| Content-Type | application/json |
| Auth Required | Yes |
| Required OAuth Scope | write_collections |
| Success Response | 201 Created |

Sample Request Body:

```json
{
"collect": {
"product_id": "10001",
"collection_id": "1001"
}
}
```

Sample Response (201 Created):

HTTP/1.1 201 Created
```json
{
"collect": {
"id": 3,
"collection_id": 1001,
"product_id": 10001,
"created_at": "2020-06-25T06:52:07-00:00",
"updated_at": "2020-06-25T06:55:48-00:00",
"position": 1,
"sort_value": ""
}
}
```

## 9.3 GET /collects

GET /admin/api/2020-01/collects/{collect_id}.json

### Query Parameters

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| collection_id | string | No | Filter by collection ID - returns all products in this collection. |
| product_id | string | No | Filter by product ID - returns all collections containing this product. |
| limit | integer | No | Number of results per page. Default: 50, Max: 250. |
| page | integer | No | Page number. Default: 1. |

Sample Request:

GET /admin/api/2020-01/collects/{collect_id}.json
Sample Response (200 OK):

```json
{   HTTP/1.1 200 OK
{
"collect": {
"id": 3,
"collection_id": 1001,
"product_id": 10001,
"created_at": "2020-06-25T06:52:07-00:00",
"updated_at": "2020-06-25T06:55:48-00:00",
"position": 1,
"sort_value": ""
}
}

## 9.4 DELETE /collects/{collect_id}

DELETE /admin/api/2020-01/collects/1001.json
Sample Request:

DELETE /admin/api/2020-01/collects/1001.json

Sample Response (200 OK):

HTTP/1.1 200 OK
{
}

## 9.5 Bulk POST /collects

The bulk collects POST endpoint is used to create a link between existing products and collections.

POST/admin/api/2020-01/bulkcollects.json

Note:
We have introduced a new attribute "sv_temp_id". You can use this attribute to send your internal ID.

| Property | Value |
| --- | --- |
| Max Items per Request | 250 |
| Required OAuth Scope | write_collections |
| Success Response | 200 OK with per-item results |

Given below is the cURL request to POST Collects in bulk.

curl --location --request POST 'http://Demo1:704A865F-EE2B-4F8B-A290-A8AD3B684F75@stagingapi.24sevencommerce.com/admin/api/2020-01/bulkcollects.json' \
--header 'X-Octopus-Access-Token: 704A865F-EE2B-4F8B-A290-A8AD3B684F75' \
--header 'Content-Type: application/json' \
--data-raw '{
"entity_type": "Collects",
"entity_count": 20,
"created_at": "2023-03-07T08:45:04-05:00",
"items": [
{
"sv_temp_id": 100,
"collection_id": "1005",
"product_id": "10000"
},
{
"sv_temp_id": 101,
"collection_id": "1006",
"product_id": "10000"
},
{
"sv_temp_id": 102,
"collection_id": "1007",
"product_id": "10000"
},
{
"sv_temp_id": 103,
"collection_id": "1008",
"product_id": "10000"
},
{
"sv_temp_id": 104,
"collection_id": "1009",
"product_id": "10000"
},
{
"sv_temp_id": 105,
"collection_id": "1010",
"product_id": "10000"
},
{
"sv_temp_id": 106,
"collection_id": "1011",
"product_id": "10000"
},
{
"sv_temp_id": 107,
"collection_id": "1012",
"product_id": "10000"
},
{
"sv_temp_id": 108,
"collection_id": "1013",
"product_id": "10000"
},
{
"sv_temp_id": 109,
"collection_id": "1014",
"product_id": "10000"
},
{
"sv_temp_id": 110,
"collection_id": "1015",
"product_id": "10000"
},
{
"sv_temp_id": 111,
"collection_id": "1016",
"product_id": "10000"
},
{
"sv_temp_id": 112,
"collection_id": "1017",
"product_id": "10000"
},
{
"sv_temp_id": 113,
"collection_id": "1018",
"product_id": "10000"
},
{
"sv_temp_id": 114,
"collection_id": "1019",
"product_id": "10000"
},
{
"sv_temp_id": 115,
"collection_id": "1020",
"product_id": "10000"
}
]
}'
