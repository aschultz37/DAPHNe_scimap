#First part of pipeline
#Imports unmicst file and writes to .h5ad file
import sys
import os
from pathlib import Path
import anndata as ad
import pandas as pd
import scanpy as sc
import seaborn as sns; sns.set(color_codes=True)
import scimap as sm

unmicstdir = '/home/aus87/CyCIF/DAPHNe/unmicst'
ofdir = '/home/aus87/CyCIF/DAPHNe/scimap'
os.chdir("/home/aus87/CyCIF/DAPHNe/")

for filename in os.listdir(unmicstdir):
    f = os.path.join(unmicstdir, filename)
    #if is a file, perform analysis and save
    if os.path.isfile(f):
        #import unmicst file w/ scimap helper function
        image_path = f
        adata = sm.pp.mcmicro_to_scimap (image_path, drop_markers = ["AntiRabbit", "AntiMouse", "AntiRat"])
        #perform PCA
        sc.tl.pca(adata, svd_solver='arpack')
        #save data to file
        ofname = Path(filename).stem + ".h5ad"
        ofpath = os.path.join(ofdir, ofname)
        adata.write(ofpath)
