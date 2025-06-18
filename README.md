<server_id>@dthejaka/mcp-tools-test</server_id>
<server_name>mcp-tools-test</server_name>
<readme>
# mcp-tools-test

[![smithery badge](https://smithery.ai/badge/@dthejaka/mcp-tools-test)](https://smithery.ai/server/@dthejaka/mcp-tools-test)
[![pypi badge](https://badge.fury.io/py/protocol2-tools.svg)](https://badge.fury.io/py/protocol2-tools)

A handful of tools to test MCP offers.

## Installing

### Installing via Smithery

To install mcp-tools-test for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@dthejaka/mcp-tools-test):

```bash
npx -y @smithery/cli install @dthejaka/mcp-tools-test --client claude
```

### Auto installation through Hotpot

0. Ensure that you have Python installed on your computer.
1. Install the package through Hotpot agent installation and version management.
2. Out of the box, you get three functions for testing:

- alfred
- natalie
- lisa

These will give you some nice responses!

## Usage
### alfred

Alfred is here to help you answer a query.

An example input is as follows:

```json
{"query": "The planet's approximate diameter"}
```

### natalie

Natalie's number generator will generate a number based on an input temperature (in Celsius).

An example input is as follows:

```json
{"temperature": 22}
```

### lisa

Lisa's fake prediction will predict the output of a basketball game.

An example input is as follows:

```json
{"team1": "Rubber Ducks", "team2": "Kangaroos", "date": "2023-06-15"}
```
</readme>