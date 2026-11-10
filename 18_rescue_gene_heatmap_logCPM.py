#!/usr/bin/env python3

'''
python3 18_rescue_gene_heatmap_logCPM.py --logCPM 05_DEGs/rescue_genes.csv
'''

####################
## Import Modules ##
####################

import argparse
import os
import polars as pl
import pandas as pd
import math
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import re
import sys
import scipy.cluster.hierarchy as sch
from scipy.spatial.distance import pdist
from plotnine import *

#####################
## Set Up Argparse ##
#####################

# Initialize argparse
parser = argparse.ArgumentParser(
    description = 'Generate heatmaps from RNA-seq DEG data')

# Required arguments
parser.add_argument('--logCPM', required=True, type=str,
    metavar='<str>', help='Matrix containing logCPM values for genes and samples')

# Finalize arguments
arg = parser.parse_args()

#########################
## Read in logCPM Data ##
#########################

count_file = arg.logCPM
df = pl.read_csv(count_file, separator=',', has_header=True)

# First column is gene names; remaining columns are samples
gene_col = df.columns[0]
sample_cols = df.columns[1:]

# Cast sample columns to Float64
for col in sample_cols:
    df = df.with_columns(pl.col(col).cast(pl.Float64))

# Convert to pandas, keeping original row/column order
data = df.to_pandas().set_index(gene_col)

# Preserve gene order and sample order explicitly
gene_order = data.index.tolist()
sample_order = data.columns.tolist()

print(f'Genes ({len(gene_order)}): {gene_order}')
print(f'Samples ({len(sample_order)}): {sample_order}')

if data.shape[0] == 0 or data.shape[1] == 0:
    print("No genes or samples found. Check input file.")
    sys.exit(1)

# Clean non-finite values
data = data.fillna(0).replace([np.inf, -np.inf], 0)

#######################
## Clustered Heatmap ##
#######################

print('Generating logCPM heatmap...')

plot_df = (
    data
    .reset_index()
    .melt(id_vars=gene_col, var_name='sample', value_name='logcpm')
)

# Enforce original ordering (no sorting)
plot_df[gene_col] = pd.Categorical(
    plot_df[gene_col], categories=gene_order[::-1], ordered=True
)
plot_df['sample'] = pd.Categorical(
    plot_df['sample'], categories=sample_order, ordered=True
)

vmax = np.nanmax(np.abs(data.values))
fill_scale = scale_fill_gradient2(
    low='#3b4cc0', mid='white', high='#b40426',
    midpoint=0, limits=(-vmax, vmax),
    name='log(CPM)'
)

p = (
    ggplot(plot_df, aes(x='sample', y=gene_col, fill='logcpm'))
    + geom_tile(color='black', size=0.3)
    + fill_scale
    + labs(
        x='', y='',
        title='Rescue Gene Expression (logCPM)'
    )
    + theme_minimal()
    + theme(
        axis_text_x=element_text(angle=0, hjust=0.5, vjust=1, size=5, color="black"),
        axis_text_y=element_text(size=5, color="black"),
        panel_grid_major=element_blank(),
        panel_grid_minor=element_blank(),
        figure_size=(10, 8),
        plot_margin=0.03,
    )
)

os.makedirs('00_FIGURES', exist_ok=True)
p.save(
    '00_FIGURES/rescue_genes_logCPM_heatmap.pdf',
    dpi=600, width=6, height=12, verbose=False
)