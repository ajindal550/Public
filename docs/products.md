# Products

## 3.1 Overview

The Products resource is the core of the Octopus Bridge API. A product represents a single item for sale in the connected shop. Each product may have multiple variants (e.g., size, color) and images. The API supports full CRUD operations as well as a bulk POST endpoint for high-volume catalog synchronization.

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | /products | Retrieve a list of products with optional filters |
| POST | /products | Create a new product |
| PUT | /products/{product_id} | Update an existing product |
| DELETE | /products/{product_id} | Delete a product |
| POST | /products/bulk | Create or update multiple products in a single request |

## 3.2 GET /products

GET   /products  Retrieve a list of products

| Property | Value |
| --- | --- |
| HTTP Method | GET |
| URL | https://octopusapi.24sevencommerce.com/admin/api/2020-01/products.json |
| Auth Required | Yes |
| Required OAuth Scope | read_products |
| Success Response | 200 OK |

### Query Parameters

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| limit | integer | No | Number of results per page. Default: 50, Max: 250. |
| page | integer | No | Page number for pagination. Default: 1. |
| since_id | string | No | Return products with ID after this value (cursor pagination). |
| title | string | No | Filter by product title (partial match supported). |
| vendor | string | No | Filter by product vendor name. |
| product_type | string | No | Filter by product type. |

Sample Request:

Request

GET https://{merchantname}:{AccessID}@octopusapi.24sevencommerce.com/admin/api/2020-01/products.json

Sample Response (200 OK):

HTTP/1.1 200 OK
```json
{
"product": [{
"id": 13964,
"title": "POTATO",
"sub_description1": "",
"sub_description2": "",
"sub_description3": "",
"body_html": "",
"vendor": "vendor",
"product_type": "product",
"created_at": "2020-04-18T01:25:25-00:00",
"handle": "potato",
"updated_at": "2020-04-18T01:25:25-00:00",
"published_at": "2020-04-18T01:25:25-00:00",
"template_suffix": null,
"published_scope": null,
"tags": "",
"admin_graphql_api_id": "POTATO",
"variants": [{
"id": 16964,
"product_id": 13964,
"title": null,
"price": 9.4900,
"PriceA": "",
"PriceB": "",
"PriceC": "",
"ListPrice": "",
"MSRP": "",
"sku": "9196",
"position": null,
"inventory_policy": "deny",
"fulfillment_service": null,
"inventory_management": "octopus",
"cost_price": "",
"sales_price": "",
"SaleStartDate": "",
"SaleEndDate": "",
"option1": "Default Title",
"option2": null,
"option3": null,
"created_at": "2020-04-18T01:25:25-00:00",
"updated_at": "2020-04-18T01:25:25-00:00",
"taxable": false,
"barcode": "",
"grams": null,
"image_id": null,
"weight": "0",
"weight_unit": "",
"inventory_item_id": 16964,
"inventory_quantity": null,
"old_inventory_quantity": null,
"requires_shipping": null,
"admin_graphql_api_id": null,
"custom_attributes": [{
"attribute_name": "Test Attribute",
"attribute_value": "Test Value"
},

{
"attribute_name": "Test Attribute2",
"attribute_value": "Test Value2"
}
]
}],
"options": [{
"id": 4964,
"product_id": 13964,
"name": "Title",
"position": 1,
"values": [
"Default Title"
]
}],
"images": [

],
"image": null
},
{
"id": 13965,
"title": "POTATO",
"sub_description1": "",
"sub_description2": "",
"sub_description3": "",
"body_html": "",
"vendor": "vendor",
"product_type": "product",
"created_at": "2020-04-18T01:25:26-00:00",
"handle": "potato",
"updated_at": "2020-04-18T01:25:26-00:00",
"published_at": "2020-04-18T01:25:26-00:00",
"template_suffix": null,
"published_scope": null,
"tags": "",
"admin_graphql_api_id": "POTATO",
"variants": [{
"id": 16965,
"product_id": 13965,
"title": null,
"price": 16.9900,
"PriceA": "",
"PriceB": "",
"PriceC": "",
"ListPrice": "",
"MSRP": "",
"sku": "9197",
"position": null,
"inventory_policy": "deny",
"cost_price": "",
"sales_price": "",
"SaleStartDate": "",
"SaleEndDate": "",
"fulfillment_service": null,
"inventory_management": "octopus",
"option1": "Default Title",
"option2": null,
"option3": null,
"created_at": "2020-04-18T01:25:26-00:00",
"updated_at": "2020-04-18T01:25:26-00:00",
"taxable": false,
"barcode": "",
"grams": null,
"image_id": null,
"weight": "0",
"weight_unit": "",
"inventory_item_id": 16965,
"inventory_quantity": null,
"old_inventory_quantity": null,
"requires_shipping": null,
"admin_graphql_api_id": null,
"custom_attributes": [{
"attribute_name": "Test Attribute",
"attribute_value": "Test Value"
},

{
"attribute_name": "Test Attribute2",
"attribute_value": "Test Value2"
}
]

}],
"options": [{
"id": 4965,
"product_id": 13965,
"name": "Title",
"position": 1,
"values": [
"Default Title"
]
}],
"images": [],
"image": null
}
]
}
```

