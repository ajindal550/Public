# Quick Start

Get up and running with the Octopus Bridge API in under five minutes.

## 1. Get your credentials

Contact your Octopus Bridge account manager to receive:

- **Merchant Name** — the identifier of your store, e.g. `acme-retail`.
- **Access ID** — a long-lived secret used as the `X-Octopus-Access-Token` and in the URL for basic auth.

Keep your Access ID secret. Do **not** commit it to source control.

## 2. Verify connectivity

The fastest way to confirm your credentials work is to hit the [Shop endpoint](shop.md):

```bash
curl --location \
  "https://<merchantname>:<AccessID>@octopusapi.24sevencommerce.com/admin/api/2020-01/shop.json" \
  --header "X-Octopus-Access-Token: <AccessID>"
```

A `200 OK` response containing a `shop` array means you are live.

## 3. List your products

```bash
curl --location \
  "https://<merchantname>:<AccessID>@octopusapi.24sevencommerce.com/admin/api/2020-01/products.json" \
  --header "X-Octopus-Access-Token: <AccessID>"
```

## 4. Create a product

```bash
curl --location --request POST \
  "https://<merchantname>:<AccessID>@octopusapi.24sevencommerce.com/admin/api/2020-01/products.json" \
  --header "X-Octopus-Access-Token: <AccessID>" \
  --header "Content-Type: application/json" \
  --data '{
    "product": {
      "title": "Hello Octopus",
      "vendor": "Octopus Bridge",
      "product_type": "Demo",
      "variants": [
        { "sku": "DEMO-001", "price": "19.99", "option1": "Default Title" }
      ]
    }
  }'
```

## 5. Where to go next

- Read the [Authentication](authentication.md) guide in full.
- Browse the [Products](products.md) and [Orders](orders.md) references — they cover 80% of integrations.
- Review the [Mapping Considerations](mapping.md) before mapping internal IDs to Octopus IDs.
