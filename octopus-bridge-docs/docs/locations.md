# Locations

## 6.1 Overview

Locations represent physical or virtual places where inventory is stored and orders are fulfilled (e.g., warehouses, retail stores, fulfillment centers). Locations are read-only through the API - they are configured in the shop admin.

## 6.2 GET /locations

GET /admin/api/2020-01/locations.json

| Property | Value |
| --- | --- |
| HTTP Method | GET |
| URL | https://api.octopusbridge.com/v1/locations |
| Auth Required | Yes |
| Required OAuth Scope | read_inventory |
| Success Response | 200 OK |

Sample Request:

GET /admin/api/2020-01/locations.json

Sample Response (200 OK):

```json
{
"locations": [
{
"id": 1000,
"name": "smart-omni-channel-qa",
"address1": "80 Citizen Court, Unit 1",
"address2": "",
"city": "San Jose ",
"zip": "95138",
"State": "California",
"country": "CA",
"phone": "(111) 111-1111",
"created_at": "2020-04-15T02:01:29-00:00",
"updated_at": "2020-07-07T23:01:02-00:00",
"country_code": "CA",
"country_name": "USA",
"State_code": "CA",
"legacy": true,
"active": true,
"admin_graphql_api_id": ""
},
{
"id": 1001,
"name": "80 Citizen Court, Unit 1",
"address1": "80 Citizen Court, Unit 1",
"address2": "",
"city": "San Jose",
"zip": "95138",
"State": "California",
"country": "CA",
"phone": "",
"created_at": "2020-04-15T02:01:32-00:00",
"updated_at": "2020-04-15T02:01:37-00:00",
"country_code": "CA",
"country_name": "USA",
"State_code": "CA",
"legacy": true,
"active": true,
"admin_graphql_api_id": ""
}
]
}
```

### Location Object Fields

| Field | Type | Description |
| --- | --- | --- |
| id | string | Unique location identifier. |
| name | string | Display name of the location. |
| address1 | string | Street address of the location. |
| city | string | City of the location. |
| province_code | string | State/province abbreviation. |
| zip | string | Postal/ZIP code. |
| country_code | string | ISO 3166-1 alpha-2 country code. |
| phone | string | Contact phone number for the location. |
| active | boolean | Whether the location is currently active for fulfillment. |
| created_at | datetime | Timestamp when the location was created (ISO 8601). |
