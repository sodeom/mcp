# mcp

A public, keyless Model Context Protocol (MCP) server.

Use it from any MCP-compatible client (Claude, OpenCode, LangChain, custom agents) to search the web through Sodeom — no API key and no signup required.

## Endpoint

- MCP URL: `https://sodeom.com/apis/mcp`

## Quick start

1. Open your MCP client/server config.
2. Add a server entry that points to the URL above.
3. Reload/restart your client.
4. Ask your agent to use Sodeom tools (for example: “search the web for …”).

## Example JSON configs

This repo includes ready-to-copy examples in `/examples/agents`:

- `/examples/agents/claude_desktop.json`
- `/examples/agents/cursor_mcp.json`
- `/examples/agents/generic_mcp_client.json`

> Different clients can use slightly different field names. If your client requires extra fields, keep the same endpoint and adapt only the client-specific keys.

## Example tool call payload

See `/examples/requests/web_search_tool_call.json` for a sample JSON-RPC `tools/call` request.