## 3.3 POST /products

POST/admin/api/2020-01/products.json
Note:
Mandatory fields - Title and one Variant must exist in the request and Variant must have SKU, Price, Sales Price for discounted items; Sales start date and Sales end date for applying sales for a period and options for matrix products.

| Property | Value |
| --- | --- |
| HTTP Method | POST |
| URL | https://octopusapi.24sevencommerce.com/admin/api/2020-01/products.json |
| Content-Type | application/json |
| Auth Required | Yes |
| Required OAuth Scope | write_products |
| Success Response | 201 Created |
| Idempotent | No - each call creates a new product |

### Request Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| title | string | Yes | Product title (max 255 characters). |
| body_html | string | No | Product description in HTML format. |
| vendor | string | No | Vendor/brand name for the product. |
| product_type | string | No | Custom product type label. |
| status | string | No | active, draft, or archived. Default: active. |
| tags | string | No | Comma-separated tags for the product. |
| variants | array | No | Array of variant objects. A default variant is created if omitted. |
| images | array | No | Array of image objects with src URLs. |
| options | array | No | Array of option objects (e.g., Size, Color). Required if multiple variants. |

Sample Request Body:

```json
{
"product": {
"title": "3D Wallet",
"sub_description1": "",
"sub_description2": "",
"sub_description3": "",
"product_type": "Wallet",
"vendor": "3d Belt Company",
"tags": "12 & 13,55,73,BB,Brown",
"body_html": "<p><strong>3D Wallet<\/strong><\/p>",
"variants": [{
"barcode": "",
"option1": "Default Title",
"price": "0",
"PriceA": "",
"PriceB": "",
"PriceC": "",
"ListPrice": "",
"MSRP": "",
"cost_price": "",
"sales_price": "",
"salestartdate": "",
"saleenddate": "",
"taxable": "true",
"sku": "      4630",
"inventory_management": "octopus",
"inventory_policy": "continue",
"weight": "12",
"weight_unit": "kg",
"custom_attributes": [{
"attribute_name": "Test Attribute",
"attribute_value": "Test Value"
},
{
"attribute_name": "Test Attribute2",
"attribute_value": "Test Value2"
}
]
}],
}

}
```

Sample Response (201 Created):

HTTP/1.1 201 Created
```json
{
"product": [{
"id": 13964,
"title": "POTATO",
"sub_description1": "",
"sub_description2": "",
"sub_description3": "",
"body_html": "",
"vendor": "vendor",
"product_type": "product",
"created_at": "2020-04-18T01:25:25-00:00",
"handle": "potato",
"updated_at": "2020-04-18T01:25:25-00:00",
"published_at": "2020-04-18T01:25:25-00:00",
"template_suffix": null,
"published_scope": null,
"tags": "",
"admin_graphql_api_id": "POTATO",
"variants": [{
"id": 16964,
"product_id": 13964,
"title": null,
"price": 9.4900,
"PriceA": "",
"PriceB": "",
"PriceC": "",
"ListPrice": "",
"MSRP": "",
"sku": "9196",
"position": null,
"inventory_policy": "deny",
"fulfillment_service": null,
"inventory_management": "octopus",
"option1": "Default Title",
"option2": null,
"option3": null,
"created_at": "2020-04-18T01:25:25-00:00",
"updated_at": "2020-04-18T01:25:25-00:00",
"taxable": false,
"barcode": "",
"grams": null,
"image_id": null,
"weight": "0",
"weight_unit": "",
"cost_price": "",
"sales_price": "",
"salestartdate": "",
"saleenddate": "",
"inventory_item_id": 16964,
"inventory_quantity": null,
"old_inventory_quantity": null,
"requires_shipping": null,
"admin_graphql_api_id": null,
"custom_attributes": [{
"attribute_name": "Test Attribute",
"attribute_value": "Test Value"
},

{
"attribute_name": "Test Attribute2",
"attribute_value": "Test Value2"
}
]
}],
"options": [{
"id": 4964,
"product_id": 13964,
"name": "Title",
"position": 1,
"values": [
"Default Title"
]
}],
"images": [

],
"image": null
}]
}
```
If you are creating a matrix product, you need to send options in the variant node with their names like given below:
"variants": [{
"option1": "General Sizes",
"option2": "General Colours",
"option3": "Shoe Widths",
}],
The options node will contain the values of the options in an array.
"options": [{
"name": "General Sizes"
}, {
"name": "General Colours"
}, {
"name": "Shoe Widths"
}]

