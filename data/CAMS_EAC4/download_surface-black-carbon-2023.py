"""Download 2023 black-carbon surface concentrations from CAMS - EAC4.

Copyright (c) 2025-now, Institut des Géosciences de l'Environnement
(IGE, UMR 5001), Grenoble, France.

This software is released under the terms of the so-called BSD 3-clause
license. The full text of this license can be found in the LICENSE file or at
https://directory.fsf.org/wiki/License:BSD-3-Clause.

"""

import cdsapi

dataset = "cams-global-reanalysis-eac4"
request = {
    "variable": ["hydrophilic_black_carbon_aerosol_mixing_ratio",
                 "hydrophobic_black_carbon_aerosol_mixing_ratio"],
    "model_level": ["60"],
    "date": ["2023-01-01/2023-12-31"],
    "time": ["00:00", "03:00", "06:00", "09:00",
             "12:00", "15:00", "18:00", "21:00"],
    "data_format": "netcdf_zip"
}

client = cdsapi.Client()
client.retrieve(dataset, request).download(__file__[:-3] + ".zip")
