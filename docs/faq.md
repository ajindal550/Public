# FAQ

## 14.1 Product Questions

**1. Can I create a product without variants?**

Yes. If you omit the `variants` array in a `POST /products` request, the API automatically creates a default variant with the product title. You can update this default variant's price and SKU via `PUT /variants/{id}`.

**2. What happens to inventory when I delete a product?**

Deleting a product permanently removes all associated variants, images, and inventory records. Inventory is not automatically restocked. If you need to preserve inventory history, consider setting the product status to `archived` instead.

**3. How many products can I send in a Bulk POST request?**

The bulk POST endpoint accepts a maximum of 250 product objects per request. For larger catalogs, paginate the requests and implement retry logic with exponential backoff for 429 rate-limit responses.

**4. Can I update variant inventory through the Products endpoint?**

No. Inventory quantities must be managed through the Inventory Levels API (`POST /inventory_levels/set` or the bulk endpoint). The Products and Variants endpoints handle product data only.

## 14.2 Order Questions

**1. Can I modify line items after an order is created?**

No. Line items, discount codes, and shipping lines are locked after order creation. To change order contents, cancel the order and create a new one, or use the Refund API to issue credits.

**2. Why does `DELETE /orders` return a 422 error?**

Deletion is restricted to test or sandbox orders with no financial activity. Orders that have payment transactions, fulfillments, or refunds must be cancelled using `POST /orders/{id}/cancel` instead of deleted.

**3. Does creating an order automatically decrement inventory?**

Inventory is decremented when an order is created with `financial_status: paid`. For pending or authorized orders, inventory is reserved but not decremented until payment is captured.

**4. How do I associate an order with an existing customer?**

Include a `customer` object with just the `id` field in the `POST /orders` request body: `{ "customer": { "id": "cust_jane01" } }`. The customer's `orders_count` and `total_spent` will be updated automatically.

## 14.3 General Questions

**1. What is the rate limit for the API?**

The default rate limit is 250 requests per minute per API key, shared across all endpoints. Rate-limit status is returned in every response via `X-RateLimit-Limit`, `X-RateLimit-Remaining`, and `X-RateLimit-Reset` headers. Contact your partner manager for burst-limit increases.

**2. Are all API responses paginated?**

List endpoints (`GET /products`, `GET /orders`, etc.) return paginated results. The response includes a `pagination` object with `total`, `page`, `limit`, and `pages` fields. Use the `since_id` parameter for cursor-based pagination in high-volume scenarios.

**3. What datetime format does the API use?**

All datetime fields use ISO 8601 format in UTC (e.g., `2024-07-15T11:00:00Z`). When filtering with parameters like `created_at_min`, provide datetime values in the same format.

**4. How do I handle webhook events?**

Register webhook subscribers in the shop admin or via the Webhooks API. The following events are dispatched automatically: `orders/create`, `orders/updated`, `orders/delete`, `products/create`, `products/update`, `products/delete`, `inventory_levels/update`.
