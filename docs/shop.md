# Shop

The Shop endpoint returns configuration and metadata about the connected store. This is typically the first call made to verify connectivity and retrieve shop-level defaults such as currency, timezone, and plan information.

## 2.1 GET /shop

Request

GET: https://{merchantname}:{AccessID}@octopusapi.24sevencommerce.com/admin/api/2020-01/shop.json

Sample Response (200 OK):

```json
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
"currency": "USD",
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
```

### Shop Object Fields

| Field | Type | Description |
| --- | --- | --- |
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
