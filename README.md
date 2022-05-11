This program functions in a two-part pipeline.  
  
Part 1: scimap_DAPHNe_analyze.py  
This script imports DAPHNe sample through scimap.  
Prerequisites for unmicst.csv:  
- Trimmed to remove dropped cells  
- Removed extra cycles (i.e. Cycle 7, Cycle 8)  

The unmicst files should be placed in a directory called unmicst/ in the same parent as the script.  
The script saves .h5ad files in a directory called scimap/ in the same parent as the script. Create this directory prior to running.  
  
Part 2: scimap_DAPHNe_analyze.py  
This script takes the .h5ad saved from Part 1 and phenotypes the cells.  
Prerequisites:  
- Gating files should be log1p transformed and named in format "<samplenumber>_manual_gates.csv".  
- manual_gates.csv files are saved in a directory called gate_files/ in the same parent as the script.  
- phenotyping_workflow.csv is saved in the same parent as the script.  
- There is a directory called cell_types/ in the same parent as the script.  
- Within cell_types/, there should be a directory with the same name as each sample (e.g., cell_types/3-1/)  

The script will prompt the user for the sample number and then phenotype the cells, saving the output in the corresponding cell_types/ directory.  
The total number of each cell type will also be displayed in the console.  
