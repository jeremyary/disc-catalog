from typing import Any
import httpx
import logging
import random
from mcp.server.fastmcp import FastMCP

# init mcp server
mcp = FastMCP("disc-catalog")

# constants
CATALOG_API_BASE = "https://discit-api.fly.dev"
USER_AGENT = "disc-catalog/1.0"


async def make_catalog_request(url: str) -> dict[str, Any] | None:
    """Make disc catalog request"""
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/json"
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            return  response.json()
        except:
            return None

def format_disc(disc: dict) -> str:
    """format disc information"""
    return f"""
Name: {disc['name']}
Manufacturer: {disc['brand']}
Category: {disc['category']}
Stability: {disc['stability']}
Speed: {disc['speed']}
Glide: {disc['glide']}
Turn: {disc['turn']}
Fade: {disc['fade']}
"""

@mcp.tool()
async def get_disc_total_count() -> str:
    """get total count of frisbee discs available in list"""
    url = f"{CATALOG_API_BASE}/disc"
    data = await make_catalog_request(url)
    discs = []

    if not data:
        logging.error("unable to find data")
        return "unable to find data or none found"

    discs.append(f"Total: {len(data)}")
    return "\n---\n".join(discs)

@mcp.tool()
async def get_full_disc_list() -> str:
    """get full list of discs"""
    url = f"{CATALOG_API_BASE}/disc"
    data = await make_catalog_request(url)

    if not data:
        logging.error("unable to find data")
        return "unable to find data or none found"

    logging.info(f"disc list found (len: {len(data)})")

    discs= [format_disc(disc) for disc in data]

    return "\n---\n".join(discs)

@mcp.tool()
async def get_discs_by_manufacturer_brand(brand: str) -> str:
    """get full list of discs made by a manufacturer"""
    url = f"{CATALOG_API_BASE}/disc?brand={brand}"
    data = await make_catalog_request(url)
    discs = []

    if not data:
        logging.error("unable to find data")
        return "unable to find data or none found"

    logging.info(f"disc list found (len: {len(data)})")

    discs= [format_disc(disc) for disc in data]

    return "\n---\n".join(discs)

if __name__ == "__main__":
    mcp.run(transport='stdio')