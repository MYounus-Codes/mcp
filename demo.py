from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo Server")

@mcp.tool()
def my_info(name: str, age: int) -> str:
    """Echo the input message"""
    return f"Name: {name}, Age: {age}"

if __name__ == "__main__":
    mcp.run(transport="stdio")
