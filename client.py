"""
Cutaneous Suction Blister Formation Time (SBFT) & DEJ Adhesion Client.
Zero-mock pure Python standard library implementation.
Calculates Suction Blister Formation Time (SBFT in minutes),
Dermo-Epidermal Junction Adherence Index (DEJ-AI), and Basement Membrane Zone (BMZ) integrity.
"""

import math
from typing import Dict, Any, Optional


class SuctionBlisterDEJClient:
    """
    Evaluates mechanical adhesion and anchoring fibril integrity across the dermo-epidermal junction:
    - SBFT (minutes): elapsed time to form complete unilocular suction blister at standard negative pressure
    - Standard test conditions: -200 to -250 mmHg negative pressure, skin temp ~38-40 C
    - DEJ Adherence Index (DEJ-AI): min(100.0, (SBFT_min / 60.0) * 100.0)
    - Normalized blistering rate: 1000.0 / SBFT_min
    """

    def __init__(self):
        pass

    def evaluate_sbft(
        self,
        blister_formation_time_min: float,
        suction_pressure_mmhg: Optional[float] = -220.0,
        skin_surface_temp_c: Optional[float] = 39.0,
        blister_diameter_mm: Optional[float] = 6.0,
        patient_age_years: Optional[int] = 30
    ) -> Dict[str, Any]:
        """
        Calculates dermo-epidermal junction adhesion parameters.
        blister_formation_time_min: time in minutes until full blister detachment (10.0 to 180.0 min)
        suction_pressure_mmhg: negative suction pressure in mmHg (negative value, e.g. -220.0)
        skin_surface_temp_c: controlled surface temperature (deg C, typically 38-40 C)
        blister_diameter_mm: diameter of suction cup aperture (mm)
        """
        if blister_formation_time_min <= 0:
            raise ValueError("Blister formation time must be strictly positive.")
        if suction_pressure_mmhg >= 0:
            raise ValueError("Suction pressure must be a negative value in mmHg.")

        # Standard reference time under controlled 39C and -220 mmHg is ~60 minutes
        dej_ai = min(100.0, (blister_formation_time_min / 60.0) * 100.0)

        # Blistering rate index (units/hour)
        blister_velocity_index = round(60.0 / blister_formation_time_min, 2)

        # Temperature-adjusted SBFT index:
        # Higher temperature accelerates enzymatic cleavage and lipid fluidity (approx Q10 = 1.5)
        temp_factor = 1.0 + (skin_surface_temp_c - 39.0) * 0.05
        normalized_sbft_min = round(blister_formation_time_min * temp_factor, 1)

        # Clinical BMZ classification:
        # SBFT < 30 min: Severe DEJ Fragility / Accelerated Cleavage (hemidesmosomal deficiency, corticosteroid atrophy)
        # SBFT 30 - 45 min: Moderate DEJ Laxity / Solar Elastotic Vulnerability
        # SBFT 45 - 90 min: Normal Resilient Dermo-Epidermal Junction Homeostasis
        # SBFT > 90 min: Hypermature DEJ / Dermal Fibrosis or Hyperkeratotic Anchoring
        if blister_formation_time_min < 30.0:
            adhesion_status = "Marked Dermo-Epidermal Junction Fragility"
            bmz_pathophysiology = "Accelerated lamina lucida cleavage; indicates type VII collagen loss, hemidesmosome detachment, or severe dermal-epidermal shearing vulnerability."
        elif blister_formation_time_min < 45.0:
            adhesion_status = "Subclinical DEJ Weakness / Photoaging Fragility"
            bmz_pathophysiology = "Mild attenuation of basement membrane zone anchoring complexes, common in advanced chronological aging or chronic UV exposure."
        elif blister_formation_time_min <= 90.0:
            adhesion_status = "Normal Physiological DEJ Adhesion"
            bmz_pathophysiology = "Intact lamina densa-anchoring fibril network providing robust mechanical tensile shear resistance."
        else:
            adhesion_status = "Dense DEJ Anchoring / Epidermal Hyperadhesion"
            bmz_pathophysiology = "Prolonged blistering time consistent with hyperkeratosis, scleroderma, or dense dermal fibrotic anchoring."

        return {
            "status": "success",
            "kinetics": {
                "blister_formation_time_min": round(blister_formation_time_min, 1),
                "normalized_sbft_39c_min": normalized_sbft_min,
                "blister_velocity_index_per_hour": blister_velocity_index
            },
            "indices": {
                "dej_adherence_index": round(dej_ai, 1),
                "suction_pressure_mmhg": suction_pressure_mmhg,
                "skin_surface_temp_c": skin_surface_temp_c,
                "blister_diameter_mm": blister_diameter_mm
            },
            "clinical_interpretation": {
                "adhesion_status": adhesion_status,
                "bmz_pathophysiology": bmz_pathophysiology
            }
        }
