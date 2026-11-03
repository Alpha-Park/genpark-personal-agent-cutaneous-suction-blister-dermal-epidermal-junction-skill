# Cutaneous Suction Blister DEJ Adhesion Personal Agent Skill

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python: 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-zero-brightgreen.svg)]()
[![Model Context Protocol](https://img.shields.io/badge/MCP-Standard%20JSON--RPC-orange.svg)]()
[![Production Ready](https://img.shields.io/badge/status-production--ready-green.svg)]()

Deterministic, zero-mock personal agent micro-skill for calculating Suction Blister Formation Time (SBFT in minutes) and Dermo-Epidermal Junction Adherence Index (DEJ-AI) to evaluate basement membrane zone mechanical resilience.

## Architecture

```mermaid
flowchart TD
    A[Negative Suction Pressure -220 mmHg @ 39C] --> B[Measure Time to Blister Formation min]
    B --> C[Compute DEJ Adherence Index DEJ-AI]
    C --> D[Normalize to 39C Thermal Reference]
    D --> E[Classify Normal vs Marked Lamina Lucida Fragility]
```

## Quickstart

```python
from client import SuctionBlisterDEJClient

client = SuctionBlisterDEJClient()
result = client.evaluate_sbft(
    blister_formation_time_min=65.0,
    suction_pressure_mmhg=-220.0,
    skin_surface_temp_c=39.0
)
print(result)
```

## License

Apache-2.0
