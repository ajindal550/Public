# Sample Code

## 16.1 Postman

A Postman collection covering all Octopus Bridge API endpoints is available from your partner integration manager. The collection includes pre-configured environments for sandbox and production, with variable placeholders for API key, secret, and base URL.

| Variable | Description |
| --- | --- |
| {{base_url}} | https://octopusapi.24sevencommerce.com/admin/api/2020-01 |
| {{api_key}} | Your X-API-Key value |
| {{api_secret}} | Your X-API-Secret value |
| {{shop_id}} | Your connected shop identifier |

To authenticate requests in Postman, set the following headers on each request or configure them at the collection level under Authorization:

X-API-Key: {{api_key}}
X-API-Secret: {{api_secret}}
Content-Type: application/json

## 16.2 C#/.NET

The following C# example demonstrates authenticating and retrieving a list of products using HttpClient:

using System;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Threading.Tasks;
using Newtonsoft.Json;

public class OctopusBridgeClient
{
private readonly HttpClient _client;
private const string BaseUrl = "https://octopusapi.24sevencommerce.com/admin/api/2020-01";

public OctopusBridgeClient(string apiKey, string apiSecret)
{
_client = new HttpClient();
_client.DefaultRequestHeaders.Add("X-API-Key", apiKey);
_client.DefaultRequestHeaders.Add("X-API-Secret", apiSecret);
_client.DefaultRequestHeaders.Accept
.Add(new MediaTypeWithQualityHeaderValue("application/json"));
}

public async Task<string> GetProductsAsync(int limit = 50, int page = 1)
{
var url = $"{BaseUrl}/products?limit={limit}&page={page}";
var response = await _client.GetAsync(url);
response.EnsureSuccessStatusCode();
return await response.Content.ReadAsStringAsync();
}

public async Task<string> CreateOrderAsync(object orderPayload)
{
var json = JsonConvert.SerializeObject(new { order = orderPayload });
var content = new StringContent(json,
System.Text.Encoding.UTF8, "application/json");
var response = await _client.PostAsync($"{BaseUrl}/orders", content);
response.EnsureSuccessStatusCode();
return await response.Content.ReadAsStringAsync();
}
}

// Usage
class Program
{
static async Task Main(string[] args)
{
var client = new OctopusBridgeClient("your_api_key", "your_api_secret");

// Get products
var products = await client.GetProductsAsync(limit: 50, page: 1);
Console.WriteLine(products);

// Create an order
var order = new {
email = "customer@example.com",
financial_status = "pending",
line_items = new[] {
new { variant_id = "var_002", quantity = 1 }
},
shipping_address = new {
first_name = "John", last_name = "Smith",
address1 = "123 Main St", city = "Austin",
province_code = "TX", zip = "78701", country_code = "US"
}
};
var result = await client.CreateOrderAsync(order);
Console.WriteLine(result);
}
}

TIP: Implement a retry wrapper with exponential backoff around all API calls to handle 429 rate limit responses and transient 500 errors gracefully.

Questions about this documentation? Contact your partner integration manager.
© 2026 Octopus Bridge  |  REST API Reference  |  v1.0  |  Confidential
```
