"""
rainwater_calculator.py
A command-line tool that estimates potential rainwater harvesting yield
for a rooftop, based on catchment area, local rainfall, and runoff
coefficient (efficiency of collection for the roof material).

Formula: Harvest (litres) = Area (m2) x Rainfall (mm) x Runoff Coefficient
(1mm of rain over 1m2 = 1 litre of water)
"""

# ---- Typical runoff coefficients by roof type ----
ROOF_COEFFICIENTS = {
    "1": ("RCC/concrete roof", 0.85),
    "2": ("Metal/tin roof", 0.90),
    "3": ("Tiled roof", 0.75),
    "4": ("Green/vegetated roof", 0.50),
}
# ---------------------------------------------------


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def get_roof_type():
    print("\nRoof type:")
    for key, (name, _) in ROOF_COEFFICIENTS.items():
        print(f"{key}. {name}")
    choice = input("Choose 1-4: ").strip()
    return ROOF_COEFFICIENTS.get(choice, ROOF_COEFFICIENTS["1"])


def calculate_harvest():
    print("=== Rainwater Harvesting Calculator ===\n")

    roof_area = get_number("Rooftop catchment area (in square metres): ")
    annual_rainfall = get_number("Average annual rainfall in your area (in mm): ")
    roof_name, coefficient = get_roof_type()

    annual_harvest_litres = roof_area * annual_rainfall * coefficient
    annual_harvest_kilolitres = annual_harvest_litres / 1000

    print(f"\n=== Results for a {roof_name} ===")
    print(f"Rooftop area: {roof_area:.0f} m2")
    print(f"Annual rainfall: {annual_rainfall:.0f} mm")
    print(f"Runoff coefficient: {coefficient}")
    print("-" * 40)
    print(f"Estimated annual harvest: {annual_harvest_litres:,.0f} litres "
          f"(~{annual_harvest_kilolitres:,.1f} kilolitres)")

    # Context: average household water use
    daily_household_use_litres = 500  # rough average for a mid-size Indian household
    days_supplied = annual_harvest_litres / daily_household_use_litres
    print(f"\nAt an average household use of {daily_household_use_litres} litres/day, "
          f"this could supply a household for approximately {days_supplied:.0f} days/year.")


if __name__ == "__main__":
    calculate_harvest()
