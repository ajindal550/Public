# Authentication

The Octopus Bridge REST API uses API Key + Secret authentication on every request. Alternatively, OAuth 2.0 Bearer tokens may be used for partner integrations.

## API Key Authentication

In order to keep transactions on Octopus Rest API safe and secure, all calls connecting with our APIs must be authenticated when making API calls.

Make Authenticated Requests
An app can make authenticated requests to the Rest API using basic authentication by using merchant name and access ID and by including its 'X-Octopus-Access-Token' access ID in the request header.

Basic Authentication

Apps can authenticate through basic HTTP authentication by using their merchant name and Access ID. Rest API can be authenticated by prepending merchant name: AccessID@ to the host name in the URL. For example:

GET https://{merchantname}:{AccessID}@octopusapi.24sevencommerce.com/admin/api/2020-01/shop.json

Note: In request header a key with name 'X-Octopus-Access-Token' with value as 'AccessID' must be passed to successful authentication.

## OAuth 2.0 Bearer Token

Partners using OAuth 2.0 may obtain a Bearer token and include it in the Authorization header:

Authorization: Bearer {access_token}

| OAuth Scope | Description |
| --- | --- |
| read_products | Read access to products, variants, images, inventory |
| write_products | Create, update, and delete products, variants, images, inventory |
| read_orders | Read access to orders and transactions |
| write_orders | Create, update, and delete orders |
| read_customers | Read access to customer records |
| read_inventory | Read access to inventory levels and locations |
| write_inventory | Create and update inventory levels |
| read_collections | Read access to custom collections and collects |
| write_collections | Create, update, and delete collections and collects |

TIP: write_* scopes implicitly grant read access. It is best practice to explicitly declare both read and write scopes for self-documenting authorization flows.

## Authentication Errors

| HTTP Code | Error | Description |
| --- | --- | --- |
| 401 | Unauthorized | Missing or invalid X-API-Key / X-API-Secret headers, or expired Bearer token. |
| 403 | Forbidden | Credentials are valid but the API key lacks the required OAuth scope for this endpoint. |
