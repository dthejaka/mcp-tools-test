import asyncio
from mcp.server.fastmcp import FastMCP
from typing import List
from tools.shopify_search import shopify_search

# Create MCP server
mcp = FastMCP("ToolsProductCatalogue")

store_domain = 'surfnet-store.myshopify.com'
access_token = '19416543129c17a489c8340f337ed858'
# Tool: Check Leave Balance

@mcp.tool()
async def get_products(search_query: str) -> str:
    """Retrieve products from the product catalogue"""
    data = await shopify_search(store_domain, access_token, search_query)
    if data:
        return data
    return "No products found"


if __name__ == "__main__":
    mcp.run()