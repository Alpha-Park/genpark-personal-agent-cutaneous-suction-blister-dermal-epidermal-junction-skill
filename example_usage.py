"""
Example usage of Cutaneous Suction Blister DEJ Adhesion Skill.
Demonstrates normal youthful basement membrane integrity vs severe junctional fragility.
"""

import json
from client import SuctionBlisterDEJClient


def main():
    print("=== Testing Cutaneous Suction Blister DEJ Adhesion Skill ===")
    client = SuctionBlisterDEJClient()

    # 1. Healthy young adult with intact BMZ (SBFT = 65.0 min at -220 mmHg, 39C -> DEJ-AI = 100%, Normal)
    res_normal = client.evaluate_sbft(
        blister_formation_time_min=65.0,
        suction_pressure_mmhg=-220.0,
        skin_surface_temp_c=39.0,
        patient_age_years=28
    )
    print("\n[Case 1: Normal Physiological DEJ Adhesion]")
    print(json.dumps(res_normal, indent=2))

    # 2. Patient with severe basement membrane fragility / steroid atrophy (SBFT = 18.0 min -> DEJ-AI = 30%, Marked Fragility)
    res_fragile = client.evaluate_sbft(
        blister_formation_time_min=18.0,
        suction_pressure_mmhg=-220.0,
        skin_surface_temp_c=39.0,
        patient_age_years=72
    )
    print("\n[Case 2: Marked DEJ Fragility / Accelerated Cleavage]")
    print(json.dumps(res_fragile, indent=2))

    # Assertions
    assert res_normal["indices"]["dej_adherence_index"] >= 90.0
    assert "Normal" in res_normal["clinical_interpretation"]["adhesion_status"]
    assert res_fragile["indices"]["dej_adherence_index"] < 40.0
    assert "Fragility" in res_fragile["clinical_interpretation"]["adhesion_status"]
    print("\n[SUCCESS] Suction Blister DEJ Adhesion tests passed!")


if __name__ == "__main__":
    main()
