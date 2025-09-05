# MCP with MCPO Demo

This repository demonstrates how to build and run **MCP (Model Context Protocol)** tools using **MCPO**.  
We'll cover everything from setup to creating sample tools and running the MCP server.

---

## **What is MCP?**
**MCP (Model Context Protocol)** is a standard protocol that allows LLMs (like GPT, Claude, etc.) to interact with external tools, databases, and APIs efficiently.

---

## **What is MCPO?**
**MCPO** is the official MCP Orchestrator, which manages your MCP servers and tools.  
It allows your LLM to **auto-discover available tools** and decide when to call them.

---

## **1. Prerequisites**
- Python **3.11+**
- [uv](https://docs.astral.sh/uv/) (Recommended for virtual environment management)
- Git

---

## **2. Setup Instructions**

### **Step 1 — Clone the Repository**
```bash
git clone https://github.com/mkamranr/mcp-mcpo.git
cd mcp-mcpo
```

### **Step 2 — Create Virtual Environment**
```bash
uv venv --python 3.11
```

Activate the environment:

**Linux / Mac:**
```bash
source .venv/bin/activate
```

**Windows (PowerShell):**
```bash
.venv\Scripts\activate
```

### **Step 3 — Install Dependencies**
```bash
uv pip install fastmcp mcpo
```
Or:
```bash
uv pip install -r requirements.txt
```

---

## **3. Project Structure**
```
MCP-MCPO/
├── tools/
│   ├── hello_world.py
│   ├── reverse_string.py
├── server.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## **4. MCP Tools**

### **4.1 Hello World Tool** (`tools/hello_world.py`)
```python
from fastmcp import tool

@tool()
def hello_world():
    """Simple Hello World tool."""
    return {"message": "Hello World from MCP!"}
```

### **4.2 Reverse String Tool** (`tools/reverse_string.py`)
```python
from fastmcp import tool

@tool()
def reverse_string(text: str):
    """Takes a string and returns its reverse."""
    return {"reversed": text[::-1]}
```

---

## **5. MCP Server** (`server.py`)
```python
from fastmcp import FastMCP
from tools.hello_world import hello_world
from tools.reverse_string import reverse_string

mcp_server = FastMCP("mcp-demo-server")
mcp_server.tool()(hello_world)
mcp_server.tool()(reverse_string)

```

---

## **6. Running the Server**
```bash
mcpo --host 0.0.0.0 --port 8000 -- python server.py
```

---

## **7. Testing Tools**

### Hello World:
```bash
curl -X POST http://127.0.0.1:8000/tools/hello_world
```
**Response:**
```json
{ "message": "Hello World from MCP!" }
```

### Reverse String:
```bash
curl -X POST http://127.0.0.1:8000/tools/reverse_string -H "Content-Type: application/json" -d '{"text":"MCP Demo"}'
```
**Response:**
```json
{ "reversed": "omeD PCM" }
```

---

## **License**
MIT License © 2025
