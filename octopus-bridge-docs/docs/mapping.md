# Mapping Considerations

## 15.1 Products

When synchronizing products from an external system (ERP, PIM, or marketplace) to Octopus Bridge, consider the following mapping rules:

| External Field | Octopus Bridge Field | Notes |
| --- | --- | --- |
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

NOTE: Inventory quantities should always be managed exclusively through the Inventory Levels API, not through the product or variant endpoints. This ensures accurate tracking across multiple locations.

## 15.2 Orders

When pushing orders from an external system (OMS, ERP, or marketplace) to Octopus Bridge, consider the following mapping rules:

| External Field | Octopus Bridge Field | Notes |
| --- | --- | --- |
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

WARNING: The variant_id is required for each line item - the API does not support SKU-based line item resolution. Maintain a SKU-to-variant_id mapping table in your integration layer and refresh it whenever products are created or updated.
