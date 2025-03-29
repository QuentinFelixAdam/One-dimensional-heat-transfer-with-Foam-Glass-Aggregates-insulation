# One-dimensional-heat-transfer-with-Foam-Glass-Aggregates-insulation
Provided here is a Fortran90 code to calculate the maximal frost front penetration within a domain representing an asphalt concrete pavement insulated with FGA.

The Fortran90 code takes as input the files:  - "Indices_de_gel.dat" --> it contains a list of freezing indexes covering the entire province of Québec, Canada.
                                    - "para.dat" --> it contains relevant parameters required to perform calculations
                                    - "Temp_amp.dat" --> it contains the temperature amplitudes utilized to construct the top boundary condition
                                    - "Temp_moyenne.dat" --> it contains the temperature averahes utilized to construct the top boundary condition
                                    
The Fortran90 code produces as output Tdepth.XX.dat files, which can be treated with the Python code "Treat files.py". This code takes as input all TdepthXX.dat files and generates a "Summary.dat" file. "Summary.dat" contains the maximal frost front penetration depth.

To launch the Fortran90 code, place all the input files and "temp_updated_structure.f90" within the same folder. Open a terminal, navigate to the folder, and type "gfortran -o exe temp_updated_structure.f90", wait for the compilation (less than a second) and then type "exe".

To run the Python code, make sure you change appropriately the path folder.

You can modify some parameters such as the layers thicknesses, total volumetric water contents, etc. The values which can be modified are within the file "temp_updated_structure.f90" between line 216 and 244. 

This code is linked to a manuscript which is published. When using this code, please cite the manuscript in the following link: https://www.sciencedirect.com/science/article/pii/S0950061823045622.

Citation is as follows:

"Quentin Félix Adam, Pauline Segui, Jean Côté, Jean-Pascal Bilodeau, Guy Doré,
Thermal insulation of flexible pavements utilizing foam glass aggregates to mitigate frost action in cold regions — Development of design tools,
Construction and Building Materials,
Volume 414,
2024,
134841,
ISSN 0950-0618,
https://doi.org/10.1016/j.conbuildmat.2023.134841."
                                    
Fortran90 compiler : gfortran (GNU Fortran GCC version 12.2.0) obtained on http://www.equation.com/servlet/equation.cmd?fa=fortran
Python version 3.11.0
