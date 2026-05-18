
OCTOPUS BRIDGE
REST API
Complete API Reference — All Endpoints
Authentication | Shop | Products | Images | Variants | Locations | Inventory | Collections | Collects | Orders | Customers | Transactions

[TABLE]
| Document Type | API Reference |
| Version | v1.0 |
| Date | March 2026 |
| Base URL | https://api.octopusbridge.com/v1 |
| Auth Required | Yes — X-API-Key + X-API-Secret (or Bearer token) |
[/TABLE]


CONFIDENTIAL — FOR INTERNAL AND PARTNER USE ONLY


# Table of Contents

1.  Authentication
2.  Shop
2.1 GET /shop
3.  Products
3.1 Overview
3.2 GET /products
3.3 POST /products
3.4 PUT /products/{id}
3.5 DELETE /products/{id}
3.6 Bulk POST /products
4.  Images
4.1 Overview
4.2 POST /products/{id}/images
4.3 PUT /products/{id}/images/{image_id}
4.4 DELETE /products/{id}/images/{image_id}
5.  Variants
5.1 Overview
5.2 GET /products/{id}/variants
5.3 POST /products/{id}/variants
5.4 PUT /variants/{id}
5.5 DELETE /variants/{id}
6.  Locations
6.1 Overview
6.2 GET /locations
7.  Inventory Levels
7.1 Overview
7.2 GET /inventory_levels
7.3 POST /inventory_levels/set
7.4 Bulk POST /inventory_levels
8.  Custom Collections
8.1 Overview
8.2 GET /custom_collections
8.3 POST /custom_collections
8.4 PUT /custom_collections/{id}
8.5 DELETE /custom_collections/{id}
8.6 Bulk POST /custom_collections
9.  Collects
9.1 Overview
9.2 POST /collects
9.3 GET /collects
9.4 DELETE /collects/{id}
9.5 Bulk POST /collects
10.  Orders
10.1 Overview
10.2 GET /orders
10.3 GET /orders/{id}
10.4 POST /orders
10.5 PUT /orders/{id}
10.6 DELETE /orders/{id}
11.  Purchase Orders
11.1 Overview
11.2 POST /PurchaseOrder/CreateOrder.json
11.3 POST /PurchaseOrder/Purchaseorderline.json
12.  Customers
12.1 Overview
12.2 GET /customers
13.  Transactions
13.1 Overview
13.2 GET /orders/{id}/transactions
14.  FAQ
14.1 Product Questions
14.2 Order Questions
14.3 General Questions
15.  Mapping Considerations
15.1 Products
15.2 Orders
16.  Sample Code
16.1 Postman
16.2 C#/.NET


# 1. Authentication

The Octopus Bridge REST API uses API Key + Secret authentication on every request. Alternatively, OAuth 2.0 Bearer tokens may be used for partner integrations.


## API Key Authentication

In order to keep transactions on Octopus Rest API safe and secure, all calls connecting with our APIs must be authenticated when making API calls.

Make Authenticated Requests
An app can make authenticated requests to the Rest API using basic authentication by using merchant name and access ID and by including its ‘X-Octopus-Access-Token’ access ID in the request header.

Basic Authentication

Apps can authenticate through basic HTTP authentication by using their merchant name and Access ID. Rest API can be authenticated by prepending merchant name: AccessID@ to the host name in the URL. For example:

GET https://{merchantname}:{AccessID}@octopusapi.24sevencommerce.com/admin/api/2020-01/shop.json

Note: In request header a key with name ‘X-Octopus-Access-Token’ with value as ‘AccessID’ must be passed to successful authentication.


## OAuth 2.0 Bearer Token

Partners using OAuth 2.0 may obtain a Bearer token and include it in the Authorization header:

Authorization: Bearer {access_token}


[TABLE]
| OAuth Scope | Description |
| read_products | Read access to products, variants, images, inventory |
| write_products | Create, update, and delete products, variants, images, inventory |
| read_orders | Read access to orders and transactions |
| write_orders | Create, update, and delete orders |
| read_customers | Read access to customer records |
| read_inventory | Read access to inventory levels and locations |
| write_inventory | Create and update inventory levels |
| read_collections | Read access to custom collections and collects |
| write_collections | Create, update, and delete collections and collects |
[/TABLE]


TIP: write_* scopes implicitly grant read access. It is best practice to explicitly declare both read and write scopes for self-documenting authorization flows.


## Authentication Errors


[TABLE]
| HTTP Code | Error | Description |
| 401 | Unauthorized | Missing or invalid X-API-Key / X-API-Secret headers, or expired Bearer token. |
| 403 | Forbidden | Credentials are valid but the API key lacks the required OAuth scope for this endpoint. |
[/TABLE]



# 2. Shop

The Shop endpoint returns configuration and metadata about the connected store. This is typically the first call made to verify connectivity and retrieve shop-level defaults such as currency, timezone, and plan information.


## 2.1 GET /shop

Request

GET: https://{merchantname}:{AccessID}@octopusapi.24sevencommerce.com/admin/api/2020-01/shop.json

Sample Response (200 OK):


{
"shop": [
{
"id": 1000,
"name": "smart-omni-channel-qa",
"email": "paul.smith@website_name.com",
"domain": "smart-omni-channel-qa.myshopify.com",
"State": "California",
"country": "USA",
"address1": "80 ABC Court, Unit 1",
"zip": "95138",
"city": "San Jose ",
"source": null,
"phone": "(111) 111-1111",
"latitude": "43.8431978",
"longitude": "-79.3191173",
"primary_locale": "en",
"address2": "",
"created_at": "2020-04-14T16:31:29-00:00",
"updated_at": "2020-07-07T13:31:02-00:00",
"country_code": "CA",
"country_name": "USA",
"currency": “USD”,
"customer_email": "paul.smith@website_name.com",
"timezone": "(GMT-05:00) America/New_York",
"iana_timezone": "America/New_York",
"shop_owner": "Paul Smith",
"money_format": "${{amount}}",
"money_with_currency_format": "${{amount}} CAD",
"weight_unit": "kg",
"State_code": "CA",
"taxes_included": false,
"tax_shipping": true,
"county_taxes": true,
"plan_display_name": "Development",
"plan_name": "affiliate",
"has_discounts": true,
"has_gift_cards": false,
"myshopify_domain": "smart-omni-channel-qa.myshopify.com",
"google_apps_domain": null,
"google_apps_login_enabled": null,
"money_in_emails_format": "${{amount}}",
"money_with_currency_in_emails_format": "${{amount}} CAD",
"eligible_for_payments": true,
"requires_extra_payments_agreement": false,
"password_enabled": true,
"has_storefront": true,
"eligible_for_card_reader_giveaway": false,
"finances": true,
"primary_location_id": 1000,
"force_ssl": true,
"checkout_api_supported": true,
"multi_location_enabled": true,
"setup_required": false,
"pre_launch_enabled": false,
"enabled_presentment_currencies": [
[]
]
},
{
"id": 1001,
"name": "80 ABC Court, Unit 1",
"email": null,
"domain": "",
"State": "California",
"country": "CA",
"address1": "80 ABC Court, Unit 1",
"zip": "95138",
"city": "San Jose",
"source": "",
"phone": "",
"latitude": "",
"longitude": "",
"primary_locale": "",
"address2": null,
"created_at": "2020-04-15T02:01:32-00:00",
"updated_at": "2020-04-15T02:01:37-00:00",
"country_code": "USA",
"country_name": "USA",
"currency": "",
"customer_email": "paul.smith@website_name.com ",
"timezone": "",
"iana_timezone": null,
"shop_owner": "",
"money_format": "",
"money_with_currency_format": "",
"weight_unit": "",
"State_code": "CA",
"taxes_included": false,
"tax_shipping": false,
"county_taxes": null,
"plan_display_name": "",
"plan_name": "",
"has_discounts": null,
"has_gift_cards": null,
"myshopify_domain": "",
"google_apps_domain": "",
"google_apps_login_enabled": "",
"money_in_emails_format": "",
"money_with_currency_in_emails_format": "",
"eligible_for_payments": null,
"requires_extra_payments_agreement": null,
"password_enabled": null,
"has_storefront": null,
"eligible_for_card_reader_giveaway": null,
"finances": null,
"primary_location_id": 1001,
"force_ssl": null,
"checkout_api_supported": null,
"multi_location_enabled": null,
"setup_required": null,
"pre_launch_enabled": null,
"enabled_presentment_currencies": ""
}
]
}

### Shop Object Fields


[TABLE]
| Field | Type | Description |
| id | string | Unique shop identifier. |
| name | string | Display name of the shop. |
| email | string | Primary contact email for the shop. |
| domain | string | Primary storefront domain. |
| currency | string | ISO 4217 default currency code for the shop. |
| timezone | string | Shop timezone in IANA format (e.g., America/New_York). |
| country_code | string | ISO 3166-1 alpha-2 country code where the shop is based. |
| plan_name | string | Current subscription plan name. |
| created_at | datetime | Timestamp when the shop was created (ISO 8601). |
| updated_at | datetime | Timestamp of last modification (ISO 8601). |
[/TABLE]



# 3. Products


## 3.1 Overview

The Products resource is the core of the Octopus Bridge API. A product represents a single item for sale in the connected shop. Each product may have multiple variants (e.g., size, color) and images. The API supports full CRUD operations as well as a bulk POST endpoint for high-volume catalog synchronization.


[TABLE]
| Method | Endpoint | Description |
| GET | /products | Retrieve a list of products with optional filters |
| POST | /products | Create a new product |
| PUT | /products/{product_id} | Update an existing product |
| DELETE | /products/{product_id} | Delete a product |
| POST | /products/bulk | Create or update multiple products in a single request |
[/TABLE]



## 3.2 GET /products

GET   /products  Retrieve a list of products


[TABLE]
| Property | Value |
| HTTP Method | GET |
| URL | https://api.octopusbridge.com/v1/products |
| Auth Required | Yes |
| Required OAuth Scope | read_products |
| Success Response | 200 OK |
[/TABLE]



### Query Parameters


