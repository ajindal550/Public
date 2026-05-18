# Variants

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

Note: We have added a custom_attributes node in the variations endpoint. This node is an array type. You can add upto 20 unique custom attributes per merchant account. The data type of this node is string. You can park any information there. You can send the custom_attribute as:

"custom_attributes": [{
"attribute_name": "Test Attribute",
"attribute_value": "Test Value"
}]

If the custom_attribute node is sent like below, it will delete all the custom attributes of the variant.

"custom_attributes": []

If you do not send custom_attribute node at the time of product updates, the attributes will remain as it is.

The attribute names should be unique and same for all the products since they are global in nature and are used for mapping for all products. The values of these attributes can be product specific.

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | /products/{product_id}/variants | List all variants for a product |
| POST | /products/{product_id}/variants | Add a new variant to a product |
| PUT | /variants/{variant_id} | Update an existing variant |
| DELETE | /variants/{variant_id} | Delete a variant |

## 5.2 GET /products/{product_id}/variants

GET   /products/{product_id}/variants  List all variants for a product

Sample Request:

GET /admin/api/2020-01/variants/13120.json

Sample Response (200 OK):

HTTP/1.1 200 OK
```json
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
```

## 5.3 POST /products/{product_id}/variants

POST   POST /admin/api/2020-01/products/{Product_ID}/variants.json

Mandatory Fields: Variant must have SKU, Price, Sales Price for discounted items, Sales start date and Sales end date for applying sales for a period and options for matrix products.

### Request Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
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

Sample Request Body:

```json
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
```

Sample Response (201 Created):

HTTP/1.1 201 Created
```json
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
```

## 5.4 PUT /variants/{variant_id}

PUT /admin/api/2020-01/variants/13120.json
Sample Request Body:

```json
{
"variant": {
"id": 13120,
"option1": "Not Pink",
"price": "99.00"
}
}
```

Sample Response (200 OK):

HTTP/1.1 200 OK
```json
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
"inventory_management": "octopus",
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
```

## 5.5 DELETE /variants/{variant_id}

DELETE /admin/api/2020-01/ products/10000/variants/20000.json
WARNING: A product must have at least one variant. Attempting to delete the last variant on a product will return a 422 error. Delete the product instead.

Sample Response (200 OK):

HTTP/1.1 200 OK
{
}
