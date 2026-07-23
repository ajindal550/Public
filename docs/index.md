# Octopus Bridge API Documentation

**API Version 1.0** &nbsp;·&nbsp; Docs last updated **July 2026** &nbsp;·&nbsp; [See what changed →](changelog.md)

The Octopus Bridge REST API is the integration layer that connects merchants, marketplaces and back-office systems to the Octopus Bridge platform. It exposes everything you need to build a real omni-channel commerce experience: catalog management, inventory sync, order capture, customer records, and financial transactions.

This documentation is the canonical reference for every public endpoint, request, response and field.

## Retail Advisor integration

Octopus Bridge now offers dedicated **Purchase Order (PO)** and **Sales Order (SO)** APIs that plug directly into **Retail Advisor**, letting merchants keep their back-office replenishment and order-fulfilment workflows in perfect sync with every connected channel.

- **[Purchase Orders API](purchase-orders.md)** — create and manage inbound POs sent to suppliers. Retail Advisor uses this endpoint to push replenishment orders into Octopus Bridge and receive real-time status updates.
- **[Orders API](orders.md)** — the Sales Order (SO) surface. Capture, update and reconcile sales orders originating from any connected channel and mirror them into Retail Advisor for fulfilment, accounting and reporting.

If you are building a Retail Advisor connector, start with **[Authentication](authentication.md)** → **[Purchase Orders](purchase-orders.md)** → **[Orders](orders.md)**.

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