[TABLE]
| Field | Type | Required | Description |
| limit | integer | No | Number of results per page. Default: 50, Max: 250. |
| page | integer | No | Page number for pagination. Default: 1. |
| since_id | string | No | Return products with ID after this value (cursor pagination). |
| title | string | No | Filter by product title (partial match supported). |
| vendor | string | No | Filter by product vendor name. |
| product_type | string | No | Filter by product type. |
[/TABLE]


Sample Request:

Request

GET https://{merchantname}:{AccessID}@octopusapi.24sevencommerce.com/admin/api/2020-01/products.json





Sample Response (200 OK):

HTTP/1.1 200 OK
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



## 3.3 POST /products

POST/admin/api/2020-01/products.json
Note:
Mandatory fields – Title and one Variant must exist in the request and Variant must have SKU, Price, Sales Price for discounted items; Sales start date and Sales end date for applying sales for a period and options for matrix products.



[TABLE]
| Property | Value |
| HTTP Method | POST |
| URL | https://api.octopusbridge.com/v1/products |
| Content-Type | application/json |
| Auth Required | Yes |
| Required OAuth Scope | write_products |
| Success Response | 201 Created |
| Idempotent | No — each call creates a new product |
[/TABLE]



### Request Fields


[TABLE]
| Field | Type | Required | Description |
| title | string | Yes | Product title (max 255 characters). |
| body_html | string | No | Product description in HTML format. |
| vendor | string | No | Vendor/brand name for the product. |
| product_type | string | No | Custom product type label. |
| status | string | No | active, draft, or archived. Default: active. |
| tags | string | No | Comma-separated tags for the product. |
| variants | array | No | Array of variant objects. A default variant is created if omitted. |
| images | array | No | Array of image objects with src URLs. |
| options | array | No | Array of option objects (e.g., Size, Color). Required if multiple variants. |
[/TABLE]


Sample Request Body:

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

Sample Response (201 Created):

HTTP/1.1 201 Created
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


[TABLE]
| Property | Value |
| HTTP Method | PUT |
| URL | https://api.octopusbridge.com/v1/products/{product_id} |
| Content-Type | application/json |
| Auth Required | Yes |
| Required OAuth Scope | write_products |
| Success Response | 200 OK |
| Partial Updates | Supported — only fields included in the body are updated |
[/TABLE]


Sample Request Body:

{
"product": {
"id": 632910392,
"title": "New product title"
}
}

Sample Response (200 OK):
Product model will return with updated title.

## 3.5 DELETE /products/{product_id}

DELETE   /products/{product_id}  Delete a product and all its variants and images


[TABLE]
| Property | Value |
| HTTP Method | DELETE |
| URL | https://api.octopusbridge.com/v1/products/{product_id} |
| Auth Required | Yes |
| Required OAuth Scope | write_products |
| Success Response | 200 OK |
| Reversible | No — deletion is permanent |
[/TABLE]


CAUTION: Deleting a product permanently removes all associated variants, images, and inventory records. This action cannot be undone.

Sample Request:

DELETE /admin/api/2020-01/products/632910392.json
Sample Response (200 OK):


## HTTP/1.1 200 OK


## {


## }



## 3.6 Bulk POST /products

POST   /products/bulk  Create or update multiple products in one request

The bulk endpoint accepts an array of product objects and processes them in a single transaction. Use this for high-volume catalog synchronization. Products with an existing id field are updated; those without are created.
POSTadmin/api/2020-01/BulkProduct/bulkpost.json
Note:
Mandatory fields – Title and one Variant must exist in the request and Variant must have SKU, Price, Sales Price for discounted items; Sales start date and Sales end date for applying sales for a period and options for matrix products. We have introduced a new attribute "SV_Temp_ProductId". You can use this attribute to send your internal product ID. Once you receive a Success response from the request, you need to map the "SV_Temp_ProductId" with the "productId" you will receive in response.




[TABLE]
| Property | Value |
| HTTP Method | POST |
| URL | https://api.octopusbridge.com/v1/products/bulk |
| Content-Type | application/json |
| Auth Required | Yes |
| Required OAuth Scope | write_products |
| Max Products per Request | 250 |
| Success Response | 200 OK with per-item results |
[/TABLE]


Given below is the cURL request to POST products in bulk:

curl --location 'http://<Merchant Name>:<Access ID>@shopifyapi.24sevencommerce.com/admin/api/2020-01/BulkProduct/bulkpost.json' \
--header 'X-Octopus-Access-Token: <Access ID> \
--header 'Content-Type: application/json' \
--data '{
"entity_type": "Products",
"entity_count": 2,
"created_at": "2024-04-24T05:45:04-08:00",
"items": [
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
]
}'

Sample Response (200 OK):

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


# 4. Images


## 4.1 Overview

Product images are managed as sub-resources of the Product object. Each image is associated with a product and can optionally be assigned to specific variants. Images are served via CDN and must be provided as publicly accessible URLs during creation.


[TABLE]
| Method | Endpoint | Description |
| POST | /products/{product_id}/images | Add a new image to a product |
| PUT | /products/{product_id}/images/{image_id} | Update an existing product image |
| DELETE | /products/{product_id}/images/{image_id} | Delete a product image |
[/TABLE]

Note:
Image file extensions supported - .jpg, .jpeg, .png
Image file size maximum – 5MB or less.
Image file dimension maximum – 1000x1000 or less
Image file name length – 100 characters
The images need to be base64 encoded before sending the POST request.
The image file name must be unique to the image data – in that two different images cannot share the same image name
The image filename cannot support special characters or spaces in the filename

In case you want to remove the existing images of a product and add new ones, please follow the following steps:
Send an Image delete request for the products.
Once the images are deleted, send the POST request. Do not change the image position number, when you are sending POST just after the delete request.

It is to be noted that there should be a time difference of at least 10 seconds between the two requests.


## 4.2 POST /products/{product_id}/images

POST   /products/{product_id}/images  Add an image to a product


[TABLE]
| Property | Value |
| HTTP Method | POST |
| URL | https://api.octopusbridge.com/v1/products/{product_id}/images |
| Content-Type | application/json |
| Auth Required | Yes |
| Required OAuth Scope | write_products |
| Success Response | 201 Created |
[/TABLE]



### Request Fields


[TABLE]
| Field | Type | Required | Description |
| src | string | Yes | Publicly accessible URL of the image. Must be HTTPS. |
| position | integer | No | Display order position. Default: appended to end. |
| alt | string | No | Alt text for accessibility and SEO. |
| variant_ids | array | No | Array of variant IDs to associate this image with. |
[/TABLE]


Sample Request Body:

{
"image": {
"position": "1",
"attachment": "/9j/4AAQSkZJRgABAQEAYABgAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAJXAa0DASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD3+iiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKiuLiK0t3nncJGgyzHtQCVyWmPLHH9+RV/3jivMdZ8d6hql0bLREaKNm2rIBl3+npTIvAmt3y+ffXypIwziVjI2ff0/Og61hVFXqysepKyuMqwI9QadXj0tr4j8GXAufMzb7h+8jJMZ9mH9cZ+tek+Htet9e08Tx/JKvyyxk5KN/h70EVaHKuaLujYooooOcKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigA7V5j481uXUNRTQ7Isyqw80IeWbsP8+/pXfa1qC6XpFzdnGY0O0Hu3QD8yK4b4f6Q17cza5dguWc+UW7k9W/z3zQdmGShF1pdNvU6Dwr4Uh0aBZZVV7xh8zdk9h/jXThBjpSgYFLQc05ynLmkQXFrFcQPFKivG4wysMgivNmhl8DeKklQsdNuTt69Fz0PupP5H2r1CsTxRo66xos0AXMqjfF/vDt+IyPxoNKFTllyy2ZsxusiK6nIIyCKdXJeAtXa+0f7JMxM9qdhz1I7GutoM6kHCTiwooooICiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiijtQBwfxHu2eCy0mHl7mT5lHcdMfqT+FddpFgmm6Zb2qAYjQAkdz3P4muEVhr3xQz96Gyz+G3gf8Aj27869IHAoOqv7lONP5/eLRRRQcoUhGRilooA85X/inPiGyj5be+G4fUn/HP4CvRRyM1xPxFsWNjbanGvz2smWI/un/P610uhXw1HSIJ8gsVw31oOut79ONT5M0qKKKDkCiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACquo3S2Om3N0/3YY2c/gM1arlfiFd/Z/CVxGDhrh0hH4n/AGgunHmkkYnwxt2mOoajJy7uEBP0y36mvRa5T4eW3k+E4JcYNw7y/ma6ug1xUr1mFFFFBzhRRRQBS1eyGoaVcWpAPmIQM+vb9a4/4d3zLFPpspIeFsAN144/lg13h5GK81uP+Kf8AiK7D5YbrEv1zwf5/pQdeH9+Eqb9Uel0UinIB9aWg5AooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigArzP4r3pH9n2SH5vnmI+gwv616ZXjPjKY6v8RBaKciMxQL+LAn/ANmoOrBxTrK/Q9U0C1FnoNjbgY2QqMfhWlTUUKiqBgAYp1BzyfNJsKKKKCQooooAK4D4j2pjbTtSQYMcvlsfY9P6139c/wCNLH7f4WvYwMuieYp9CP8A62aDfDT5KqZc8P3gvtGt5c5bbtb6itSuG+Hmoie0kgJ6gSKD79a7mgMTT5KriFFFFBgFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAjHCknsK8S8NN/bXxH+1dVku5JwfZQf/ihXq/ie9/s7wzqFznBWFgp9CeB+pFea/Ca1MutTXLDIjtyw9i7f4KKDtwq5YTn5HsNFFFBxBRRRQAUUUUAFRzxLNBJE/wB11Kn6GpKKAPI/CVw2leIfsshwY52gYe2eP5j8q9bryHxNCdM8b3ez5VmVLhSfXof1r1XTbkXmnQXA/wCWiA0HoY5c0YVV1RaooooPPCiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooA4L4s3/2bwotup+a5mC49QMn+YFQ/Ciz8rTL65/vyrGP+AKAf1zWJ8WrsXGt6XpwbhF3sP94//Y/rXb+ALX7P4Ps2Iw84aZvqxJ/woO5e5hH5s6eiiig4QooooAKKKKACiiigDzf4m2vl32lX6r1LQMfryP1re8B332nQ/JZgWhbHHoef8aT4iWRu/CFy6DMlsVnUe6n/AAzXM+AdREWrmHf+7uE+UZ79R/Wg9WC9rgmusT1Giiig8oKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiio5pFhgeRztVFLMfQCgDwTxpdf2j441GRWz5LtABj7pVABz7sT/AJxn3LSbf7JpNpbgY8uFV/ICvn3RA+s+KFL5P2q9DMOuCz7m/Ra+jlGFA9BQd2J92jCHqLRRRQcIUUUUAFFFFABRRRQBW1C2F5p9xbN0ljZPzGK8U0Fls2V3fy7mxlwuc/PtbBX8ufwr3M8ivEtft/7N8XarAvCtIJ1GOzDmg9TLfecqXc9qhkWWFJFOVYAg1JWF4RvPtnh22JOWjHltz6f/AFsVu0HnVIck3HsFFFFBAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAVz3jm9+weDNTmDYYwmMH3Y7f610NeefGC88jwrBbA8z3Kgj2AJ/nigumrySOG+GNt9o8T2bEZAd5D/wFcD/ANCr3yvHfhBabtRknxxHbcexdv8A7GvYqDqxz/eKPZIKKKKDiCiiigAooooAKKKKACvKfiRa+R4ms7kDC3Fu0ZP+0pz/ACNerVwnxQtd2k2V6OttcjcfRWG0/wBKDswM+SvFkfw3vflurMn0dR+h/pXf1494NvPsXiWAHhZSYyPTPQfnivYOtBrmdPkrt9xaKKKDzgooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigArxv403u6/02yB/1cTykf7xwP8A0E17JXz58S7o3/j25jBysPlwr+QJ/Umg6MLHmqI774TWnlaZeT4+8yRj8FB/mxr0WuT+HVuIfCkbgf62aR//AB4gfoK6ygeLlzV5MKKKKDmCiiigAooooAKKKKACsHxnZfb/AAjqUAGW8ksv1X5h/Kt6o541lgeNhlWUgj2oKg+WSZ4JaXJSSC5Q4b5XBxjnrXvFlcLdWUM6HKyIGH4ivAI4zArQN96CR4j68EivYvA959r8NQAnLRExn8Dx+hFB7maw5qUKiOkooooPBCiiigAooooAKKKKACii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iiigDlfHPhn/AISHSAYcC7t8tET39RXh80UttM0E6GOZDhkbtX01XH+K/A1rryGaELHcjoemaDuwmMdH3XseJinYq7q3hvVtFmZZrdyoP3scfmKyRcSD70R+gPP9KZ7dLFUqnwstZp26qn2od1b8s0faR2R/yoOjmi+pZzS7qp/aDnmM/wDfSj+tH2tR2A+rr/jQHtIrqXd9JvFUTep6p+Mi/wCNN+2J/ej/AO/i0C9tDuXy1G6qH25P76f99j/Gk+3J/wA9Iv8Avr/61Ae3p/zI0waN1Zwv0/56xf8AfR/wpwvk/wCesP8A32f8KBe3pfzL7y/ml3CqIvFPSSI/9tBSi5B6NH/38Wgr20O5ezSg1T8//d/CRf8AGlFwf7v/AI+v+NIFVh3Lgp2aqC4P9wf99r/jQZ39Yh9ZB/TNA/aw7lvNLkY61S+0EHmW3/7+/wD1qQ3aj/lvb/8AfZ/woJdan3RdzS7qzzer/wA94P8Avs/4Un25P+esP/fTf4UC9vT/AJkaYanA1mLfDOA8R/4Ef8Kl+1MBkSRnpgKpNAvrFL+ZGgDS5GDk4qtbrJcPje6g+igf416D4U8J6bdMs1zDJcMpziRjtH4UHNUzGhDZ3KXg3wxJrF/He3EZFhC24bhxK3bHsK9cAAGBTIokhjWONQqqMAKMAVJQeFicTKvPmYUUUUHOFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUARzW8U6lZY1dT2IrGufB2hXZJlsI8n04rdooA5GT4a+GZDk2bD6NUR+F3hg/8usn/AH2P8K7Oigd2cZ/wq3wx/wA+0v8A32P8KX/hV/hj/n2k/wC+x/hXZUUBdnG/8Kv8Mf8APrJ/33/9aj/hWHhj/n2k/wC+x/hXZUUCucePhl4ZH/Lq/wD33/8AWpR8NPDI/wCXR/8Avr/61dfRQByX/CtvDX/Po3/fX/1qP+Fb+Gv+fNv++v8A61dbRQByX/Ct/DX/AD5n/vr/AOtR/wAK38Nf8+bf99f/AFq62igLnI/8K18Nf8+jf99f/WpD8M/DJ/5dX/77/wDrV19FA7s47/hWPhn/AJ9pf++//rUf8Kx8Nf8APvL/AN9//WrsaKAuzjv+FY+Gv+feX/vsf4Un/CsPDX/PCb/vsf4V2VFArnGf8Kv8Nf8APGf/AL7H+FIfhb4b/wCedx/32P8ACu0ooA4r/hVnhwdFuR/20X/4mnr8M/D69Bc/i6//ABNdlRQBzVt4F0S1YFYZGx/fb/AV0FvbQ2sYjgjVFHYCpaKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigD//2Q==",
"filename": "s4630.jpg",
"metafields": [
{
"namespace": "tags",
"key": "alt",
"value": "Test tag",
"value_type": "string"
}
]
}
}

Sample Response (201 Created):

HTTP/1.1 200 OK
{
"image": {
"id": 14102836772957,
"product_id": 4430053933149,
"position": 1,
"created_at": "2019-12-05T11:27:15-05:00",
"updated_at": "2019-12-05T11:27:15-05:00",
"alt": "Test tag",
"width": 429,
"height": 599,
"src": "https:\/\/demo.com\/s\/files\/1\/0283\/7417\/1741\/products\/s4630.jpg?v=1575563235",
"variant_ids": [
],
"admin_graphql_api_id": "gid:\/\/shopify\/ProductImage\/14102836772957"
}
}


## 4.3 PUT /products/{product_id}/images/{image_id}

PUT   /products/{product_id}/images/{image_id}  Update a product image

Sample Request Body:

{
"image": {
"id": 850703190,
"attachment": "/9j/4AAQSkZJRgABAQEAYABgAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAJXAa0DASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD3+iiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKiuLiK0t3nncJGgyzHtQCVyWmPLHH9+RV/3jivMdZ8d6hql0bLREaKNm2rIBl3+npTIvAmt3y+ffXypIwziVjI2ff0/Og61hVFXqysepKyuMqwI9QadXj0tr4j8GXAufMzb7h+8jJMZ9mH9cZ+tek+Htet9e08Tx/JKvyyxk5KN/h70EVaHKuaLujYooooOcKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigA7V5j481uXUNRTQ7Isyqw80IeWbsP8+/pXfa1qC6XpFzdnGY0O0Hu3QD8yK4b4f6Q17cza5dguWc+UW7k9W/z3zQdmGShF1pdNvU6Dwr4Uh0aBZZVV7xh8zdk9h/jXThBjpSgYFLQc05ynLmkQXFrFcQPFKivG4wysMgivNmhl8DeKklQsdNuTt69Fz0PupP5H2r1CsTxRo66xos0AXMqjfF/vDt+IyPxoNKFTllyy2ZsxusiK6nIIyCKdXJeAtXa+0f7JMxM9qdhz1I7GutoM6kHCTiwooooICiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiijtQBwfxHu2eCy0mHl7mT5lHcdMfqT+FddpFgmm6Zb2qAYjQAkdz3P4muEVhr3xQz96Gyz+G3gf8Aj27869IHAoOqv7lONP5/eLRRRQcoUhGRilooA85X/inPiGyj5be+G4fUn/HP4CvRRyM1xPxFsWNjbanGvz2smWI/un/P610uhXw1HSIJ8gsVw31oOut79ONT5M0qKKKDkCiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACquo3S2Om3N0/3YY2c/gM1arlfiFd/Z/CVxGDhrh0hH4n/AGgunHmkkYnwxt2mOoajJy7uEBP0y36mvRa5T4eW3k+E4JcYNw7y/ma6ug1xUr1mFFFFBzhRRRQBS1eyGoaVcWpAPmIQM+vb9a4/4d3zLFPpspIeFsAN144/lg13h5GK81uP+Kf8AiK7D5YbrEv1zwf5/pQdeH9+Eqb9Uel0UinIB9aWg5AooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigArzP4r3pH9n2SH5vnmI+gwv616ZXjPjKY6v8RBaKciMxQL+LAn/ANmoOrBxTrK/Q9U0C1FnoNjbgY2QqMfhWlTUUKiqBgAYp1BzyfNJsKKKKCQooooAK4D4j2pjbTtSQYMcvlsfY9P6139c/wCNLH7f4WvYwMuieYp9CP8A62aDfDT5KqZc8P3gvtGt5c5bbtb6itSuG+Hmoie0kgJ6gSKD79a7mgMTT5KriFFFFBgFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAjHCknsK8S8NN/bXxH+1dVku5JwfZQf/ihXq/ie9/s7wzqFznBWFgp9CeB+pFea/Ca1MutTXLDIjtyw9i7f4KKDtwq5YTn5HsNFFFBxBRRRQAUUUUAFRzxLNBJE/wB11Kn6GpKKAPI/CVw2leIfsshwY52gYe2eP5j8q9bryHxNCdM8b3ez5VmVLhSfXof1r1XTbkXmnQXA/wCWiA0HoY5c0YVV1RaooooPPCiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooA4L4s3/2bwotup+a5mC49QMn+YFQ/Ciz8rTL65/vyrGP+AKAf1zWJ8WrsXGt6XpwbhF3sP94//Y/rXb+ALX7P4Ps2Iw84aZvqxJ/woO5e5hH5s6eiiig4QooooAKKKKACiiigDzf4m2vl32lX6r1LQMfryP1re8B332nQ/JZgWhbHHoef8aT4iWRu/CFy6DMlsVnUe6n/AAzXM+AdREWrmHf+7uE+UZ79R/Wg9WC9rgmusT1Giiig8oKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiio5pFhgeRztVFLMfQCgDwTxpdf2j441GRWz5LtABj7pVABz7sT/AJxn3LSbf7JpNpbgY8uFV/ICvn3RA+s+KFL5P2q9DMOuCz7m/Ra+jlGFA9BQd2J92jCHqLRRRQcIUUUUAFFFFABRRRQBW1C2F5p9xbN0ljZPzGK8U0Fls2V3fy7mxlwuc/PtbBX8ufwr3M8ivEtft/7N8XarAvCtIJ1GOzDmg9TLfecqXc9qhkWWFJFOVYAg1JWF4RvPtnh22JOWjHltz6f/AFsVu0HnVIck3HsFFFFBAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAVz3jm9+weDNTmDYYwmMH3Y7f610NeefGC88jwrBbA8z3Kgj2AJ/nigumrySOG+GNt9o8T2bEZAd5D/wFcD/ANCr3yvHfhBabtRknxxHbcexdv8A7GvYqDqxz/eKPZIKKKKDiCiiigAooooAKKKKACvKfiRa+R4ms7kDC3Fu0ZP+0pz/ACNerVwnxQtd2k2V6OttcjcfRWG0/wBKDswM+SvFkfw3vflurMn0dR+h/pXf1494NvPsXiWAHhZSYyPTPQfnivYOtBrmdPkrt9xaKKKDzgooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigArxv403u6/02yB/1cTykf7xwP8A0E17JXz58S7o3/j25jBysPlwr+QJ/Umg6MLHmqI774TWnlaZeT4+8yRj8FB/mxr0WuT+HVuIfCkbgf62aR//AB4gfoK6ygeLlzV5MKKKKDmCiiigAooooAKKKKACsHxnZfb/AAjqUAGW8ksv1X5h/Kt6o541lgeNhlWUgj2oKg+WSZ4JaXJSSC5Q4b5XBxjnrXvFlcLdWUM6HKyIGH4ivAI4zArQN96CR4j68EivYvA959r8NQAnLRExn8Dx+hFB7maw5qUKiOkooooPBCiiigAooooAKKKKACii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iiigDlfHPhn/AISHSAYcC7t8tET39RXh80UttM0E6GOZDhkbtX01XH+K/A1rryGaELHcjoemaDuwmMdH3XseJinYq7q3hvVtFmZZrdyoP3scfmKyRcSD70R+gPP9KZ7dLFUqnwstZp26qn2od1b8s0faR2R/yoOjmi+pZzS7qp/aDnmM/wDfSj+tH2tR2A+rr/jQHtIrqXd9JvFUTep6p+Mi/wCNN+2J/ej/AO/i0C9tDuXy1G6qH25P76f99j/Gk+3J/wA9Iv8Avr/61Ae3p/zI0waN1Zwv0/56xf8AfR/wpwvk/wCesP8A32f8KBe3pfzL7y/ml3CqIvFPSSI/9tBSi5B6NH/38Wgr20O5ezSg1T8//d/CRf8AGlFwf7v/AI+v+NIFVh3Lgp2aqC4P9wf99r/jQZ39Yh9ZB/TNA/aw7lvNLkY61S+0EHmW3/7+/wD1qQ3aj/lvb/8AfZ/woJdan3RdzS7qzzer/wA94P8Avs/4Un25P+esP/fTf4UC9vT/AJkaYanA1mLfDOA8R/4Ef8Kl+1MBkSRnpgKpNAvrFL+ZGgDS5GDk4qtbrJcPje6g+igf416D4U8J6bdMs1zDJcMpziRjtH4UHNUzGhDZ3KXg3wxJrF/He3EZFhC24bhxK3bHsK9cAAGBTIokhjWONQqqMAKMAVJQeFicTKvPmYUUUUHOFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUARzW8U6lZY1dT2IrGufB2hXZJlsI8n04rdooA5GT4a+GZDk2bD6NUR+F3hg/8usn/AH2P8K7Oigd2cZ/wq3wx/wA+0v8A32P8KX/hV/hj/n2k/wC+x/hXZUUBdnG/8Kv8Mf8APrJ/33/9aj/hWHhj/n2k/wC+x/hXZUUCucePhl4ZH/Lq/wD33/8AWpR8NPDI/wCXR/8Avr/61dfRQByX/CtvDX/Po3/fX/1qP+Fb+Gv+fNv++v8A61dbRQByX/Ct/DX/AD5n/vr/AOtR/wAK38Nf8+bf99f/AFq62igLnI/8K18Nf8+jf99f/WpD8M/DJ/5dX/77/wDrV19FA7s47/hWPhn/AJ9pf++//rUf8Kx8Nf8APvL/AN9//WrsaKAuzjv+FY+Gv+feX/vsf4Un/CsPDX/PCb/vsf4V2VFArnGf8Kv8Nf8APGf/AL7H+FIfhb4b/wCedx/32P8ACu0ooA4r/hVnhwdFuR/20X/4mnr8M/D69Bc/i6//ABNdlRQBzVt4F0S1YFYZGx/fb/AV0FvbQ2sYjgjVFHYCpaKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigD//2Q==",
"filename": "ipod-nano.png ",
}
}


Sample Response (200 OK):

HTTP/1.1 200 OK
{
"image": {
"id": 850703190,
"product_id": 632910392,
"position": 1,
"created_at": "2020-05-22T14:26:11-04:00",
"updated_at": "2020-05-22T14:26:11-04:00",
"alt": null,
"width": 123,
"height": 456,
"src": "https://demo.com/s/files/1/0006/9093/3842/products/ipod-nano.png",
"admin_graphql_api_id": "gid://shopify/ProductImage/850703190"
}
}


## 4.4 DELETE /products/{product_id}/images/{image_id}

DELETE   /products/{product_id}/images/{image_id}  Delete a product image

Sample Request:

DELETE /admin/api/2020-01/products/{Product_id}/images/{image_id}.json

Sample Response (200 OK):

HTTP/1.1 200 OK
{
}

# 5. Variants


## 5.1 Overview

A variant can be added to a Product resource to represent one version of a product with several options. The Product resource will have a variant for every possible combination of its options.
The Octopus Rest API lets you do the following with the Product variants resource.
GET /admin/api/2020-01/variants/{variant_id}.json
Retrieve a single Product Variant by ID
GET/admin/api/2020-01/Variants.json?sku={SKU_id)
Retrieve a Product Variant by SKU
GET/admin/api/2020-01/products/{product_id}/Variants.json
Retrieve all variants of a Product
admin/api/2020-01/products/{product_id}/Variants/count.json
Retrieve count of variants of a Product
PUT /admin/api/2020-01/variants/{variant_id}.json
Modify an existing Product Variant
POST /admin/api/2020-01/products/{variant_id}/variants.json
Create a new Product Variant
DELETE /admin/api/2020-01/products/{product_id}/variants/{variant_id}.json
Delete any existing variant of a products.

Note: We have added a custom_attributes node in the variations endpoint. This node is an array type. You can add upto 20 unique custom attributes per merchant account. The data type of this node is string. You can park any information there. You can send the custom_attribute as:

"custom_attributes": [{
"attribute_name": "Test Attribute",
"attribute_value": "Test Value"
}]



If the custom_attribute node is sent like below, it will delete all the custom attributes of the variant.

"custom_attributes": []

If you do not send custom_attribute node at the time of product updates, the attributes will remain as it is.

The attribute names should be unique and same for all the products since they are global in nature and are used for mapping for all products. The values of these attributes can be product specific.


[TABLE]
| Method | Endpoint | Description |
| GET | /products/{product_id}/variants | List all variants for a product |
| POST | /products/{product_id}/variants | Add a new variant to a product |
| PUT | /variants/{variant_id} | Update an existing variant |
| DELETE | /variants/{variant_id} | Delete a variant |
[/TABLE]



## 5.2 GET /products/{product_id}/variants

GET   /products/{product_id}/variants  List all variants for a product

Sample Request:

GET /admin/api/2020-01/variants/13120.json

Sample Response (200 OK):

HTTP/1.1 200 OK
{
"variant": {
"id": 13120,
"product_id": 84630,
"title": null,
"price": 27.9900,
"PriceA": "",
"PriceB": "",
"PriceC": "",
"ListPrice": "",
"MSRP": "",
"sku": "5116",
"position": null,
"inventory_policy": "deny",
"fulfillment_service": null,
"inventory_management": "octopus",
"option1": "Default Title",
"option2": null,
"option3": null,
"created_at": "2020-04-18T00:26:40-00:00",
"updated_at": "2020-05-23T03:44:06-00:00",
"taxable": true,
"barcode": "",
"grams": null,
"image_id": null,
"weight": "0",
"weight_unit": "",
"cost_price": "",
"sales_price": "",
"salestartdate": "",
"saleenddate": "",
"inventory_item_id": 13120,
"inventory_quantity": 0,
"old_inventory_quantity": 0,
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

}
}


## 5.3 POST /products/{product_id}/variants

POST   POST /admin/api/2020-01/products/{Product_ID}/variants.json

Mandatory Fields: Variant must have SKU, Price, Sales Price for discounted items, Sales start date and Sales end date for applying sales for a period and options for matrix products.


### Request Fields


[TABLE]
| Field | Type | Required | Description |
| option1 | string | Yes | Value for the first product option (e.g., size value). |
| option2 | string | No | Value for the second product option (e.g., color value). |
| option3 | string | No | Value for the third product option. |
| sku | string | No | Stock Keeping Unit identifier. |
| price | string | Yes | Variant price as a decimal string (e.g., "29.99"). |
| compare_at_price | string | No | Original price for display as strikethrough. |
| inventory_quantity | integer | No | Starting inventory count. Default: 0. |
| inventory_management | string | No | shopify or null. Controls inventory tracking. |
| inventory_policy | string | No | deny or continue. Behavior when out of stock. |
| requires_shipping | boolean | No | Whether this variant requires shipping. Default: true. |
| taxable | boolean | No | Whether this variant is taxable. Default: true. |
| weight | number | No | Variant weight for shipping calculations. |
| weight_unit | string | No | Unit of weight: kg, g, lb, oz. |
[/TABLE]



