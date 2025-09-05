from fastmcp import tool

@tool()
def hello_world():
    """Simple Hello World tool."""
    return {"message": "Hello World from MCP!"}
