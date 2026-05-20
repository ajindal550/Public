# Changelog

All notable changes to the Octopus Bridge public API will be documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this API adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] — 2026-03

### Added
- Initial public release.
- Endpoints: Shop, Products (incl. bulk), Images, Variants, Locations, Inventory Levels (incl. bulk), Custom Collections (incl. bulk), Collects (incl. bulk), Orders, Purchase Orders, Customers, Transactions.
- Authentication via `X-Octopus-Access-Token` and OAuth 2.0 Bearer tokens.
- OAuth scopes: `read_products`, `write_products`, `read_orders`, `write_orders`, `read_customers`, `read_inventory`, `write_inventory`, `read_collections`, `write_collections`.
