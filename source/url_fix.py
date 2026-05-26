"""Batch-update all api.octopusbridge.com/v1/... URLs to the real
octopusapi.24sevencommerce.com/admin/api/2020-01/...json paths."""
import os
import re

DOCS = "/app/docs"

# Exact-string replacements (string -> string).  Order matters: more specific first.
REPLACEMENTS = [
    # Base URLs first (longest match wins)
    ("https://api.octopusbridge.com/v1/products/bulk",
     "https://octopusapi.24sevencommerce.com/admin/api/2020-01/BulkProduct/bulkpost.json"),
    ("https://api.octopusbridge.com/v1/products/{product_id}/images",
     "https://octopusapi.24sevencommerce.com/admin/api/2020-01/products/{product_id}/images.json"),
    ("https://api.octopusbridge.com/v1/products/{product_id}",
     "https://octopusapi.24sevencommerce.com/admin/api/2020-01/products/{product_id}.json"),
    ("https://api.octopusbridge.com/v1/products",
     "https://octopusapi.24sevencommerce.com/admin/api/2020-01/products.json"),

    ("https://api.octopusbridge.com/v1/orders/{order_id}/transactions",
     "https://octopusapi.24sevencommerce.com/admin/api/2020-01/orders/{order_id}/transactions.json"),
    ("https://api.octopusbridge.com/v1/orders/{order_id}",
     "https://octopusapi.24sevencommerce.com/admin/api/2020-01/orders/{order_id}.json"),
    ("https://api.octopusbridge.com/v1/orders",
     "https://octopusapi.24sevencommerce.com/admin/api/2020-01/orders.json"),

    ("https://api.octopusbridge.com/v1/inventory_levels/set",
     "https://octopusapi.24sevencommerce.com/admin/api/2020-01/inventory_levels/set.json"),
    ("https://api.octopusbridge.com/v1/inventory_levels/bulk",
     "https://octopusapi.24sevencommerce.com/admin/api/2020-01/inventory_levels/bulk.json"),

    ("https://api.octopusbridge.com/v1/collects",
     "https://octopusapi.24sevencommerce.com/admin/api/2020-01/collects.json"),
    ("https://api.octopusbridge.com/v1/customers",
     "https://octopusapi.24sevencommerce.com/admin/api/2020-01/customers.json"),
    ("https://api.octopusbridge.com/v1/locations",
     "https://octopusapi.24sevencommerce.com/admin/api/2020-01/locations.json"),

    # Base URL declarations (used in index.md and samples.md)
    ("https://api.octopusbridge.com/v1",
     "https://octopusapi.24sevencommerce.com/admin/api/2020-01"),

    # Purchase orders: keep path, change host only
    ("https://api.octopusbridge.com/admin/api/2025-09/PurchaseOrder/CreateOrder.json",
     "https://octopusapi.24sevencommerce.com/admin/api/2025-09/PurchaseOrder/CreateOrder.json"),
    ("https://api.octopusbridge.com/admin/api/2025-09/PurchaseOrder/Purchaseorderline.json",
     "https://octopusapi.24sevencommerce.com/admin/api/2025-09/PurchaseOrder/Purchaseorderline.json"),

    # Host headers in HTTP request examples
    ("Host: api.octopusbridge.com",
     "Host: octopusapi.24sevencommerce.com"),
]

total_subs = 0
files_touched = []

for fn in sorted(os.listdir(DOCS)):
    if not fn.endswith(".md"):
        continue
    path = os.path.join(DOCS, fn)
    with open(path) as f:
        text = f.read()
    original = text
    file_subs = 0
    for old, new in REPLACEMENTS:
        count = text.count(old)
        if count:
            text = text.replace(old, new)
            file_subs += count
    if text != original:
        with open(path, "w") as f:
            f.write(text)
        files_touched.append((fn, file_subs))
        total_subs += file_subs

print(f"Total substitutions: {total_subs}")
print(f"Files touched: {len(files_touched)}")
for fn, n in files_touched:
    print(f"  {fn:25}  {n} change(s)")
