"""Minimal Sodeom MCP client using the official Python SDK.

Install:  pip install "mcp>=2"
Run:      python examples/python/client.py "python 3.14 release notes"
"""

import asyncio
import sys

from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client


async def main(query: str) -> None:
    # mcp 1.x: use `streamablehttp_client` and unpack (read, write, _)
    async with streamable_http_client("https://sodeom.com/mcp") as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await session.list_tools()
            print("Tools:", ", ".join(t.name for t in tools.tools))

            result = await session.call_tool("search", {"query": query})
            print("\n" + result.content[0].text)


if __name__ == "__main__":
    asyncio.run(main(" ".join(sys.argv[1:]) or "python 3.14 release notes"))
