import uvicorn
from fastapi import FastAPI
from fastmcp import FastMCP

mcp = FastMCP("GenAI-Asset-Registry")

@mcp.tool()
def list_assets(asset_type: str = "all") -> dict:
    """List registered GenAI assets like models, agents, or MCP."""
    assets = [
        {"id": "ast-01", "name": "LLM-Router", "type": "model_provider"},
        {"id": "ast-02", "name": "CustomerSupport-Agent", "type": "agent"},
        {"id": "ast-03", "name": "PostgreSQL-MCP", "type": "mcp"},
    ]
    if asset_type != "all":
        assets =[asset for asset in assets if asset["type"] == asset_type]
    return {"count": len(assets), "assets": assets}

@mcp.tool()
def get_agent_metrics(agent_id: str) -> dict:
    """Fetch execution metrics and token usage for a specific agent."""
    return {
        "agent_id": agent_id,
        "total_calls": 1420,
        "avg_latency_ms": 320,
        "tokens_consumed": 185000,
        "status": "active",
    }

app = FastAPI(
    title="GenAI Asset Registry & MCP Gateway",
    description="Backend platform for LLM assets, tracking and MCP endpoints.",
    version="0.1.0",
)

@app.get("/")
async def read_root():
    """Root endpoint to check service basic information."""
    return {
        "service": "GenAI Asset Management",
        "status": "online",
        "mcp_enabled": "true",
    }

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}


if __name__ == "__main__":
    import threading
    mcp_thread = threading.Thread(
        target=lambda: mcp.run(transport="sse", host="127.0.0.1", port=8001)
    )
    mcp_thread.daemon = True
    mcp_thread.start()
    uvicorn.run(app, host="127.0.0.1", port=8000)