Sample Request Body:

{
"variant": {
"option1": "26-33",
"option2": "Dark Wash",
"option3": "",
"barcode": "",
"price": "85",
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
"sku": "45689",
"inventory_management": "octopus",
"inventory_policy": "deny",
"weight": "0",
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

}
}

Sample Response (201 Created):

HTTP/1.1 201 Created
{
"variant": {
"id": 90494,
"product_id": 13120,
"title": null,
"price": 85,
"PriceA": "",
"PriceB": "",
"PriceC": "",
"ListPrice": "",
"MSRP": "",
"sku": "45689",
"position": null,
"inventory_policy": "deny",
"fulfillment_service": null,
"inventory_management": "octopus",
"option1": "26-33",
"option2": "Dark Wash",
"option3": "",
"created_at": "2020-06-25T06:30:55-00:00",
"updated_at": "2020-06-25T06:30:55-00:00",
"taxable": true,
"barcode": "",
"grams": null,
"image_id": null,
"weight": "0",
"weight_unit": "kg",
"cost_price": "",
"sales_price": "",
"salestartdate": "",
"saleenddate": "",
"inventory_item_id": 90494,
"inventory_quantity": 0,
"old_inventory_quantity": 0,
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

}
}


## 5.4 PUT /variants/{variant_id}

PUT /admin/api/2020-01/variants/13120.json
Sample Request Body:

{
"variant": {
"id": 13120,
"option1": "Not Pink",
"price": "99.00"
}
}

Sample Response (200 OK):

HTTP/1.1 200 OK
{
"variant": {
"id": 13120,
"product_id": 84630,
"title": null,
"price": 99.00,
"PriceA": ""
"PriceB": ""
"PriceC": ""
"ListPrice":""
"MSRP": ""
"sku": "5116",
"position": null,
"inventory_policy": "deny",
"fulfillment_service": null,
"inventory_management": “octopus”,
"option1": "Not Pink",
"option2": null,
"option3": null,
"created_at": "2020-04-18T00:26:40-00:00",
"updated_at": "2020-06-25T06:36:45-00:00",
"taxable": true,
"barcode": "",
"grams": null,
"image_id": null,
"cost_price": "",
"sales_price": "",
"salestartdate":"",
"saleenddate":"",
"weight": "0",
"weight_unit": "",
"inventory_item_id": 13120,
"inventory_quantity": 0,
"old_inventory_quantity": 0,
"requires_shipping": null,
"admin_graphql_api_id": null
"custom_attributes": [
{
"attribute_name": "Test Attribute",
"attribute_value": "Test Value"
},

{
"attribute_name": "Test Attribute2",
"attribute_value": "Test Value2"
}
]

}
}


## 5.5 DELETE /variants/{variant_id}

DELETE /admin/api/2020-01/ products/10000/variants/20000.json
WARNING: A product must have at least one variant. Attempting to delete the last variant on a product will return a 422 error. Delete the product instead.

Sample Response (200 OK):

HTTP/1.1 200 OK
{
}


# 6. Locations


## 6.1 Overview

Locations represent physical or virtual places where inventory is stored and orders are fulfilled (e.g., warehouses, retail stores, fulfillment centers). Locations are read-only through the API — they are configured in the shop admin.


## 6.2 GET /locations

GET /admin/api/2020-01/locations.json

[TABLE]
| Property | Value |
| HTTP Method | GET |
| URL | https://api.octopusbridge.com/v1/locations |
| Auth Required | Yes |
| Required OAuth Scope | read_inventory |
| Success Response | 200 OK |
[/TABLE]


Sample Request:

GET /admin/api/2020-01/locations.json

Sample Response (200 OK):

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



### Location Object Fields


[TABLE]
| Field | Type | Description |
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
[/TABLE]




# 7. Inventory Levels


## 7.1 Overview

An inventory level represents the available quantity of an inventory item at a specific location. Each inventory level belongs to one inventory item and has one location. For every location where an inventory item is available, there's an inventory level that represents the inventory item's quantity at that location.


[TABLE]
| Method | Endpoint | Description |
| GET | /inventory_levels | Get inventory levels for variants at locations |
| POST | /inventory_levels/set | Set the inventory level for a variant at a location |
| POST | /inventory_levels/bulk | Set inventory levels for multiple variant/location pairs |
[/TABLE]



## 7.2 GET /inventory_levels

GET /admin/api/2020-01/inventory_levels.json?inventory_item_ids={Item_Id}&location_ids={Location_Id}

### Query Parameters


[TABLE]
| Field | Type | Required | Description |
| inventory_item_ids | string | Yes* | Comma-separated list of inventory item IDs. *Required if location_ids not provided. |
| location_ids | string | Yes* | Comma-separated list of location IDs. *Required if inventory_item_ids not provided. |
| limit | integer | No | Number of results per page. Default: 50, Max: 250. |
[/TABLE]


Sample Request:

GET /admin/api/2020-01/inventory_levels.json?inventory_item_ids={Item_Id}&location_ids={Location_Id}
Sample Response (200 OK):

HTTP/1.1 200 OK
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


## 7.3 POST /inventory_levels/set

POST   /inventory_levels/set  Set the inventory quantity for a variant at a location

Mandatory fields: location_id, inventory_item_id, available


[TABLE]
| Property | Value |
| HTTP Method | POST |
| URL | https://api.octopusbridge.com/v1/inventory_levels/set |
| Content-Type | application/json |
| Auth Required | Yes |
| Required OAuth Scope | write_inventory |
| Success Response | 200 OK |
[/TABLE]


Sample Request Body:

{
"location_id": "1000",
"inventory_item_id": "13000",
"available": "17"
}

Sample Response (200 OK):
HTTP/1.1 200 OK
{
"inventory_level": {
"inventory_item_id": 13000,
"location_id": 1000,
"available": 17,
"updated_at": "2020-06-24T14:15:20-00:00",
"admin_graphql_api_id": ""
}
}


## 7.4 Bulk POST /inventory_levels

The bulk inventory_levels POST endpoint is used to POST inventory levels in bulk in a single request.

[TABLE]
| Property | Value |
| HTTP Method | POST |
| URL | https://api.octopusbridge.com/v1/inventory_levels/bulk |
| Content-Type | application/json |
| Auth Required | Yes |
| Required OAuth Scope | write_inventory |
| Max Items per Request | 250 |
| Success Response | 200 OK |
[/TABLE]

Note:
We have introduced a new attribute "sv_temp_id". You can use this attribute to send your internal ID.

Given below is the cURL request to POST inventory levels in bulk:

curl --location --request POST 'http://<Merchant Name>:<Access ID>@octopusapi.24sevencommerce.com/admin/api/2020-01/bulkinventory_levels/bulkset.json' \
--header 'X-Octopus-Access-Token: 704A865F-EE2B-4F8B-A290-A8AD3B684F75' \
--header 'Content-Type: application/json' \
--data-raw '{
"entity_type": "Inventory_Levels",
"entity_count": 2,
"created_at": "2023-03-07T08:45:04-05:00",
"items": [
{
"sv_temp_id": 100,
"location_id": 1000,
"inventory_item_id": 13000,
"available": 4
},
{
"sv_temp_id": 100,
"location_id": 1001,
"inventory_item_id": 13000,
"available": 5
}
]
}
'



# 8. Custom Collections


## 8.1 Overview

A custom collection is a grouping of products that a merchant can create to make their store easier to browse. The merchant creates a custom collection (Category) and then selects the products that will go into it.


[TABLE]
| Method | Endpoint | Description |
| GET | /custom_collections | List all custom collections |
| POST | /custom_collections | Create a new custom collection |
| PUT | /custom_collections/{id} | Update an existing custom collection |
| DELETE | /custom_collections/{id} | Delete a custom collection |
| POST | /custom_collections/bulk | Create or update multiple collections |
[/TABLE]



## 8.2 GET /custom_collections

GET   /custom_collections  Retrieve a list of custom collections


### Query Parameters


[TABLE]
| Field | Type | Required | Description |
| limit | integer | No | Number of results per page. Default: 50, Max: 250. |
| page | integer | No | Page number. Default: 1. |
| since_id | string | No | Return collections with ID after this value. |
| title | string | No | Filter by collection title. |
| product_id | string | No | Filter to collections containing this product ID. |
| fields | string | No | Comma-separated list of fields to return. |
[/TABLE]


Request:
GET /admin/api/2020-01/custom_collections.json
Sample Response (200 OK):

HTTP/1.1 200 OK
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


GET a specific collection by its ID

Request

GET /admin/api/2020-01/custom_collections/{Custom_Collection_ID}.json

Response

HTTP/1.1 200 OK
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

Count all custom collections

Request

GET /admin/api/2020-01/custom_collections/count.json

Response

HTTP/1.1 200 OK
{
"count": 2
}



## 8.3 POST /custom_collections

POST /admin/api/2020-01/custom_collections.json

### Request Fields


[TABLE]
| Field | Type | Required | Description |
| title | string | Yes | Collection title (max 255 characters). |
| body_html | string | No | Collection description in HTML. |
| handle | string | No | URL handle (slug). Auto-generated from title if omitted. |
| published | boolean | No | Whether the collection is visible in the storefront. Default: true. |
| sort_order | string | No | Product sort order: manual, best-selling, alpha-asc, alpha-desc, price-asc, price-desc, created, created-desc. |
| image | object | No | Collection image object with src URL. |
[/TABLE]


Sample Request Body:

{
"custom_collection": {
"body_html": "<p>footwear items</p>",
"handle": "sale-items-footwear",
"title": "SALE ITEMS > FOOTWEAR"
}
}



Sample Response (201 Created):

HTTP/1.1 200 OK
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



## 8.4 PUT /custom_collections/{collection_id}

