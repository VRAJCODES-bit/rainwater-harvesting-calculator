# Rainwater Harvesting Calculator

A Python command-line tool that estimates potential rainwater harvesting
yield for a rooftop, based on catchment area, local annual rainfall, and
roof material (runoff coefficient).

Built as a personal project alongside my B.Tech in Climate Change at
Anant National University.

## What it does

Asks the user for:
- Rooftop catchment area (in square metres)
- Average annual rainfall for their area (in mm)
- Roof type (RCC/concrete, metal/tin, tiled, or green roof)

...and calculates the estimated annual rainwater harvest in litres, plus
how many days of average household water use that could supply.

## The formula

```
Harvest (litres) = Area (m2) x Rainfall (mm) x Runoff Coefficient
```

This is the standard formula used in rainwater harvesting system design,
since 1mm of rainfall over 1m2 of catchment area equals 1 litre of water.
Runoff coefficients account for water lost to evaporation, absorption,
and first-flush diversion, and vary by roof material:

| Roof Type | Coefficient |
|---|---|
| RCC/Concrete | 0.85 |
| Metal/Tin | 0.90 |
| Tiled | 0.75 |
| Green/Vegetated | 0.50 |

## Sample output

```
=== Results for a RCC/concrete roof ===
Rooftop area: 100 m2
Annual rainfall: 800 mm
Runoff coefficient: 0.85
----------------------------------------
Estimated annual harvest: 68,000 litres (~68.0 kilolitres)

At an average household use of 500 litres/day, this could supply a
household for approximately 136 days/year.
```

## How to run it

1. Clone this repository:
   ```
   git clone https://github.com/VRAJCODES-bit/rainwater-harvesting-calculator.git
   cd rainwater-harvesting-calculator
   ```

2. Run it (no extra libraries needed — pure Python):
   ```
   python rainwater_calculator.py
   ```

3. Answer the prompts with your rooftop area, local rainfall, and roof type.

## Tech used

- Python (no external libraries required)

## Possible next steps

- Add storage tank sizing recommendations based on the harvest volume
- Pull real rainfall data automatically via the Open-Meteo API (like my
  [Climate Trends Dashboard](https://github.com/VRAJCODES-bit/climate-trends-dashboard))
  instead of manual entry
- Build a simple web interface with Streamlit
