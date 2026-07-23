# Octopus Bridge API Documentation

**API Version 1.0** &nbsp;·&nbsp; Docs last updated **July 2026** &nbsp;·&nbsp; [See what changed →](changelog.md)

The Octopus Bridge REST API is the integration layer that connects merchants, marketplaces and back-office systems to the Octopus Bridge platform. It exposes everything you need to build a real omni-channel commerce experience: catalog management, inventory sync, order capture, customer records, and financial transactions.

This documentation is the canonical reference for every public endpoint, request, response and field.

## Retail Advisor integration

**[Retail Advisor](https://octopusbridge.com/retail-advisor)** is Octopus Bridge's AI-powered retail intelligence product. It connects to a merchant's POS and gives store owners instant, plain-English answers about their business — right from their phone. Think of it as a ChatGPT-style assistant trained specifically on that merchant's retail data.

Retail Advisor turns raw POS data into daily decisions:

- **Daily insights** — what's selling, what's slowing, what needs attention right now
- **Inventory guidance** — low-stock alerts, overstock warnings, reorder suggestions
- **Sales performance** — top sellers, slow movers, trend movements
- **Forecasting** — category-level seasonal demand and buying recommendations
- **Vendor intelligence** — which vendors need a PO, which are underperforming
- **Ask anything** — *"What should I reorder today?" · "What's trending down?" · "Which items are at risk?"*

For this intelligence to work, Retail Advisor needs a continuous feed of **sales order (SO)** and **purchase order (PO)** activity from the merchant's POS. That's what the following two endpoints do:

- **[Purchase Orders API](purchase-orders.md)** — push POs raised in the POS into Octopus Bridge so Retail Advisor can build vendor performance and reorder recommendations.
- **[Orders API](orders.md)** *(used here as the Sales Order surface)* — stream sales orders in so Retail Advisor can compute what's selling, what's slowing, and forecast seasonal demand.

> **When are PO / SO endpoints required?**
> **Only when the downstream destination is Retail Advisor.** If you are integrating a merchant to Shopify, BigCommerce, or any other non-RA destination, you do **not** need to call the PO or SO endpoints — the standard catalog, inventory and orders endpoints are enough.

## Which endpoints do I need?

All partners use the same core Octopus Bridge endpoints regardless of the downstream destination. PO / SO are conditional and only apply to Retail Advisor.

| Your integration goal | Endpoints you use | PO required? | SO required? |
| --- | --- | --- | --- |
| Basic catalog & inventory sync (e.g. Shopify, BigCommerce) | [Products](products.md), [Variants](variants.md), [Images](images.md), [Inventory Levels](inventory.md), [Collections](collections.md), [Collects](collects.md), [Locations](locations.md) | ❌ No | ❌ No |
| Full commerce sync (adds order capture & customers) | Above **+** [Customers](customers.md), [Orders](orders.md), [Transactions](transactions.md) | ❌ No | ❌ No |
| **Retail Advisor** — feed POS data into the AI advisor | Above **+** [Purchase Orders](purchase-orders.md) **+** [Orders](orders.md) tagged as SO | ✅ Yes | ✅ Yes |

If you're unsure which profile applies to your integration, your Octopus Bridge account manager can confirm.

## Base URL

```
https://octopusapi.24sevencommerce.com/admin/api/2020-01
```

> All API traffic is served over HTTPS. Plain HTTP requests are rejected.

## How the API is organized

| Group | What it does |
| --- | --- |
| [Shop](shop.md) | Read configuration and metadata about the connected store. |
| [Products](products.md) | Create, read, update, delete and bulk-sync products. |
| [Images](images.md) | Manage product image assets. |
| [Variants](variants.md) | Manage product variants (size, color, etc.). |
| [Locations](locations.md) | Read the physical/logical locations of a shop. |
| [Inventory Levels](inventory.md) | Set and bulk-update stock per location. |
| [Custom Collections](collections.md) | Curated groupings of products. |
| [Collects](collects.md) | The join table between products and collections. |
| [Orders](orders.md) | Capture, read, update and cancel orders. |
| [Purchase Orders](purchase-orders.md) | Inbound purchase orders to suppliers. |
| [Customers](customers.md) | Customer records and search. |
| [Transactions](transactions.md) | Payment transactions per order. |

## Conventions

- All request and response bodies are JSON encoded as `application/json; charset=utf-8`.
- All timestamps are ISO 8601 with timezone offset (e.g. `2026-03-14T09:30:00-08:00`).
- IDs returned by the API are integers unless documented otherwise.
- All endpoints require authentication — see [Authentication](authentication.md).

## Support

Questions, bug reports, or integration help?
Email **api@octopusbridge.com** or open an issue on the [GitHub repository](https://github.com/).

---

© Octopus Bridge, Inc. — Confidential / Partner Use.
