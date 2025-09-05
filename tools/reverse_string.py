from fastmcp import tool

@tool()
def reverse_string(text: str):
    """Takes a string and returns its reverse."""
    return {"reversed": text[::-1]}
