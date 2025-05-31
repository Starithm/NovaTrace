## Prompt 1:
### Took 2m 33sec on Mistral
Extract the following structured fields from the given astronomy event description:

- Dates
- Times
- Time References (like P0, P90)
- Coordinates (RA and Dec)
- Instrument/Telescope
- Detector (if any)
- Redshift (if present)
- Confidence level
- Any uncertainity values
- Any Energy Measurements (e.g. GRB, neutrino)

Return ONLY a JSON object with with keys as mentioned above.
If a field is not present, use null.

Event Description:
\"\"\"
{text}
\"\"\"
"""

## Prompt 2:
### Took 13m on Mistral
Extract the following structured fields from the given astronomy event description:

- Dates
- Times
- Time References (like P0, P90)
- Coordinates (RA and Dec)
- Instrument/Telescope
- Detector (if any)
- Redshift (if present)
- Confidence level
- Any numeric values (e.g alpha, fluence, wavelengths, also mention what the value is)
- Any Particles (e.g. GRB, neutrino)

Return ONLY a JSON object with with keys as mentioned above.
If a field is not present, use null.

Event Description:
\"\"\"
{text}
\"\"\"
"""
### Mistral Output:
{'Dates': ['2017-09-22'], 'Times': ['20:54:30.4 UTC', '+-300 s around T0'], 'Time_References': None, 'Coordinates': None, 'Instrument/Telescope': ['INTEGRAL', 'SPI-ACS', 'IBIS/Veto'], 'Detector': None, 'Redshift': None, 'Confidence_level': ['3-sigma'], 'Numeric_Values': {'Fluence (75-2000 keV) for burst lasting less than 1 s with a characteristic short GRB spectrum': '2.8x10^-7 erg/cm^2', 'Peak flux upper limit for a typical long GRB spectrum in 8 s time scale in 75-2000 keV energy range': '7.8x10^-7 erg/cm^2/s'}, 'Particles': ['GRB']}

## Prompt 3
Extract the following structured fields from the given astronomy event description:

- Coordinates (RA and Dec)
- Redshift (if present)
- Confidence level
- Any numeric values (e.g alpha, fluence, wavelengths, also mention what the value is)
- Any Particles (e.g. GRB, neutrino)

Return ONLY a JSON object with with keys as mentioned above.
If a field is not present, use null.

