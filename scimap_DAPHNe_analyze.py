import sys
import os
import anndata as ad
import pandas as pd
import scanpy as sc
import seaborn as sns; sns.set(color_codes=True)
import scimap as sm

os.chdir("/home/aus87/CyCIF/DAPHNe/")

print("Enter sample number: ")
samplenum = input()
mangatespath = 'gate_files/' + samplenum + '_manual_gates.csv'
manual_gate = pd.read_csv(mangatespath)
phenotype = pd.read_csv('phenotyping_workflow.csv')

#print("Enter .h5ad file: ")
inputfile = 'scimap/' + samplenum + '-trimmed.h5ad'
adata = ad.read(inputfile)

adata = sm.pp.rescale(adata, gate=manual_gate)
adata = sm.tl.phenotype_cells(adata, phenotype=phenotype, label="phenotype")

print(adata.obs['phenotype'].value_counts())

#print("Enter output directory: ")
outputdir = 'cell_types/' + samplenum + '/'

adata.write_csvs(outputdir, skip_data=True, sep=',')
