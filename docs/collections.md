# Custom Collections

## 8.1 Overview

A custom collection is a grouping of products that a merchant can create to make their store easier to browse. The merchant creates a custom collection (Category) and then selects the products that will go into it.

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | /custom_collections | List all custom collections |
| POST | /custom_collections | Create a new custom collection |
| PUT | /custom_collections/{id} | Update an existing custom collection |
| DELETE | /custom_collections/{id} | Delete a custom collection |
| POST | /custom_collections/bulk | Create or update multiple collections |

## 8.2 GET /custom_collections

GET   /custom_collections  Retrieve a list of custom collections

### Query Parameters

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| limit | integer | No | Number of results per page. Default: 50, Max: 250. |
| page | integer | No | Page number. Default: 1. |
| since_id | string | No | Return collections with ID after this value. |
| title | string | No | Filter by collection title. |
| product_id | string | No | Filter to collections containing this product ID. |
| fields | string | No | Comma-separated list of fields to return. |

Request:
GET /admin/api/2020-01/custom_collections.json
Sample Response (200 OK):

HTTP/1.1 200 OK
```json
{
"custom_collection": [
{
"id": 1000,
"handle": "stone",
"title": "Stone",
"updated_at": "2020-04-28T11:20:14-00:00",
"body_html": "",
"published_at": "2020-04-17T22:53:35-00:00",
"sort_order": null,
"template_suffix": null,
"published_scope": null,
"admin_graphql_api_id": null
},
{
"id": 1001,
"handle": "planting-supplies",
"title": "Planting Supplies",
"updated_at": "2020-06-09T21:13:07-00:00",
"body_html": "",
"published_at": "2020-04-17T22:53:35-00:00",
"sort_order": null,
"template_suffix": null,
"published_scope": null,
"admin_graphql_api_id": null
}
]
}
```

GET a specific collection by its ID

Request

GET /admin/api/2020-01/custom_collections/{Custom_Collection_ID}.json

Response

HTTP/1.1 200 OK
```json
{
"custom_collection": {
"id": 1001,
"handle": "planting-supplies",
"title": "Planting Supplies",
"updated_at": "2020-06-09T21:13:07-00:00",
"body_html": "",
"published_at": "2020-04-17T22:53:35-00:00",
"sort_order": null,
"template_suffix": null,
"published_scope": null,
"admin_graphql_api_id": null
}
}
```

Count all custom collections

Request

GET /admin/api/2020-01/custom_collections/count.json

Response

HTTP/1.1 200 OK
```json
{
"count": 2
}
```

## 8.3 POST /custom_collections

POST /admin/api/2020-01/custom_collections.json

### Request Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| title | string | Yes | Collection title (max 255 characters). |
| body_html | string | No | Collection description in HTML. |
| handle | string | No | URL handle (slug). Auto-generated from title if omitted. |
| published | boolean | No | Whether the collection is visible in the storefront. Default: true. |
| sort_order | string | No | Product sort order: manual, best-selling, alpha-asc, alpha-desc, price-asc, price-desc, created, created-desc. |
| image | object | No | Collection image object with src URL. |

Sample Request Body:

```json
{
"custom_collection": {
"body_html": "<p>footwear items</p>",
"handle": "sale-items-footwear",
"title": "SALE ITEMS > FOOTWEAR"
}
}
```

Sample Response (201 Created):

HTTP/1.1 200 OK
```json
{
"custom_collection": {
"id": 1000,
"handle": "sale-items-footwear",
"title": "SALE ITEMS > FOOTWEAR",
"updated_at": "2020-06-25T07:31:47-00:00",
"body_html": "<p>footwear items</p>",
"published_at": "2020-04-17T22:53:35-00:00",
"sort_order": null,
"template_suffix": null,
"published_scope": null,
"admin_graphql_api_id": null
}
}
```

## 8.4 PUT /custom_collections/{collection_id}

PUT   /admin/api/2020-01/custom_collections/{Custom_Collection_ID}.json
Sample Request Body:

```json
{
"custom_collection": {
"id": 1000,
"body_html": "<p>footwear items</p>",
"handle": "sale-items-footwear",
"title": "SALE ITEMS > FOOTWEAR"
}
}
```

Sample Response (200 OK):

HTTP/1.1 200 OK
```json
{
"custom_collection": {
"id": 1000,
"handle": "sale-items-footwear",
"title": "SALE ITEMS > FOOTWEAR",
"updated_at": "2020-06-25T07:31:47-00:00",
"body_html": "<p>footwear items</p>",
"published_at": "2020-04-17T22:53:35-00:00",
"sort_order": null,
"template_suffix": null,
"published_scope": null,
"admin_graphql_api_id": null
}
}
```

## 8.5 DELETE /custom_collections/{collection_id}

DELETE /admin/api/2020-01/custom_collections/{Custom_Collection_ID}.json

NOTE: Deleting a collection does not delete the products within it. Only the collection and its collect associations are removed.

Sample Response (200 OK):

HTTP/1.1 200 OK
{
}

## 8.6 Bulk POST /custom_collections

## The bulk custom collection POST endpoint is used to POST custom collections or categories in bulk in a single request.

POST/admin/api/2020-01/bulkcustom_collections.json
Note:
We have introduced a new attribute "sv_temp_id". You can use this attribute to send your internal ID.

| Property | Value |
| --- | --- |
| Max Collections per Request | 250 |
| Required OAuth Scope | write_collections |
| Success Response | 200 OK with per-item results |

Given below is the cURL request to POST custom collections in bulk:

```json
{
"entity_type": "category",
"entity_count": 20,
"created_at": "2023-03-07T08:45:04-05:00",
"items": [
{
"sv_temp_id": 100,
"title": "BulkInsert_0",
"body_html": "BulkInsert_0",
"image": ""
},
{
"sv_temp_id": 101,
"title": "BulkInsert_1",
"body_html": "",
"image": ""
},
{
"sv_temp_id": 102,
"title": "BulkInsert_2",
"body_html": "",
"image": ""
},
{
"sv_temp_id": 103,
"title": "BulkInsert_3",
"body_html": "",
"image": ""
},
{
"sv_temp_id": 104,
"title": "BulkInsert_4",
"body_html": "",
"image": ""
},
{
"sv_temp_id": 105,
"title": "BulkInsert_5",
"body_html": "",
"image": ""
},
{
"sv_temp_id": 106,
"title": "BulkInsert_6",
"body_html": "",
"image": ""
},
{
"sv_temp_id": 107,
"title": "BulkInsert_7",
"body_html": "",
"image": ""
},
{
"sv_temp_id": 108,
"title": "BulkInsert_8",
"body_html": "",
"image": ""
},
{
"sv_temp_id": 109,
"title": "BulkInsert_9",
"body_html": "",
"image": ""
},
{
"sv_temp_id": 110,
"title": "BulkInsert_10",
"body_html": "",
"image": ""
},
{
"sv_temp_id": 111,
"title": "BulkInsert_11",
"body_html": "",
"image": ""
},
{
"sv_temp_id": 112,
"title": "BulkInsert_12",
"body_html": "",
"image": ""
},
{
"sv_temp_id": 113,
"title": "BulkInsert_13",
"body_html": "",
"image": ""
},
{
"sv_temp_id": 114,
"title": "BulkInsert_14",
"body_html": "",
"image": ""
},
{
"sv_temp_id": 115,
"title": "BulkInsert_15",
"body_html": "",
"image": ""
},
{
"sv_temp_id": 116,
"title": "BulkInsert_16",
"body_html": "",
"image": ""
},
{
"sv_temp_id": 117,
"title": "BulkInsert_17",
"body_html": "",
"image": ""
},
{
"sv_temp_id": 118,
"title": "BulkInsert_18",
"body_html": "",
"image": ""
},
{
"sv_temp_id": 119,
"title": "BulkInsert_19",
"body_html": "",
"image": ""
},
{
"sv_temp_id": 120,
"title": "BulkInsert_20",
"body_html": "",
"image": ""
},

]
}
```