Event Description:
\"\"\"
{text}
\"\"\"
"""
### Took 52sec but with chrome almost closed. (Mistral)
### Took 2ms (Mathstral: 7b)


### Mistral Output:
{'Coordinates': None, 'Redshift': None, 'Confidence level': '3-sigma', 'Fluence (75-2000 keV) (short GRB spectrum)': 2.8e-07, 'Flux peak upper limit (long GRB spectrum)': 7.8e-07, 'Particles': ['GRB']}
### mathstral:7b: [39990]
{'Coordinates': {'RA': '02h 54m 34.96s', 'Dec': '+65d 33m 33.8s'}, 'Redshift': None, 'Confidence Level': None, 'Numeric Values': {'Tmid-T0': 62554, 'Date Time': '2025-03-31 23:11:20', 'Site Coordinates (J2000)': ['(02h 54m 34.96s , +65d 33m 33.8s)', '(02h 54m 36.68s , +65d 33m 23.8s)', '(02h 53m 45.13s , +65d 44m 21.5s)'], 'Expt': 60, 'Limit': ['17.7', '17.9', '17.7']}, 'Particles': ['GRB']}




# Mathstral:7b

### Mathstral:7b with table prompt
{
    "Coordinates": {
      "RA": "03h 18m 00.28s",
      "Dec": "-38d 23m 19.1s"
    },
    "Redshift": null,
    "Confidence Levels": null,
    "Numeric Values": [
      {
        "Name": "Limit",
        "Value": [14.1, 14.5, 14.4, 14.4, 14.7, 14.8, 14.8, 16.3, 16.5, 17.0, 18.2, 17.1, 18.4, 17.1, 18.3, 17.1, 18.2, 17.1, 18.1, 18.0, 17.1, 18.0, 17.2, 18.0, 17.1, 17.1, 16.9, 17.4]
      }
    ],
    "Markdown Tables": [
      {
        "Tmid-T0": 70,
        "Date Time": "2025-05-09 22:34:33",
        "Site": "MASTER-OAFA",
        "Coordinates (J2000)": "(03h 18m 00.28s , -38d 23m 19.1s)",
        "Filt.": "C",
        "Expt.": 10,
        "Limit": 14.1
      },
      {
        "Tmid-T0": 104,
        "Date Time": "2025-05-09 22:35:03",
        "Site": "MASTER-OAFA",
        "Coordinates (J2000)": "(03h 18m 00.24s , -38d 23m 19.1s)",
        "Filt.": "C",
        "Expt.": 20,
        "Limit": 14.5
      },
      {
        "Tmid-T0": 138,
        "Date Time": "2025-05-09 22:35:42",
        "Site": "MASTER-OAFA",
        "Coordinates (J2000)": "(03h 18m 00.14s , -38d 23m 18.9s)",
        "Filt.": "C",
        "Expt.": 10,
        "Limit": 14.4
      },
      //...
    ]
  }

### GOOD one: CIRCULAR: 40409
{
  "redshift": "NA",
  "confidence": "NA",
  "numeric_values": {
    "zenith_distance": 70,
    "sun_altitude": -9.7,
    "galactic_latitude": -60,
    "longitude": 237,
    "limit": [
      14.1,
      14.5,
      14.4,
      14.4,
      14.7,
      14.8,
      14.8,
      16.3,
      16.5,
      17,
      18.2,
      17.1,
      18.4,
      17.1,
      18.3,
      17.1,
      18.2,
      18,
      17.1,
      18,
      17.2,
      18,
      17.1,
      17.1,
      17.6,
      16.9,
      17.4
    ]
  },
  "table": [
    {
      "Tmid-T0": 70,
      "Date Time": "2025-05-09 22:34:33",
      "Site": "MASTER-OAFA",
      "Coord (J2000)": "(03h 18m 00.28s , -38d 23m 19.1s)",
      "Filt.": "C",
      "Expt.": 10,
      "Limit": 14.1,
      "Comment": ""
    },
    {
      "Tmid-T0": 104,
      "Date Time": "2025-05-09 22:35:03",
      "Site": "MASTER-OAFA",
      "Coord (J2000)": "(03h 18m 00.24s , -38d 23m 19.1s)",
      "Filt.": "C",
      "Expt.": 20,
      "Limit": 14.5,
      "Comment": ""
    },
    {
      "Tmid-T0": 138,
      "Date Time": "2025-05-09 22:35:42",
      "Site": "MASTER-OAFA",
      "Coord (J2000)": "(03h 18m 00.14s , -38d 23m 18.9s)",
      "Filt.": "C",
      "Expt.": 10,
      "Limit": 14.4,
      "Comment": ""
    },
    {
      "Tmid-T0": 174,
      "Date Time": "2025-05-09 22:36:18",
      "Site": "MASTER-OAFA",
      "Coord (J2000)": "(03h 18m 00.11s , -38d 23m 18.5s)",
      "Filt.": "C",
      "Expt.": 10,
      "Limit": 14.4,
      "Comment": ""
    },
    {
      "Tmid-T0": 215,
      "Date Time": "2025-05-09 22:36:53",
      "Site": "MASTER-OAFA",
      "Coord (J2000)": "(03h 18m 00.28s , -38d 23m 19.1s)",
      "Filt.": "C",
      "Expt.": 10,
      "Limit": 14.7,
      "Comment": ""
    },
    {
      "Tmid-T0": 2728,
      "Date Time": "2025-05-09 23:17:27",
      "Site": "MASTER-OAFA",
      "Coord (J2000)": "(03h 06m 26.66s , -38d 44m 06.7s)",
      "Filt.": "C",
      "Expt.": 180,
      "Limit": 18,
      "Comment": ""
    },
    {
      "Tmid-T0": 2914,
      "Date Time": "2025-05-09 23:20:33",
      "Site": "MASTER-OAFA",
      "Coord (J2000)": "(03h 06m 26.94s , -38d 44m 08.8s)",
      "Filt.": "C",
      "Expt.": 180,
      "Limit": 17.6,
      "Comment": ""
    },
    {
      "Tmid-T0": 3100,
      "Date Time": "2025-05-09 23:23:39",
      "Site": "MASTER-OAFA",
      "Coord (J2000)": "(03h 06m 27.22s , -38d 44m 12.4s)",
      "Filt.": "C",
      "Expt.": 180,
      "Limit": 17.4,
      "Comment": ""
    }
  ]
}

### 40457

{
  "redshift": null,
  "numeric_values": [
    {
      "alpha": 1.9,
      "fluence": null,
      "wavelengths": null,
      "energy": 40 - 6000,
      "errors": 0.7,
      "confidence levels": null,
      "durations": 1.9 +0.7/-0.7,
      "keVs": [40, 6000],
      "Date-time": "2025-05-11T00:52:17 UTC"
    }
  ],
  "table": null
}
### 40168
{
  "redshift": null,
  "numeric_values": {
    "alpha": null,
    "fluence": null,
    "wavelengths": null,
    "energy": [5, 8],
    "errors": null,
    "confidence levels": 90,
    "durations": 20.40,
    "keVs": null,
    "Date-time": "2025-04-19T02:29:32 UTC",
    "Coordinates (RA, DEC)": {
      "RA": "13h29m32.97s",
      "DEC": "7d05m09.92s"
    },
    "radius": 9.15
  },
  "table": null
}


###
Falcon takes time




### Hallucination
f"""
You are an information extractor.

