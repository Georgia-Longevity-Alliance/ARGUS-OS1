"""Expose ARGUS drivers over MCP (model-agnostic transport, per MHS).

Requires the `mcp` python package (pip install mcp). If unavailable, the
module still imports (drivers usable via CLI/code).
"""
from __future__ import annotations

import json
from typing import Dict

from argus_mhs.driver import MHSDriver

_devices: Dict[str, MHSDriver] = {}


def register(driver: MHSDriver):
    _devices[driver.id] = driver


def list_devices() -> str:
    return json.dumps([d.discover() for d in _devices.values()], indent=2)


def read(device: str, qty: str) -> str:
    return json.dumps(_devices[device].read(qty))


def write(device: str, qty: str, value) -> str:
    return json.dumps(_devices[device].write(qty, value))


def run_mcp(server_name: str = "ARGUS") -> None:
    """Start an MCP stdio server wrapping all registered drivers."""
    try:
        from mcp.server.fastmcp import FastMCP
    except Exception as exc:  # mcp not installed
        raise RuntimeError("pip install mcp first") from exc

    mcp = FastMCP(server_name)
    mcp.tool()(list_devices)
    mcp.tool()(read)
    mcp.tool()(write)

    # register devices before run
    mcp.run()