PUT   /admin/api/2020-01/custom_collections/{Custom_Collection_ID}.json
Sample Request Body:

{
"custom_collection": {
"id": 1000,
"body_html": "<p>footwear items</p>",
"handle": "sale-items-footwear",
"title": "SALE ITEMS > FOOTWEAR"
}
}



Sample Response (200 OK):

HTTP/1.1 200 OK
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






## 8.5 DELETE /custom_collections/{collection_id}

DELETE /admin/api/2020-01/custom_collections/{Custom_Collection_ID}.json

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



[TABLE]
| Property | Value |
| Max Collections per Request | 250 |
| Required OAuth Scope | write_collections |
| Success Response | 200 OK with per-item results |
[/TABLE]


Given below is the cURL request to POST custom collections in bulk:

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


# 9. Collects


## 9.1 Overview

The Collect resource connects a product to a custom collection. Collects are meant for managing the relationship between products and custom collections. For every product in a custom collection there is a collect that tracks the ID of both the product and the custom collection.

Note: First you need to send updates to all custom collections if there are many.
Once all calls to custom collections are done then you need to send the collects call to all products related to those affected collections.


[TABLE]
| Method | Endpoint | Description |
| POST | /collects | Add a product to a custom collection |
| GET | /collects | List all collect associations |
| DELETE | /collects/{collect_id} | Remove a product from a collection |
| POST | /collects/bulk | Add multiple products to collections in one request |
[/TABLE]



## 9.2 POST /collects

POST /admin/api/2020-01/collects.json

Note:
Mandatory fields - Product_id, Collection_id
This call creates a new link between an existing product and an existing collection

[TABLE]
| Property | Value |
| HTTP Method | POST |
| URL | https://api.octopusbridge.com/v1/collects |
| Content-Type | application/json |
| Auth Required | Yes |
| Required OAuth Scope | write_collections |
| Success Response | 201 Created |
[/TABLE]


Sample Request Body:

{
"collect": {
"product_id": "10001",
"collection_id": "1001"
}
}

Sample Response (201 Created):

HTTP/1.1 201 Created
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


## 9.3 GET /collects

GET /admin/api/2020-01/collects/{collect_id}.json

### Query Parameters


[TABLE]
| Field | Type | Required | Description |
| collection_id | string | No | Filter by collection ID — returns all products in this collection. |
| product_id | string | No | Filter by product ID — returns all collections containing this product. |
| limit | integer | No | Number of results per page. Default: 50, Max: 250. |
| page | integer | No | Page number. Default: 1. |
[/TABLE]


Sample Request:

GET /admin/api/2020-01/collects/{collect_id}.json
Sample Response (200 OK):

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

DELETE /admin/api/2020-01/collects/1001.json
Sample Request:

DELETE /admin/api/2020-01/collects/1001.json



Sample Response (200 OK):

HTTP/1.1 200 OK
{
}

## 9.5 Bulk POST /collects

The bulk collects POST endpoint is used to create a link between existing products and collections.

POST/admin/api/2020-01/bulkcollects.json

Note:
We have introduced a new attribute "sv_temp_id". You can use this attribute to send your internal ID.


[TABLE]
| Property | Value |
| Max Items per Request | 250 |
| Required OAuth Scope | write_collections |
| Success Response | 200 OK with per-item results |
[/TABLE]


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



# 10. Orders


## 10.1 Overview

The Orders resource provides full CRUD support for managing orders in the connected shop. The GET endpoints allow partners to retrieve order lists and individual order details. POST, PUT, and DELETE enable programmatic order creation, editing, and removal.


[TABLE]
| Method | Endpoint | Description |
| GET | /orders | List all orders with filters |
| GET | /orders/{order_id} | Retrieve a single order by ID |
| POST | /orders | Create a new order |
| PUT | /orders/{order_id} | Update an existing order |
| DELETE | /orders/{order_id} | Delete an order (restricted) |
[/TABLE]



## 10.2 GET /orders


## An order is a customer's completed request to purchase one or more products from a shop. An order is created when a customer completes the checkout process, during which time they provide an email address or phone number, billing address and payment information.

GET   /orders  List all orders with optional filters

This endpoint implements pagination by using links that are provided in the response header. Sending the page parameter will return an error.

### Query Parameters


[TABLE]
| Field | Type | Required | Description |
| ids | Retrieve only orders specified by a comma-separated list of order IDs. | ids | Retrieve only orders specified by a comma-separated list of order IDs. |
| limit | The maximum number of results to show on a page. (default: 50, maximum: 250) | limit | The maximum number of results to show on a page. (default: 50, maximum: 250) |
| created_at_min | Show orders created at or after date (format: 2014-04-25T16:15:47) | created_at_min | Show orders created at or after date (format: 2014-04-25T16:15:47) |
| created_at_max | Show orders created at or before date (format: 2014-04-25T16:15:47) | created_at_max | Show orders created at or before date (format: 2014-04-25T16:15:47) |
| updated_at_min | Show orders last updated at or after date (format: 2014-04-25T16:15:47) | updated_at_min | Show orders last updated at or after date (format: 2014-04-25T16:15:47) |
| updated_at_max | Show orders last updated at or before date (format: 2014-04-25T16:15:47) | updated_at_max | Show orders last updated at or before date (format: 2014-04-25T16:15:47) |
| since_id | Show orders on or after the specified ID | since_id | Show orders on or after the specified ID |
| location_id | Get orders of a specific fulfillment location | location_id | Get orders of a specific fulfillment location |
| financial_status | Get orders of a specific finacial_status e.g. paid, refunded, pending etc. | financial_status | Get orders of a specific finacial_status e.g. paid, refunded, pending etc. |
[/TABLE]


Sample Request:

GET /admin/api/2020-01/orders.json
Sample Response (200 OK):

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
Note:
Rate: Depending on a given point of sale system, we send tax rate as it is received in the order. In some POS, the order does not download to POS due to mismatch such as Lightspeed. You can handle it as you see fit.

Location_ID: In case of some shopping carts/marketplaces like Woocommerce and Amazon, we do not receive any location_id in the fulfillments node. The location_id can not be left blank as it is mandatory. Therefore, in this instance we pass "location_id": 0.
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

GET /admin/api/2020-01/orders.json?since_id=2

Response:

This end point will return a list of orders generated after since id. The model of sales order is represented in the above request.

Response

HTTP/1.1 200 OK

Retrieves an order count

Request:

Get /admin/api/2020-01/orders/count.json

Response:

Copy
HTTP/1.1 200 OK
{
"count": 620
}










## Order Object Schema


## The following table defines every field in the Order object. Fields marked as System-set are automatically managed by the server and must not be included in POST or PUT request bodies.



[TABLE]
| Field | Type | Writable | Description |
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
[/TABLE]



## 4. POST /orders — Create Order


## 4.1 Endpoint Definition


## POST   /orders   Create a new order in the connected shop



[TABLE]
| Property | Value |
| HTTP Method | POST |
| URL | https://api.octopusbridge.com/v1/orders |
| Content-Type | application/json |
| Auth Required | Yes — X-API-Key / X-API-Secret or Bearer token |
| Required OAuth Scope | write_orders |
| Success Response | 201 Created |
| Idempotent | No — each call creates a new order |
[/TABLE]



## 4.2 Request Fields


## Top-Level Fields


[TABLE]
| Field | Type | Required | Description |
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
[/TABLE]



## Line Item Fields


[TABLE]
| Field | Type | Required | Description |
| variant_id | string | Yes | ID of the product variant to add. Must exist in the shop. |
| quantity | integer | Yes | Number of units to order. Must be a positive integer. |
| price | string | No | Override price per unit as decimal string. Defaults to variant price. |
| title | string | No | Override line item title. Defaults to product + variant title. |
| requires_shipping | boolean | No | Override shipping requirement. Defaults to variant setting. |
| taxable | boolean | No | Override taxable status. Defaults to variant setting. |
| discount_allocations | array | No | Array of {amount, discount_application_index} objects for line-level discounts. |
[/TABLE]



## Address Object Fields


[TABLE]
| Field | Type | Required | Description |
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
[/TABLE]



## Shipping Line Fields


[TABLE]
| Field | Type | Required | Description |
| title | string | Yes | Display name for the shipping method (e.g., Standard Shipping). |
| price | string | Yes | Shipping cost as decimal string (e.g., "8.95"). Use "0.00" for free shipping. |
| code | string | No | Internal shipping method code. |
| carrier_identifier | string | No | Carrier identifier: fedex, ups, usps, dhl. |
[/TABLE]



## 4.3 Sample Requests & Responses


## Example A — Standard Order with Customer Reference


## Request:


## POST /orders HTTP/1.1
Host: api.octopusbridge.com
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



## Example B — Paid B2B Order with Billing Address


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



## Example C — Validation Error Response


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




# PUT /orders/{order_id} — Update Order


## 5.1 Endpoint Definition

PUT   /orders/{order_id}   Update fields on an existing order


[TABLE]
| Property | Value |
| HTTP Method | PUT |
| URL | https://api.octopusbridge.com/v1/orders/{order_id} |
| Content-Type | application/json |
| Auth Required | Yes — X-API-Key / X-API-Secret or Bearer token |
| Required OAuth Scope | write_orders |
| Success Response | 200 OK |
| Idempotent | Yes — same request body produces same result |
| Partial Updates | Supported — only fields included in the body are updated |
[/TABLE]



## 5.2 Updatable Fields

The following fields may be updated via PUT. System-managed fields (id, order_number, totals, fulfillment_status, timestamps) are read-only and ignored if included in the request body.


[TABLE]
| Field | Type | Required | Description |
| email | string | No | Update the contact email address for this order. |
| phone | string | No | Update the contact phone number (E.164 format). |
| shipping_address | object | No | Update the shipping destination. Only allowed if order is unfulfilled. |
| billing_address | object | No | Update the billing address. Allowed at any order status. |
| note | string | No | Update the internal order note (max 5,000 chars). |
| tags | string | No | Replace all order tags with this new comma-separated value. |
| email_notif | boolean | No | Trigger a notification email to the customer about the update. |
[/TABLE]


