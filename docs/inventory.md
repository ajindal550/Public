# Inventory Levels

## 7.1 Overview

An inventory level represents the available quantity of an inventory item at a specific location. Each inventory level belongs to one inventory item and has one location. For every location where an inventory item is available, there's an inventory level that represents the inventory item's quantity at that location.

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | /inventory_levels | Get inventory levels for variants at locations |
| POST | /inventory_levels/set | Set the inventory level for a variant at a location |
| POST | /inventory_levels/bulk | Set inventory levels for multiple variant/location pairs |

## 7.2 GET /inventory_levels

GET /admin/api/2020-01/inventory_levels.json?inventory_item_ids={Item_Id}&location_ids={Location_Id}

### Query Parameters

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| inventory_item_ids | string | Yes* | Comma-separated list of inventory item IDs. *Required if location_ids not provided. |
| location_ids | string | Yes* | Comma-separated list of location IDs. *Required if inventory_item_ids not provided. |
| limit | integer | No | Number of results per page. Default: 50, Max: 250. |

Sample Request:

GET /admin/api/2020-01/inventory_levels.json?inventory_item_ids={Item_Id}&location_ids={Location_Id}
Sample Response (200 OK):

HTTP/1.1 200 OK
```json
{
"inventory_levels": [
{
"inventory_item_id": 13000,
"location_id": 1000,
"available": 17,
"updated_at": "2020-04-26T00:10:38-00:00",
"admin_graphql_api_id": ""
}
]
}
```

## 7.3 POST /inventory_levels/set

POST   /inventory_levels/set  Set the inventory quantity for a variant at a location

Mandatory fields: location_id, inventory_item_id, available

| Property | Value |
| --- | --- |
| HTTP Method | POST |
| URL | https://api.octopusbridge.com/v1/inventory_levels/set |
| Content-Type | application/json |
| Auth Required | Yes |
| Required OAuth Scope | write_inventory |
| Success Response | 200 OK |

Sample Request Body:

```json
{
"location_id": "1000",
"inventory_item_id": "13000",
"available": "17"
}
```

Sample Response (200 OK):
HTTP/1.1 200 OK
```json
{
"inventory_level": {
"inventory_item_id": 13000,
"location_id": 1000,
"available": 17,
"updated_at": "2020-06-24T14:15:20-00:00",
"admin_graphql_api_id": ""
}
}
```

## 7.4 Bulk POST /inventory_levels

The bulk inventory_levels POST endpoint is used to POST inventory levels in bulk in a single request.

| Property | Value |
| --- | --- |
| HTTP Method | POST |
| URL | https://api.octopusbridge.com/v1/inventory_levels/bulk |
| Content-Type | application/json |
| Auth Required | Yes |
| Required OAuth Scope | write_inventory |
| Max Items per Request | 250 |
| Success Response | 200 OK |

Note:
We have introduced a new attribute "sv_temp_id". You can use this attribute to send your internal ID.

Given below is the cURL request to POST inventory levels in bulk:

```bash
curl --location --request POST 'http://<Merchant Name>:<Access ID>@octopusapi.24sevencommerce.com/admin/api/2020-01/bulkinventory_levels/bulkset.json' \
--header 'X-Octopus-Access-Token: 704A865F-EE2B-4F8B-A290-A8AD3B684F75' \
--header 'Content-Type: application/json' \
--data-raw '{
```
"entity_type": "Inventory_Levels",
"entity_count": 2,
"created_at": "2023-03-07T08:45:04-05:00",
"items": [
```json
{
"sv_temp_id": 100,
"location_id": 1000,
"inventory_item_id": 13000,
"available": 4
},
```
```json
{
"sv_temp_id": 100,
"location_id": 1001,
"inventory_item_id": 13000,
"available": 5
}
```
]
}
'
