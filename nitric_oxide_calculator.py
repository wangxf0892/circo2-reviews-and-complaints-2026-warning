"""
Nitric Oxide & L-Citrulline Bioavailability Calculator (CircO2 Reference Protocol)
Open-source utility for estimating sublingual lozenge timing and endothelial support factors.
"""

def calculate_nitric_oxide_protocol(weight_lbs: float, age: int, activity_level: str = "moderate"):
    """
    Calculates estimated daily nitric oxide replenishment targets based on 
    age-related endothelial decline curves and metabolic activity.
    """
    # Baseline endothelial decline factor (accelerates past age 40)
    endothelial_factor = 1.0
    if age > 40:
        decades_past_40 = (age - 40) / 10.0
        endothelial_factor += decades_past_40 * 0.15

    # Activity metabolic demand adjustment
    activity_multipliers = {
        "sedentary": 1.0,
        "moderate": 1.15,
        "high": 1.30
    }
    multiplier = activity_multipliers.get(activity_level.lower(), 1.0)

    # Calculate recommended daily intake thresholds
    daily_lozenges = 1
    if age >= 60 or (age >= 50 and activity_level == "high"):
        daily_lozenges = 2

    timing_recommendation = "Morning on an empty stomach (allow 5-8 min sublingual dissolution)"
    if daily_lozenges == 2:
        timing_recommendation = "1 lozenge at 08:00 AM, 1 lozenge at 02:00 PM (avoid after 06:00 PM)"

    return {
        "User Age": age,
        "Body Weight (lbs)": weight_lbs,
        "Endothelial Decline Index": round(endothelial_factor, 2),
        "Recommended Daily Dosage": f"{daily_lozenges} CircO2 Lozenge(s)",
        "Administration Timing": timing_recommendation,
        "Clinical Target": "Salivary nitrate-nitrite conversion within 20 mins"
    }

if __name__ == "__main__":
    print("=" * 65)
    print(" CircO2 Nitric Oxide Clinical Dosage Estimator (2026 Benchmark)")
    print("=" * 65)
    
    # Baseline test profile: 58-year-old adult, 175 lbs
    result = calculate_nitric_oxide_protocol(weight_lbs=175, age=58, activity_level="moderate")
    for key, value in result.items():
        print(f" {key:<28}: {value}")
    print("=" * 65)
    print(" Notice: Consult a healthcare professional before adjusting dosages.")