Extract and return ONLY the following structured fields from the astronomy event description below, formatted as a **valid JSON object**.

Structure:
{{
  "numeric_values": {{
    "alpha": [...],
    "fluence": [...],
    "wavelengths": [...],
    "energy": [...],
    "errors": [...],
    "confidence_levels": [...],
    "durations": [...],
    "keV": [...],
    "datetime": [...],
    "coordinates": [...],
    "radius": [...],
    "redshift": [...]
  }},
  "table": [{{...}}] OR null // If any **markdown-style tables** are present, convert them to an array of objects
}}

Instructions:
- Return only the **final JSON** object. No preamble, no explanation, no Markdown formatting.
- If a value is not present, leave its value as an empty array (`[]`) or `null` for the table.

Text:
\"\"\"
{text}
\"\"\"
"""

"numeric_values": {
    "alpha": [],
    "fluence": [],
    "wavelengths": [],
    "energy": [],
    "errors": [],
    "confidence_levels": [],
    "durations": [],
    "keV": [],
    "datetime": ["2025-05-09 22:34:33", "2025-05-09 22:35:03", "2025-05-09 22:35:42", "2025-05-09 22:36:18", "2025-05-09 22:36:53", "2025-05-09 22:37:39", "2025-05-09 22:46:44", "2025-05-09 22:49:30", "2025-05-09 22:52:36", "2025-05-09 22:55:42", "2025-05-09 22:55:43", "2025-05-09 22:58:49", "2025-05-09 22:58:49", "2025-05-09 23:01:55", "2025-05-09 23:01:55", "2025-05-09 23:05:01", "2025-05-09 23:05:02", "2025-05-09 23:08:08", "2025-05-09 23:08:08", "2025-05-09 23:11:14", "2025-05-09 23:14:20", "2025-05-09 23:14:20", "2025-05-09 23:17:26", "2025-05-09 23:17:27", "2025-05-09 23:20:33", "2025-05-09 23:20:33", "2025-05-09 23:23:39", "2025-05-09 23:23:39"],
    "coordinates": [{"alpha": "03h 18m 00.28s", "delta": "-38d 23m 19.1s"}, {"alpha": "03h 18m 00.24s", "delta": "-38d 23m 19.1s"}, {"alpha": "03h 18m 00.14s", "delta": "-38d 23m 18.9s"}, {"alpha": "03h 18m 00.11s", "delta": "-38d 23m 18.5s"}, {"alpha": "03h 18m 00.10s", "delta": "-38d 23m 18.6s"}, {"alpha": "03h 18m 00.12s", "delta": "-38d 23m 19.3s"}, {"alpha": "03h 18m 00.32s", "delta": "-38d 23m 28.0s"}, {"alpha": "03h 18m 00.52s", "delta": "-38d 23m 31.2s"}, {"alpha": "03h 18m 00.73s", "delta": "-38d 23m 34.3s"}, {"alpha": "03h 18m 01.03s", "delta": "-38d 23m 38.0s"}, {"alpha": "03h 06m 24.43s", "delta": "-38d 43m 44.4s"}, {"alpha": "03h 18m 01.35s", "delta": "-38d 23m 42.3s"}, {"alpha": "03h 06m 24.67s", "delta": "-38d 43m 47.0s"}, {"alpha": "03h 18m 01.74s", "delta": "-38d 23m 46.7s"}, {"alpha": "03h 06m 24.96s", "delta": "-38d 43m 50.0s"}, {"alpha": "03h 18m 02.05s", "delta": "-38d 23m 50.9s"}, {"alpha": "03h 06m 25.27s", "delta": "-38d 43m 53.2s"}, {"alpha": "03h 18m 02.30s", "delta": "-38d 23m 55.2s"}, {"alpha": "03h 06m 25.58s", "delta": "-38d 43m 56.5s"}, {"alpha": "03h 06m 25.97s", "delta": "-38d 44m 00.1s"}, {"alpha": "03h 18m 02.98s", "delta": "-38d 24m 03.8s"}, {"alpha": "03h 06m 26.35s", "delta": "-38d 44m 03.6s"}, {"alpha": "03h 18m 03.37s", "delta": "-38d 24m 09.0s"}, {"alpha": "03h 06m 26.66s", "delta": "-38d 44m 06.7s"}, {"alpha": "03h 18m 03.73s", "delta": "-38d 24m 14.1s"}, {"alpha": "03h 06m 26.94s", "delta": "-38d 44m 08.8s"}, {"alpha": "03h 18m 04.07s", "delta": "-38d 24m 19.9s"}, {"alpha": "03h 06m 27.22s", "delta": "-38d 44m 12.4s"}],
    "site": []
  },
  "tables": [
    {

      
      ]



### Prompt
f"""
Extract the following structured fields from the given astronomy event description:

