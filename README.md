# Transient delivery of CRISPR epigenome editors enables durable silencing of HTT in Huntington's disease models

## Citation

TBD

## Raw Data

All raw data associated with the study can be found under GEO Accession Number **GSE355213**.

| SRA ID | Sample Name | Genotype | Treatment | Group | Replicate | Tissue Type | Batch |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| SRX36252170 | MUT_Guide6_1 | MUT | Guide6 | MUT_Guide6 | 1 | Cortical Organoid | 0 |
| SRX36252169 | MUT_Guide6_2 | MUT | Guide6 | MUT_Guide6 | 2 | Cortical Organoid | 0 |
| SRX36252168 | MUT_Guide6_3 | MUT | Guide6 | MUT_Guide6 | 3 | Cortical Organoid | 0 |
| SRX36252167 | MUT_NonEffector_1 | MUT | NonEffector | MUT_NonEffector | 1 | Cortical Organoid | 1 |
| SRX36252166 | MUT_NonEffector_2 | MUT | NonEffector | MUT_NonEffector | 2 | Cortical Organoid | 1 |
| SRX36252177 | MUT_NonEffector_3 | MUT | NonEffector | MUT_NonEffector | 3 | Cortical Organoid | 1 |
| SRX36252176 | MUT_NT_1 | MUT | NT | MUT_NT | 1 | Cortical Organoid | 1 |
| SRX36252175 | MUT_NT_2 | MUT | NT | MUT_NT | 2 | Cortical Organoid | 1 |
| SRX36252174 | MUT_NT_3 | MUT | NT | MUT_NT | 3 | Cortical Organoid | 1 |
| SRX36252173 | WT_NT_1 | WT | NT | WT_NT | 1 | Cortical Organoid | 1 |
| SRX36252172 | WT_NT_2 | WT | NT | WT_NT | 2 | Cortical Organoid | 1 |
| SRX36252171 | WT_NT_3 | WT | NT | WT_NT | 3 | Cortical Organoid | 1 |

Note that all numerical labels preceding scripts and directories are reflective of the order that things were run. Some directories are not in the GitHub repository due to the fact that those directories contained sequence data that are inappropriate to host on GitHub. However, you can access all the raw data using the information above and associated scripts in this repository.

## 1. Processing Raw Data

Sample configurations were stored in [`samples.yaml`](https://github.com/vhaghani26/Fink_Ankita_RNAseq_2026/blob/main/samples.yaml) and processed via the [`Snakefile`](https://github.com/vhaghani26/Fink_Ankita_RNAseq_2026/blob/main/Snakefile), which executed:

1. Downloading and indexing the hg38 genome and GTF annotation
2. Trimming raw reads with Trim Galore
3. Aligning reads to hg38 using STAR (outputting gene counts)
4. Indexing BAM files with Samtools
5. Quality control for all raw and processed data using MultiQC

## 2. DEG Analysis

Gene count files were read in using [`05.1_assign_gene_names.py`](https://github.com/vhaghani26/Fink_Ankita_RNAseq_2026/blob/main/05.1_assign_gene_names.py) to convert Ensembl IDs to HUGO nomenclature. Differentially expressed genes (DEGs) were identified using [`05.2_DEG_Analysis.ipynb`](https://github.com/vhaghani26/Fink_Ankita_RNAseq_2026/blob/main/05.2_DEG_Analysis.ipynb). Gene Ontology (GO) enrichment was performed using [`09_DEG_GO.ipynb`](https://github.com/vhaghani26/Fink_Ankita_RNAseq_2026/blob/main/09_DEG_GO.ipynb).

## 3. Visualization of Results

Multiple visualization techniques were used. Below are the scripts for different types of plots/visualizations and further analyses:

- [`06_Bar_Plots.ipynb`](https://github.com/vhaghani26/Fink_Ankita_RNAseq_2026/blob/main/06_Bar_Plots.ipynb): Bar plots of expression/DEG results
- [`07_Upset_Plot.ipynb`](https://github.com/vhaghani26/Fink_Ankita_RNAseq_2026/blob/main/07_Upset_Plot.ipynb): UpSet plot of overlapping DEG sets across comparisons
- [`08_Volcano_Plots.ipynb`](https://github.com/vhaghani26/Fink_Ankita_RNAseq_2026/blob/main/08_Volcano_Plots.ipynb): Volcano plots of differential expression results
- [`10_DEG_GO_Dot_Plots.ipynb`](https://github.com/vhaghani26/Fink_Ankita_RNAseq_2026/blob/main/10_DEG_GO_Dot_Plots.ipynb): GO term dot plots for DEGs
- [`11_heatmaps.py`](https://github.com/vhaghani26/Fink_Ankita_RNAseq_2026/blob/main/11_heatmaps.py): Heatmaps with clustering
- [`12_Identify_Rescue_Genes.ipynb`](https://github.com/vhaghani26/Fink_Ankita_RNAseq_2026/blob/main/12_Identify_Rescue_Genes.ipynb): Identification of rescue genes
- [`13_HD_Signatures_GO.ipynb`](https://github.com/vhaghani26/Fink_Ankita_RNAseq_2026/blob/main/13_HD_Signatures_GO.ipynb): GO analysis of HD disease signatures
- [`14_RNAseq_Disease_Signatures_GO.ipynb`](https://github.com/vhaghani26/Fink_Ankita_RNAseq_2026/blob/main/14_RNAseq_Disease_Signatures_GO.ipynb): GO analysis of RNAseq disease signatures
- [`15_Global_Transcriptome.ipynb`](https://github.com/vhaghani26/Fink_Ankita_RNAseq_2026/blob/main/15_Global_Transcriptome.ipynb): Global transcriptome visualization
- [`16_HD_Signatures_Custom_GO_DotPlot.ipynb`](https://github.com/vhaghani26/Fink_Ankita_RNAseq_2026/blob/main/16_HD_Signatures_Custom_GO_DotPlot.ipynb): Custom GO dot plots for HD signatures
- [`17_Rescue_Gene_GO_BP.ipynb`](https://github.com/vhaghani26/Fink_Ankita_RNAseq_2026/blob/main/17_Rescue_Gene_GO_BP.ipynb): GO biological process dot plots for rescue genes
- [`18_rescue_gene_heatmap_logCPM.py`](https://github.com/vhaghani26/Fink_Ankita_RNAseq_2026/blob/main/18_rescue_gene_heatmap_logCPM.py): logCPM heatmap for rescue genes

## Software Information

All environments and associated software versions are delineated below:

- [Data Processing and Alignment](https://github.com/vhaghani26/Fink_Ankita_RNAseq_2026/blob/main/ngs_tools.yml)
- [RNA-seq Analysis, Visualization, and Plotting](https://github.com/vhaghani26/Fink_Ankita_RNAseq_2026/blob/main/jupyter_nb_R4.4.2.yml)