WARNING:  Line items, discount codes, and shipping lines cannot be modified after order creation. To change order contents, cancel and recreate the order, or use the Refund API.


## 5.3 Sample Requests & Responses


### Example A — Update Email, Tags, and Note

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


### Example B — Update Shipping Address (before fulfillment)

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


### Example C — Attempt to Update a Cancelled Order

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


### Example D — Attempt to Update Shipping on a Fulfilled Order

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
Tag updates are a full replacement — the existing tag string is overwritten by the new value. To append tags, retrieve the current tags first.
A webhook event orders/updated is dispatched to all registered webhook subscribers on every successful update.


# 6. DELETE /orders/{order_id} — Delete Order


## 6.1 Endpoint Definition

DELETE   /orders/{order_id}   Permanently delete an order


[TABLE]
| Property | Value |
| HTTP Method | DELETE |
| URL | https://api.octopusbridge.com/v1/orders/{order_id} |
| Auth Required | Yes — X-API-Key / X-API-Secret or Bearer token |
| Required OAuth Scope | write_orders |
| Success Response | 200 OK with deleted order summary |
| Idempotent | Yes — deleting an already-deleted order returns 404 |
| Reversible | No — deletion is permanent and cannot be undone |
[/TABLE]


CAUTION:  DELETE is restricted to test/sandbox orders only. Orders that have payment transactions, fulfillments, or refunds attached must be cancelled (POST /orders/{id}/cancel) instead of deleted. Attempting to delete a live order with financial activity returns a 422 error.


## 6.2 Sample Requests & Responses


### Example A — Successful Deletion of a Test Order

Request:
DELETE /orders/ord_test_999 HTTP/1.1
Host: api.octopusbridge.com
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


### Example B — Order Not Found

Response (404 Not Found):
{
  "error": {
    "code": "RESOURCE_NOT_FOUND",
    "message": "No order found with ID ord_xxxxxx.",
    "field": "order_id",
    "status": 404
  }
}


### Example C — Order Has Financial Transactions (Cannot Delete)

Response (422 Unprocessable Entity):
{
  "error": {
    "code": "ORDER_NOT_DELETABLE",
    "message": "Order ord_1010 cannot be deleted because it has associated payment transactions.",
    "hint": "Use POST /orders/ord_1010/cancel to cancel this order instead.",
    "status": 422
  }
}


### Example D — Order Already Cancelled (Safe to Delete)

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


[TABLE]
| Condition | Allowed | Notes |
| Order has no payment transactions | YES | Zero transactions — typically a test order or cancelled before payment |
| Order has no fulfillments | YES | No items have been shipped or marked fulfilled |
| Order has no refunds | YES | No refund records exist on the order |
| Order has payment transactions | NO | Cancel instead using POST /orders/{id}/cancel |
| Order has been fulfilled | NO | Cannot delete once fulfillment has started |
| Order has refunds | NO | Cannot delete orders with existing refund records |
[/TABLE]


WARNING:  In the production environment, only orders created via the API (source_name: api) with no financial activity can be deleted. All other orders should be cancelled using the POST /orders/{id}/cancel endpoint.


## 6.4 Business Logic & Side Effects

Deletion is permanent and irreversible. There is no soft-delete or recycle bin.
If the order was associated with a customer record, the customer's orders_count is decremented by 1 after deletion.
Inventory is not automatically restocked on deletion. Use POST /orders/{id}/cancel with restock: true if inventory should be returned.
A webhook event orders/delete is dispatched to all registered webhook subscribers with the deleted order ID.
Deleted orders are excluded from all reporting and analytics data.


# 7. Error Reference for Order Endpoints

All errors follow the standard Octopus Bridge error envelope. Below is the complete reference for errors specific to the POST, PUT, and DELETE order endpoints.


[TABLE]
| HTTP Code | Status | Description |
| 201 | Created | POST — Order created successfully. |
| 200 | OK | PUT / DELETE — Order updated or deleted successfully. |
| 400 | Bad Request | Malformed JSON body. Ensure Content-Type: application/json is set. |
| 401 | Unauthorized | Missing or invalid API credentials. |
| 403 | Forbidden | API key lacks write_orders scope. |
| 404 | Not Found | PUT / DELETE — The specified order_id does not exist. |
| 422 | Unprocessable | Validation failed, order not editable, or deletion not permitted. See errors array. |
| 429 | Rate Limited | Request rate limit exceeded. Wait for Retry-After seconds. |
| 500 | Internal Error | Unexpected server error. Retry with exponential backoff; contact support if persistent. |
[/TABLE]



## 7.1 Order-Specific Error Codes


[TABLE]
| Error Code | Endpoint | Description |
| VALIDATION_ERROR | POST, PUT | One or more request fields failed validation. See errors[] array for field-level details. |
| ORDER_NOT_FOUND | PUT, DELETE | No order exists with the provided order_id. |
| ORDER_NOT_EDITABLE | PUT | Order cannot be updated — it has been cancelled or closed. |
| SHIPPING_ADDRESS_LOCKED | PUT | Shipping address cannot be changed after fulfillment has started. |
| ORDER_NOT_DELETABLE | DELETE | Order cannot be deleted due to existing transactions, fulfillments, or refunds. |
| INVALID_VARIANT | POST | One or more variant_id values in line_items do not exist in the shop. |
| INVALID_DISCOUNT_CODE | POST | One or more discount_codes do not exist or have expired. |
| INSUFFICIENT_INVENTORY | POST | Insufficient stock for one or more line items at the requested location. |
| INVALID_CURRENCY | POST | The specified currency code is not a valid ISO 4217 code. |
| INVALID_COUNTRY_CODE | POST, PUT | The country_code in an address is not a valid ISO 3166-1 alpha-2 code. |
[/TABLE]



# 11. Purchase Orders


## 11.1 Overview

The Purchase Orders resource enables creation and management of purchase orders and their associated line items within the connected shop. Purchase orders track inbound inventory from suppliers, including ordered, received, and arrival dates, as well as line-item-level pricing and receipt confirmation.


[TABLE]
| Method | Endpoint | Description |
| POST | /admin/api/2025-09/PurchaseOrder/CreateOrder.json | Create a new purchase order |
| POST | /admin/api/2025-09/PurchaseOrder/Purchaseorderline.json | Add a line item to an existing purchase order |
[/TABLE]


NOTE: Purchase Order endpoints use the /admin/api/2025-09/ base path and are versioned independently from the core /v1/ endpoints. Include your standard X-API-Key and X-API-Secret authentication headers on all requests.


## 11.2 POST /PurchaseOrder/CreateOrder.json

POST   /admin/api/2025-09/PurchaseOrder/CreateOrder.json  Create a new purchase order


[TABLE]
| Property | Value |
| HTTP Method | POST |
| URL | https://api.octopusbridge.com/admin/api/2025-09/PurchaseOrder/CreateOrder.json |
| Content-Type | application/json |
| Auth Required | Yes — X-API-Key / X-API-Secret |
| Required OAuth Scope | write_orders |
| Success Response | 200 OK |
| Idempotent | No — each call creates a new purchase order |
[/TABLE]



### Request Fields


[TABLE]
| Field | Type | Required | Description |
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
[/TABLE]


Sample Request:

POST /admin/api/2025-09/PurchaseOrder/CreateOrder.json HTTP/1.1
Host: api.octopusbridge.com
X-API-Key: your_api_key
X-API-Secret: your_api_secret
Content-Type: application/json

Request Body:

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

Response (200 OK):

{
"status":  "Success",
"message": "Purchase order created successfully.",
"orderId": 3021
}


### Response Fields


[TABLE]
| Field | Type | Description |
| status | string | Result of the operation. Success indicates the purchase order was created. |
| message | string | Human-readable confirmation message. |
| orderId | integer | The system-generated ID of the newly created purchase order. Use this ID when creating line items via POST /PurchaseOrder/Purchaseorderline.json. |
[/TABLE]



## 11.3 POST /PurchaseOrder/Purchaseorderline.json

POST   /admin/api/2025-09/PurchaseOrder/Purchaseorderline.json  Add a line item to a purchase order


[TABLE]
| Property | Value |
| HTTP Method | POST |
| URL | https://api.octopusbridge.com/admin/api/2025-09/PurchaseOrder/Purchaseorderline.json |
| Content-Type | application/json |
| Auth Required | Yes — X-API-Key / X-API-Secret |
| Required OAuth Scope | write_orders |
| Success Response | 200 OK |
[/TABLE]


NOTE: The OrderID in the request body must match a valid purchase order ID returned from POST /PurchaseOrder/CreateOrder.json. Create the purchase order header first, then add line items using the returned orderId.


### Request Fields


[TABLE]
| Field | Type | Required | Description |
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
[/TABLE]


Sample Request:

POST /admin/api/2025-09/PurchaseOrder/Purchaseorderline.json HTTP/1.1
Host: api.octopusbridge.com
X-API-Key: your_api_key
X-API-Secret: your_api_secret
Content-Type: application/json

Request Body:

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

Response (200 OK):

{
"status":  "Success",
"message": "Order line created successfully.",
"orderId": 0
}


### Response Fields


[TABLE]
| Field | Type | Description |
| status | string | Result of the operation. Success indicates the line item was created. |
| message | string | Human-readable confirmation message. |
| orderId | integer | Returns 0 for line item creation. The parent purchase order ID is not echoed here. |
[/TABLE]



### Typical Workflow

Purchase orders are created in two steps. First, create the purchase order header to obtain an orderId, then add one or more line items referencing that orderId:

// Step 1 — Create the purchase order header
POST /admin/api/2025-09/PurchaseOrder/CreateOrder.json
→ Response: { "orderId": 3021 }

// Step 2 — Add line items using the returned orderId
POST /admin/api/2025-09/PurchaseOrder/Purchaseorderline.json
Body: { "OrderID": 3021, "ItemID": "SKU-78923", ... }

// Repeat Step 2 for each additional line item on the same order


# 12. Customers


## 12.1 Overview

The Customers resource provides read access to customer records in the connected shop. Customer records include contact information, order history summaries, and address data.