Extract **all numeric values** such as:
- alpha, fluence, wavelengths, energy, errors, uncertaininties, confidence levels, time durations, keV values, date-times, coordinates (RA, DEC), radius, redshift (z), etc.
- Each key describes the physical quantity (e.g., `"redshift"`, `"wavelengths"`).
- Each value is an object with two keys: "value" (the numeric value) and "unit" (the unit of the numeric value if any, use null if not present). 
- If there are multiple values for a quantity, use an array:
Example: `{{"redshift": [-2, -1], "wavelengths": [{{"value":200, "unit":"AA"}},{{"value":3000, "unit":"AA"}}]}}`

Return a single **JSON object**
If a section is not applicable or not found, use `null` for that key.

**Return only the complete JSON object. No explanations.**

Text:
\"\"\"
{text}
\"\"\"
"""
### Mathral: 
{'alpha': None, 'fluence': None, 'wavelengths': [{'value': 3600, 'unit': 'AA'}, {'value': 9600, 'unit': 'AA'}], 'energy': None, 'errors': None, 'uncertaininties': None, 'confidence levels': None, 'time durations': [10.99, 10.76], 'keV values': None, 'date-times': ['2025 April 4 at 02:15:01 UT', '2025 April 4 at 02:01:37 UT'], 'coordinates (RA, DEC)': None, 'radius': None, 'redshift (z)': [1.847], 'uncertain redshifts': [[1.763]]}


## Another good
### falcon3:7b
f"""
Extract the following structured fields from the given astronomy event description:

Extract all **relevant numeric values** into a flat JSON object. These include:
- redshift (z), fluence, wavelengths, energy, errors, uncertainties, 
- confidence levels, durations, keV values, date-times, coordinates (RA, DEC), radius, alpha, (any other physics related values) etc.
- Keys must be **clear physical quantities**.
- If multiple values exist for a key, use an array.
- If a value has a unit, store it as an object with `value` and `unit`.
- If a value doesnt exist, use `null`

**Output format Example:**
```json
{{
  "fluence": [{{"value": 2.8e-7, "unit": "erg/cm^2"}}],
  "duration": [1.2],
  "redshift": [1.1],
  "RA": ["03h 18m 00.28s"],
  "DEC": ["-38d 23m 19.1s"]
}}

**Return only the complete JSON object. No explanations.**

Text:
\"\"\"
{text}
\"\"\"
"""

```json
{
  "redshift": [
    {
      "value": 1.847,
      "unit": null
    },
    {
      "value": 1.763,
      "unit": null
    }
  ],
  "RA": ["03h 18m 00.28s"],
  "DEC": [
    {
      "value": "-38",
      "unit": "deg"
    },
    {
      "value": "23m 19.1s",
      "unit": "arcmin"
    }
  ],
  "duration": [2.0, 0.6],
  "fluence": null,
  "wavelengths": [
    {"value": 3300, "unit": "AA"},
    {"value": 9600, "unit": "AA"}
  ],
  "energy": null,
  "errors": null,
  "uncertainties": null,
  "confidence_levels": null,
  "date-times": [
    {
      "value": "2025 April 4 02:15:01 UT",
      "unit": null
    },
    {
      "value": "2025 April 4 02:01:37 UT",
      "unit": null
    }
  ],
  "coordinates": {
    "RA": "03h 18m 00.28s",
    "DEC": "-38d 23m 19.1s"
  },
  "radius": null,
  "alpha": null
}
```