## 3.4 PUT /products/{product_id}

PUT   /products/{product_id}  Update an existing product

| Property | Value |
| --- | --- |
| HTTP Method | PUT |
| URL | https://octopusapi.24sevencommerce.com/admin/api/2020-01/products/{product_id}.json |
| Content-Type | application/json |
| Auth Required | Yes |
| Required OAuth Scope | write_products |
| Success Response | 200 OK |
| Partial Updates | Supported - only fields included in the body are updated |

Sample Request Body:

```json
{
"product": {
"id": 632910392,
"title": "New product title"
}
}
```

Sample Response (200 OK):
Product model will return with updated title.

## 3.5 DELETE /products/{product_id}

DELETE   /products/{product_id}  Delete a product and all its variants and images

| Property | Value |
| --- | --- |
| HTTP Method | DELETE |
| URL | https://octopusapi.24sevencommerce.com/admin/api/2020-01/products/{product_id}.json |
| Auth Required | Yes |
| Required OAuth Scope | write_products |
| Success Response | 200 OK |
| Reversible | No - deletion is permanent |

CAUTION: Deleting a product permanently removes all associated variants, images, and inventory records. This action cannot be undone.

Sample Request:

DELETE /admin/api/2020-01/products/632910392.json
Sample Response (200 OK):

## HTTP/1.1 200 OK

## {

## }

## 3.6 Bulk POST /products

POST   /products/bulk  Create or update multiple products in one request

The bulk endpoint accepts an array of product objects and processes them in a single transaction. Use this for high-volume catalog synchronization. Products with an existing id field are updated; those without are created.
POSTadmin/api/2020-01/BulkProduct/bulkpost.json
Note:
Mandatory fields - Title and one Variant must exist in the request and Variant must have SKU, Price, Sales Price for discounted items; Sales start date and Sales end date for applying sales for a period and options for matrix products. We have introduced a new attribute "SV_Temp_ProductId". You can use this attribute to send your internal product ID. Once you receive a Success response from the request, you need to map the "SV_Temp_ProductId" with the "productId" you will receive in response.

| Property | Value |
| --- | --- |
| HTTP Method | POST |
| URL | https://octopusapi.24sevencommerce.com/admin/api/2020-01/BulkProduct/bulkpost.json |
| Content-Type | application/json |
| Auth Required | Yes |
| Required OAuth Scope | write_products |
| Max Products per Request | 250 |
| Success Response | 200 OK with per-item results |

Given below is the cURL request to POST products in bulk:

```bash
curl --location 'http://<Merchant Name>:<Access ID>@shopifyapi.24sevencommerce.com/admin/api/2020-01/BulkProduct/bulkpost.json' \
--header 'X-Octopus-Access-Token: <Access ID> \
--header 'Content-Type: application/json' \
--data '{
```
"entity_type": "Products",
"entity_count": 2,
"created_at": "2024-04-24T05:45:04-08:00",
"items": [
```json
{   "SV_Temp_ProductId": 101,
"title": "TESTPROD5",
"product_type": "Snowboard",
"vendor": "Burton",
"tags": "",
"body_html": "<strong>Good snowboard!</strong>",
"handle": "burton-custom-freestyle-151",
"sub_discription1": null,
"sub_discription2": null,
"sub_discription3": null,
"template_suffix": "",
"published_scope": "web",
"admin_graphql_api_id": "gid://shopify/Product/1071559588",
"images": [],
"image": "",
"variants": [
{
"SV_Temp_variantId": 1009,
"title": "TESTPROD1_VAR3",
"inventory_policy": "deny",
"fulfillment_service": "manual",
"barcode": "",
"grams": "0",
"admin_graphql_api_id": "gid://shopify/ProductVariant/1070325033",
"price": 0.00,
"option1": "XL7777777",
"option2": "",
"option3": "",
"position": 1,
"compare_at_price": null,
"taxable": true,
"sku": "4635",
"inventory_management": "",
"weight": "0",
"weight_unit": "lb",
"image_id": null,
"requires_shipping": true,
"SaleStartDate": null,
"SaleEndDate": null,
"sales_price": null,
"cost_price": null,
"price_a": null,
"price_b": null,
"price_c": null,
"list_price": null,
"msrp": null,
"inventory_quantity": 0,
"old_inventory_quantity": 0,
"inventory_item_id": 0,
"custom_attributes": null
}
],
"options": [
{
"id": 1055547198,
"name": "Title",
"position": 1,
"values": [
"New TitleXL777777"
]
}
],
"metafields": null
},
```
```json
{
"SV_Temp_ProductId": 102,
"title": "TESTPROD6",
"product_type": "Snowboard",
"vendor": "Burton",
"tags": "",
"body_html": "<strong>Good snowboard!</strong>",
"handle": "burton-custom-freestyle-151",
"sub_discription1": null,
"sub_discription2": null,
"sub_discription3": null,
"template_suffix": "",
"published_scope": "web",
"admin_graphql_api_id": "gid://shopify/Product/1071559588",
"images": [],
"image": "",
"variants": [
{
"SV_Temp_variantId": 1009,
"title": "TESTPROD1_VAR4",
"inventory_policy": "deny",
"fulfillment_service": "manual",
"barcode": "",
"grams": "0",
"admin_graphql_api_id": "gid://shopify/ProductVariant/1070325033",
"price": 0.00,
"option1": "XL7777777",
"option2": "",
"option3": "",
"position": 1,
"compare_at_price": null,
"taxable": true,
"sku": "4636",
"inventory_management": "",
"weight": "0",
"weight_unit": "lb",
"image_id": null,
"requires_shipping": true,
"SaleStartDate": null,
"SaleEndDate": null,
"sales_price": null,
"cost_price": null,
"price_a": null,
"price_b": null,
"price_c": null,
"list_price": null,
"msrp": null,
"inventory_quantity": 0,
"old_inventory_quantity": 0,
"inventory_item_id": 0,
"custom_attributes": null
}
],
"options": [
{
"id": 1055547198,
"name": "Title",
"position": 1,
"values": [
"New TitleXL777777"
]
}
],
"metafields": null
}
```
]
}'

