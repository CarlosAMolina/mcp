## Introduction

Project to learn MPC.

## Installation

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

Check that you have node >= 18 to run npx:

```bash
node -v
npx -v
```

## Run

Run FastMCP server:

```bash
$ python src/main.py
# Verify SSE enpoint is reachable
$ curl -N http://127.0.0.1:8001/sse
```

Launch MCP inspector:

```bash
npx @modelcontextprotocol/inspector http://127.0.0.1:8001/sse
```

Select connect to the server and go to the `Tool` section.

## Endpoints

- [API Endpoint](http://127.0.0.1:8000/)
- [Interactive Swagger Docs](http://127.0.0.1:8000/docs)
- [MCP SSE Server Endpoint](http://127.0.0.1:8001/sse)
