# Changelog

All notable changes to the **Octopus Bridge REST API documentation** are listed here in reverse chronological order.

The **API itself** follows [Semantic Versioning](https://semver.org/). Docs revisions (like typo fixes, reformatting, and clarifications) do **not** change the API version — they just get a new dated entry below.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

---

## Docs revision — July 2026

Documentation-only updates. **The underlying API behaviour has not changed.**

### Added
- **Retail Advisor section:** Added a dedicated Retail Advisor block to the Introduction page calling out the PO and SO APIs that now power the Retail Advisor connector. Includes a suggested integration path (Authentication → Purchase Orders → Orders) so partners building against Retail Advisor can get to the right endpoints in one click.

### Fixed
- **Page title & link previews:** Sharing the docs URL in Slack/Teams/iMessage used to unfurl as "Overview". Updated the `<title>` tag, docsify site name and sidebar label to consistently read **"Octopus Bridge API Documentation"**, and added Open Graph + Twitter Card meta tags so link previews look right in every messaging app.
- **Products & Variants:** The `PriceA`, `PriceB`, `PriceC`, and `ListPrice` fields shown in `POST /products` and `POST /variants` samples were documented in PascalCase, but only the snake_case versions (`price_a`, `price_b`, `price_c`, `list_price`) actually persist. All 32 field references corrected to snake_case across `products.md` and `variants.md`.
- **All resource pages:** Endpoint URLs were shown as `https://api.octopusbridge.com/v1/…`. Corrected to the real host `https://octopusapi.24sevencommerce.com/admin/api/2020-01/…json` across 25 URL references in 11 files.
- **Orders — POST endpoint (Section 4):** The entire section had heading-style formatting corruption from the source Word doc that made request/response samples render as unformatted headings. Section fully rewritten: request/response bodies now properly fenced as JSON code blocks, sub-sections renumbered as `H3`, and validation rules restructured as bullet lists.
- **Orders — misc:** GET-by-since_id and GET-count examples were rendered as flat text; wrapped in `http` and `json` code fences. Removed a stray "Copy" artifact and fixed a `Get` → `GET` typo in the count example.
- **Purchase Orders, Customers, Transactions:** ~50 sample JSON / HTTP request blocks were rendering as unformatted plain text. All wrapped in fenced `json` / `http` code blocks — copy-to-clipboard and syntax highlighting now work everywhere.
- **Products — POST endpoint:** The variant matrix `options` array was rendered as inline text. Wrapped in a fenced `json` block with clean array formatting.
- **Variants:** The prose paragraph listing every variant endpoint was converted to a proper method/endpoint/description table. Also fixed source-doc typos: `?sku={SKU_id)` → `?sku={SKU_id}`, missing `GET` method label on the count endpoint, and `{variant_id}` → `{product_id}` in the POST endpoint path.
- **FAQ:** Product, Order, and General Question sections were rendering as walls of paragraph text. Each Q/A now uses bold numbered questions separated from answers, with inline code formatting on all field/endpoint references.
- **Orders overview:** Inline field references `octopus_created_at` / `octopus_updated_at` were on their own lines; converted to inline code inside the surrounding paragraph. Valid Statuses list converted from prose to a bullet list. Two paragraphs mistakenly styled as H2 headings restored to plain prose.
- **Cover page & sidebar:** Added a subtle "Docs last updated" timestamp and a "What's new →" link so partners can immediately see what changed between revisions.
- **CNAME:** Restored the `CNAME` file at the repo root that was inadvertently removed during an "Overwrite everything" push, which had caused `developers.octopusbridge.com` to briefly return "Site not found".

### Notes for API integrators
- No client changes required — this is a docs-only revision.
- If you had followed the old `api.octopusbridge.com/v1/...` URL pattern from a previous version of these docs, please switch to the current `octopusapi.24sevencommerce.com/admin/api/2020-01/...json` endpoints.
- Similarly, if your integration was writing to `PriceA` / `PriceB` / `PriceC` / `ListPrice`, those values are being silently discarded server-side — switch to the snake_case field names to make them persist.

---

## [1.0.0] — 2026-03

### Added
- Initial public release.
- Endpoints: Shop, Products (incl. bulk), Images, Variants, Locations, Inventory Levels (incl. bulk), Custom Collections (incl. bulk), Collects (incl. bulk), Orders, Purchase Orders, Customers, Transactions.
- Authentication via `X-Octopus-Access-Token` and OAuth 2.0 Bearer tokens.
- OAuth scopes: `read_products`, `write_products`, `read_orders`, `write_orders`, `read_customers`, `read_inventory`, `write_inventory`, `read_collections`, `write_collections`.