Sample Response (200 OK):

```json
{
"entity_type": "Products",
"entity_count": 2,
"created_at": "/Date(1735221673533)/",
"items": [
{
"SV_Temp_ProductId": 101,
"productid": 10055,
"title": "TESTPROD5",
"product_type": "Snowboard",
"vendor": "Burton",
"tags": "",
"body_html": "<strong>Good snowboard!</strong>",
"handle": "burton-custom-freestyle-151",
"sub_description1": null,
"sub_description2": null,
"sub_description3": null,
"template_suffix": null,
"published_scope": "web",
"admin_graphql_api_id": "TESTPROD5",
"images": [],
"image": null,
"variants": [
{
"SV_Temp_variantId": 1009,
"variantId": 13011,
"title": "TESTPROD1_VAR3",
"inventory_policy": "deny",
"fulfillment_service": "manual",
"barcode": "",
"grams": "0",
"admin_graphql_api_id": "gid://shopify/ProductVariant/1070325033",
"price": 0.00,
"option1": "XL7777777",
"option2": "",
"option3": "",
"position": 1,
"compare_at_price": null,
"taxable": true,
"sku": "4635",
"inventory_management": "",
"weight": "0",
"weight_unit": "lb",
"image_id": null,
"requires_shipping": true,
"SaleStartDate": null,
"SaleEndDate": null,
"sales_price": null,
"cost_price": null,
"price_a": null,
"price_b": null,
"price_c": null,
"list_price": null,
"msrp": null,
"inventory_quantity": 0,
"old_inventory_quantity": 0,
"inventory_item_id": 13011,
"custom_attributes": null
}
],
"options": [
{
"id": 1055,
"name": "Title",
"position": 1,
"values": [
"XL7777777"
]
}
],
"metafields": []
},
{
"SV_Temp_ProductId": 102,
"productid": 10056,
"title": "TESTPROD6",
"product_type": "Snowboard",
"vendor": "Burton",
"tags": "",
"body_html": "<strong>Good snowboard!</strong>",
"handle": "burton-custom-freestyle-151",
"sub_description1": null,
"sub_description2": null,
"sub_description3": null,
"template_suffix": null,
"published_scope": "web",
"admin_graphql_api_id": "TESTPROD6",
"images": [],
"image": null,
"variants": [
{
"SV_Temp_variantId": 1009,
"variantId": 13012,
"title": "TESTPROD1_VAR4",
"inventory_policy": "deny",
"fulfillment_service": "manual",
"barcode": "",
"grams": "0",
"admin_graphql_api_id": "gid://shopify/ProductVariant/1070325033",
"price": 0.00,
"option1": "XL7777777",
"option2": "",
"option3": "",
"position": 1,
"compare_at_price": null,
"taxable": true,
"sku": "4636",
"inventory_management": "",
"weight": "0",
"weight_unit": "lb",
"image_id": null,
"requires_shipping": true,
"SaleStartDate": null,
"SaleEndDate": null,
"sales_price": null,
"cost_price": null,
"price_a": null,
"price_b": null,
"price_c": null,
"list_price": null,
"msrp": null,
"inventory_quantity": 0,
"old_inventory_quantity": 0,
"inventory_item_id": 13012,
"custom_attributes": null
}
],
"options": [
{
"id": 1056,
"name": "Title",
"position": 1,
"values": [
"XL7777777"
]
}
],
"metafields": []
}
],
"errors": null
}
```