## 12.2 GET /customers

GET   /customers  Retrieve a list of customers


[TABLE]
| Property | Value |
| HTTP Method | GET |
| URL | https://api.octopusbridge.com/v1/customers |
| Auth Required | Yes |
| Required OAuth Scope | read_customers |
| Success Response | 200 OK |
[/TABLE]



### Query Parameters


[TABLE]
| Field | Type | Required | Description |
| limit | integer | No | Number of results per page. Default: 50, Max: 250. |
| page | integer | No | Page number. Default: 1. |
| since_id | string | No | Return customers with ID after this value. |
| email | string | No | Filter by customer email address (exact match). |
| created_at_min | datetime | No | Return customers created at or after this datetime. |
| created_at_max | datetime | No | Return customers created at or before this datetime. |
| fields | string | No | Comma-separated list of fields to include. |
| ids | string | No | Comma-separated list of specific customer IDs. |
[/TABLE]


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


# 13. Transactions


## 13.1 Overview

Transactions represent payment events associated with an order — such as authorizations, captures, refunds, and voids. Transactions are read-only through this API; payment processing is handled by the connected payment gateway.


## 13.2 GET /orders/{order_id}/transactions

GET   /orders/{order_id}/transactions  Retrieve all transactions for a specific order


[TABLE]
| Property | Value |
| HTTP Method | GET |
| URL | https://api.octopusbridge.com/v1/orders/{order_id}/transactions |
| Auth Required | Yes |
| Required OAuth Scope | read_orders |
| Success Response | 200 OK |
[/TABLE]


Sample Request:

GET /orders/ord_1001/transactions HTTP/1.1
Host: api.octopusbridge.com
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


[TABLE]
| Field | Type | Description |
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
[/TABLE]



# 14. FAQ


## 14.1 Product Questions

Can I create a product without variants?
Yes. If you omit the variants array in a POST /products request, the API automatically creates a default variant with the product title. You can update this default variant's price and SKU via PUT /variants/{id}.
What happens to inventory when I delete a product?
Deleting a product permanently removes all associated variants, images, and inventory records. Inventory is not automatically restocked. If you need to preserve inventory history, consider setting the product status to archived instead.
How many products can I send in a Bulk POST request?
The bulk POST endpoint accepts a maximum of 250 product objects per request. For larger catalogs, paginate the requests and implement retry logic with exponential backoff for 429 rate limit responses.
Can I update variant inventory through the Products endpoint?
No. Inventory quantities must be managed through the Inventory Levels API (POST /inventory_levels/set or the bulk endpoint). The Products and Variants endpoints handle product data only.


## 14.2 Order Questions

Can I modify line items after an order is created?
No. Line items, discount codes, and shipping lines are locked after order creation. To change order contents, cancel the order and create a new one, or use the Refund API to issue credits.
Why does DELETE /orders return a 422 error?
Deletion is restricted to test or sandbox orders with no financial activity. Orders that have payment transactions, fulfillments, or refunds must be cancelled using POST /orders/{id}/cancel instead of deleted.
Does creating an order automatically decrement inventory?
Inventory is decremented when an order is created with financial_status: paid. For pending or authorized orders, inventory is reserved but not decremented until payment is captured.
How do I associate an order with an existing customer?
Include a customer object with just the id field in the POST /orders request body: { "customer": { "id": "cust_jane01" } }. The customer's orders_count and total_spent will be updated automatically.


## 14.3 General Questions

What is the rate limit for the API?
The default rate limit is 250 requests per minute per API key, shared across all endpoints. Rate limit status is returned in every response via X-RateLimit-Limit, X-RateLimit-Remaining, and X-RateLimit-Reset headers. Contact your partner manager for burst limit increases.
Are all API responses paginated?
List endpoints (GET /products, GET /orders, etc.) return paginated results. The response includes a pagination object with total, page, limit, and pages fields. Use the since_id parameter for cursor-based pagination in high-volume scenarios.
What datetime format does the API use?
All datetime fields use ISO 8601 format in UTC (e.g., 2024-07-15T11:00:00Z). When filtering with parameters like created_at_min, provide datetime values in the same format.
How do I handle webhook events?
Register webhook subscribers in the shop admin or via the Webhooks API. The following events are dispatched automatically: orders/create, orders/updated, orders/delete, products/create, products/update, products/delete, inventory_levels/update.


# 15. Mapping Considerations


## 15.1 Products

When synchronizing products from an external system (ERP, PIM, or marketplace) to Octopus Bridge, consider the following mapping rules:


[TABLE]
| External Field | Octopus Bridge Field | Notes |
| Item Number / SKU | variants[].sku | Map the external item number to the variant SKU. If the item has no variants, map to the default variant. |
| Item Name / Title | title | Use the primary product name. Variant-level names map to variant.title. |
| Description | body_html | HTML is supported. Strip unsupported tags if sourcing from plain text. |
| Category | product_type | Map the external category or item class to product_type. |
| Brand / Supplier | vendor | Map the supplier or brand name to the vendor field. |
| List Price | variants[].price | Always provided as a decimal string (e.g., "29.99"). |
| Comparable Price | variants[].compare_at_price | Used for strikethrough pricing in the storefront. |
| Stock Quantity | inventory via /inventory_levels/set | Do not pass inventory_quantity in POST /products. Use the Inventory Levels API. |
| Item Status | status | Map active items to active, discontinued to archived, draft items to draft. |
| UPC / Barcode | variants[].barcode | Store UPC or EAN barcode in the variant barcode field. |
[/TABLE]


NOTE: Inventory quantities should always be managed exclusively through the Inventory Levels API, not through the product or variant endpoints. This ensures accurate tracking across multiple locations.


## 15.2 Orders

When pushing orders from an external system (OMS, ERP, or marketplace) to Octopus Bridge, consider the following mapping rules:


[TABLE]
| External Field | Octopus Bridge Field | Notes |
| Order ID / Reference | note or tags | Store the external order reference in the note or tags field for traceability. |
| Customer Email | email | Required field. Must be a valid email format. |
| Customer Phone | phone | E.164 format required (e.g., +14155550123). |
| Line Item SKU | line_items[].variant_id | Resolve the SKU to a variant_id before submitting. The API does not accept SKUs directly. |
| Line Item Qty | line_items[].quantity | Must be a positive integer. |
| Unit Price Override | line_items[].price | Provide only if overriding the variant's default price. |
| Shipping Method | shipping_lines[].title + price | Always include at least one shipping line. Use price: "0.00" for free shipping. |
| Discount Code | discount_codes[].code | Codes must exist and be active in the shop before order creation. |
| Order Source | source_name | Set to api for programmatically created orders. |
| Payment Status | financial_status | Map paid transactions to paid, pending invoices to pending. |
| Ship-To Address | shipping_address | country_code (ISO 3166-1 alpha-2) is required. |
| Bill-To Address | billing_address | Defaults to shipping_address if omitted. |
[/TABLE]


WARNING: The variant_id is required for each line item — the API does not support SKU-based line item resolution. Maintain a SKU-to-variant_id mapping table in your integration layer and refresh it whenever products are created or updated.


# 16. Sample Code


## 16.1 Postman

A Postman collection covering all Octopus Bridge API endpoints is available from your partner integration manager. The collection includes pre-configured environments for sandbox and production, with variable placeholders for API key, secret, and base URL.


[TABLE]
| Variable | Description |
| {{base_url}} | https://api.octopusbridge.com/v1 |
| {{api_key}} | Your X-API-Key value |
| {{api_secret}} | Your X-API-Secret value |
| {{shop_id}} | Your connected shop identifier |
[/TABLE]


To authenticate requests in Postman, set the following headers on each request or configure them at the collection level under Authorization:

X-API-Key: {{api_key}}
X-API-Secret: {{api_secret}}
Content-Type: application/json


## 16.2 C#/.NET

The following C# example demonstrates authenticating and retrieving a list of products using HttpClient:

using System;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Threading.Tasks;
using Newtonsoft.Json;

public class OctopusBridgeClient
{
private readonly HttpClient _client;
private const string BaseUrl = "https://api.octopusbridge.com/v1";

public OctopusBridgeClient(string apiKey, string apiSecret)
{
_client = new HttpClient();
_client.DefaultRequestHeaders.Add("X-API-Key", apiKey);
_client.DefaultRequestHeaders.Add("X-API-Secret", apiSecret);
_client.DefaultRequestHeaders.Accept
.Add(new MediaTypeWithQualityHeaderValue("application/json"));
}

public async Task<string> GetProductsAsync(int limit = 50, int page = 1)
{
var url = $"{BaseUrl}/products?limit={limit}&page={page}";
var response = await _client.GetAsync(url);
response.EnsureSuccessStatusCode();
return await response.Content.ReadAsStringAsync();
}

public async Task<string> CreateOrderAsync(object orderPayload)
{
var json = JsonConvert.SerializeObject(new { order = orderPayload });
var content = new StringContent(json,
System.Text.Encoding.UTF8, "application/json");
var response = await _client.PostAsync($"{BaseUrl}/orders", content);
response.EnsureSuccessStatusCode();
return await response.Content.ReadAsStringAsync();
}
}

// Usage
class Program
{
static async Task Main(string[] args)
{
var client = new OctopusBridgeClient("your_api_key", "your_api_secret");

// Get products
var products = await client.GetProductsAsync(limit: 50, page: 1);
Console.WriteLine(products);

// Create an order
var order = new {
email = "customer@example.com",
financial_status = "pending",
line_items = new[] {
new { variant_id = "var_002", quantity = 1 }
},
shipping_address = new {
first_name = "John", last_name = "Smith",
address1 = "123 Main St", city = "Austin",
province_code = "TX", zip = "78701", country_code = "US"
}
};
var result = await client.CreateOrderAsync(order);
Console.WriteLine(result);
}
}

TIP: Implement a retry wrapper with exponential backoff around all API calls to handle 429 rate limit responses and transient 500 errors gracefully.

Questions about this documentation? Contact your partner integration manager.
© 2026 Octopus Bridge  |  REST API Reference  |  v1.0  |  Confidential