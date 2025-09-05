from fastmcp import FastMCP
from tools.hello_world import hello_world
from tools.reverse_string import reverse_string

mcp_server = FastMCP("mcp-demo-server")
mcp_server.tool()(hello_world)
mcp_server.tool()(reverse_string)

if __name__ == "__main__":
    mcp_server.run()
