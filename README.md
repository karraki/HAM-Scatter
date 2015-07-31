## Halo Abundance Matching with Scatter (HAM-Scatter)

This code examines how scatter impacts Halo Abundance Matching techniques. Specifically, it is used to look at the low mass end of galaxy formation to better understand dwarf galaxies.

How to run this code: `$ python plot.py`

Soft code requirements: `mcconnachie.dat`

This is observational data of dwarf galaxies from [McConnachie, A. W., 2012, AJ, 144, 4](http://iopscience.iop.org/1538-3881/144/1/4/)
This is not my data and is therefore not distributed within this repository.
The data can be found at: [http://vizier.cfa.harvard.edu/viz-bin/VizieR?-source=J/AJ/144/4](http://vizier.cfa.harvard.edu/viz-bin/VizieR?-source=J/AJ/144/4)

Download the data, name it `mcconnachie.dat`, and place it in the directory you will run the code from.

Code outputs:

- ASCII data file of masses including scatter `estimated_mstar.txt`
- PDF multipage plot `HaloMassFunctions.pdf`

Code written by Kenza Arraki
Code distributed under MIT license
