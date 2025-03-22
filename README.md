# Hipparcos Planetarium Data Creator

This is a simple Python script that creates a JSON file with the data of the stars in the Hipparcos catalog. The data is obtained from the [Hipparcos catalog](http://cdsarc.u-strasbg.fr/viz-bin/Cat?I/239) and the [Bright Star Catalog](http://cdsarc.u-strasbg.fr/viz-bin/Cat?V/50).

## Prerequisites

Before running the scripts, you need to download the Stellarium sky culture data:

1. Visit the [Stellarium GitHub repository](https://github.com/Stellarium/stellarium)
2. Navigate to `skycultures/modern/index.json`
3. Download this file and save it to the root directory of this project
4. Alternatively, you can use wget or curl:

```bash
   curl -o index.json https://raw.githubusercontent.com/Stellarium/stellarium/master/skycultures/modern/index.json
``````

This step is necessary to respect the copyright of the Stellarium project, which is licensed under GPL.

# Install dependencies

```bash
pip install astroquery pandas
```

# Usage

```bash
python create_hip_lite_major.py
python create_hip_constellation_line.py
python create_hip_constellation_line_star.py
```

# License
This project is licensed under the GNU General Public License v2.0 (GPLv2) - see the LICENSE file for details.
The data from the Hipparcos catalog is based on public domain data from the ESA Hipparcos mission.
Constellation data derived from Stellarium is used under the terms of the GPLv2 license, consistent with Stellarium's licensing.

# Acknowledgements

- Stellarium for the constellation line data
- VizieR/CDS for hosting the astronomical catalogs

