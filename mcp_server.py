"""
MCP Server for Cutaneous Suction Blister DEJ Adhesion Skill.
Provides standard Model Context Protocol JSON-RPC tool endpoints.
"""

import sys
import json
from client import SuctionBlisterDEJClient


def main():
    client = SuctionBlisterDEJClient()

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
        except Exception:
            continue

        method = req.get("method")
        msg_id = req.get("id")

        if method == "tools/list":
            res = {
                "jsonrpc": "2.0",
                "id": msg_id,
                "result": {
                    "tools": [
                        {
                            "name": "evaluate_sbft",
                            "description": "Calculates Suction Blister Formation Time (SBFT in minutes) and Dermo-Epidermal Junction Adherence Index (DEJ-AI) to evaluate basement membrane zone structural integrity.",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "blister_formation_time_min": {
                                        "type": "number",
                                        "description": "Elapsed suction blistering time in minutes."
                                    },
                                    "suction_pressure_mmhg": {
                                        "type": "number",
                                        "description": "Applied negative pressure in mmHg (e.g. -220.0)."
                                    },
                                    "skin_surface_temp_c": {
                                        "type": "number",
                                        "description": "Controlled skin temperature in degrees Celsius (default: 39.0)."
                                    },
                                    "blister_diameter_mm": {
                                        "type": "number",
                                        "description": "Diameter of aperture in millimeters (default: 6.0)."
                                    },
                                    "patient_age_years": {
                                        "type": "integer",
                                        "description": "Patient age in years (optional)."
                                    }
                                },
                                "required": [
                                    "blister_formation_time_min"
                                ]
                            }
                        }
                    ]
                }
            }
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()

        elif method == "tools/call":
            params = req.get("params", {})
            name = params.get("name")
            args = params.get("arguments", {})

            if name == "evaluate_sbft":
                try:
                    out = client.evaluate_sbft(**args)
                    res = {
                        "jsonrpc": "2.0",
                        "id": msg_id,
                        "result": {
                            "content": [{"type": "text", "text": json.dumps(out, indent=2)}]
                        }
                    }
                except Exception as e:
                    res = {
                        "jsonrpc": "2.0",
                        "id": msg_id,
                        "isError": True,
                        "error": {"code": -32000, "message": str(e)}
                    }
                sys.stdout.write(json.dumps(res) + "\n")
                sys.stdout.flush()


if __name__ == "__main__":
    main()
