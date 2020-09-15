
#  A collection of all C. elegans single cell RNA sequencing data

This website aims to be a handy collection of all publicly available C. elegans single cell and single nucleus RNA sequencing data. In addition to listing studies and original data sources, for convenience a direct download link to the data in [.h5ad](https://anndata.readthedocs.io/en/latest/) format is provided. 

<font size="2" face="Arial" >
<table style="width:150%" class="tbl" cellspacing="0" cellpadding="0" >
<tr>
<th>Short Name</th>
<th>Total cells</th>
<th>Method</th>
<th>h5ad</th>
<th>Summary</th>
<th>Article/preprint</th>
<th> Original Data</th>
<th> Notes</th>
</tr>

<tr>
<td>Cao 2017</td>
<td> 35,987 </td>
<td> sci-RNA-seq</td>
<td> <a href="https://github.com/Munfred/wormcells-site/releases/download/cao2017/cao2017.h5ad"> 136MB </a> </td>
<td> L2 larvae</td>
<td> <a href="https://doi.org/10.1126/science.aam8940">A lineage-resolved molecular atlas of C. elegans embryogenesis at single-cell resolution </a> Science 2019.</td>
<td> <a href="https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE98561">GSE98561 </a> and <a href="https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM4318946">GSM4318946 (reprocessed)</a>  </td>
<td> GSM4318946 release was a reannotation of the data </td>
</tr>

<tr>
<td>Packer 2019</td>
<td> 89,701 </td>
<td> 10x v2</td>
<td> <a href="https://github.com/Munfred/wormcells-site/releases/download/packer2019/packer2019.h5ad"> 653MB </a> </td>
<td> Several timepoints of embryo development</td>
<td> <a href="https://science.sciencemag.org/content/365/6459/eaax1971.long">A lineage-resolved molecular atlas of C. elegans embryogenesis at single-cell resolution </a> Science 2019.</td>
<td> <a href="https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE126954">GSE126954</a> </td>
<td> <a href="https://cello.shinyapps.io/celegans/">VisCello app for data exploration </a> </td>
</tr>

<tr>
<td>Taylor 2019</td>
<td> 65,450 </td>
<td> 10x v2/v3</td>
<td> <a href="https://github.com/Munfred/wormcells-site/releases/download/taylor2019/taylor2019.h5ad"> 217MB </a> </td>
<td> L4 larvae neurons selected via flow cytometry </td>
<td> <a href="https://doi.org/10.1101/737577">Expression profiling of the mature C. elegans nervous system by single-cell RNA-Sequencing </a> biorxiv 2019.</td>
<td> <a href="https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE136049">GSE136049</a> </td>
<td> <a href="https://cengen.org">CeNGEN website </a> 
<a href="http://cengen.shinyapps.io/SCeNGEA"> Shiny R app to explore the data </a>
</td>
</tr>

<tr>
<td>Ben-David 2020</td>
<td> 55,508 </td>
<td> 10x v2</td>
<td> <a href="https://github.com/Munfred/wormcells-site/releases/download/bendavid2020.h5ad/bendavid2020.h5ad"> 145MB </a> </td>
<td> L2 larvae</td>
<td> <a href="https://doi.org/10.1101/2020.08.23.263798">Whole-organism mapping of the genetics of gene expression at cellular resolution </a> biorxiv 2020.</td>
<td> - </td>
<td> Gene count matrix was kindly provided by the authors on request</td>
</tr>

</table>
</font>
# About the data




## Cao 2017 L2 Larva Dataset (reprocessed)	
Cao and friends. [Comprehensive single-cell transcriptional profiling of a multicellular organism](https://doi.org/10.1126/science.aam8940). Science 2017.

This was the first scRNAseq C. elegans data to be published. The single cell matrices used here were a newer version that was reprocessed and re-annotated and kindly provided by Robert Waterston and colleagues.

The technology used was sci-RNA seq. Two experiments with C. elegans at the L2 larval stage were performed with labels and cell counts as below. Their annotations define 117 cell types.

| Experiment name | Cells |
|-----------------|-------|
| L2_experiment_1 | 35480 |
| L2_experiment_2 |   507 |



## Packer 2019 Embryogenesis Dataset				
Packer and friends. [A lineage-resolved molecular atlas of C. elegans embryogenesis at single-cell resolution](https://science.sciencemag.org/content/365/6459/eaax1971.long). Science 2019.

In the paper supplements, the way the age of the embryos was defined is described as follows:
>_Around 250,000 L1 larvae were 29 plated onto four 100 mm petri plates seeded with NA22 bacteria and allowed to develop at 20 30 °C. As the worms reached the young adult stage, the population was closely monitored. When 31 about 20-30% of the adults had a single embryo in either arm of the gonad, worms were 32 subjected to hypochlorite treatment. The time hypochlorite was added to the worms was 33 considered t = 0._ 

They used 10x Genomics v2 chemistry to profile 89,701 cells, split as below. Their annotations define 183 cell types. 

| Experiment name               | Cells | Description                                                    |
|-------------------------------|-------|----------------------------------------------------------------|
| Waterston_400_minutes         | 25875 | 400 minute synchronized embryos                                |
| Waterston_300_minutes         | 17168 | 300 minute synchronized embryos                                |
| Murray_b01                    | 12129 | mixed time point                                               |
| Waterston_500_minutes_batch_2 | 11589 | 500 minute synchronized embryos, replicate 1                   |
| Waterston_500_minutes_batch_1 | 10532 | 500 minute synchronized embryos, replicate 2                   |
| Murray_r17                    |  9363 | mixed time point                                               |
| Murray_b02                    |  3045 | mixed time point                                               |

<br>

## Taylor 2019 Neuron Dataset	

Taylor and friends. [Expression profiling of the mature C. elegans nervous system by single-cell RNA-Sequencing](https://www.biorxiv.org/content/10.1101/737577v2). biorxiv 2019.

This is the first data release of the C. elegans Neuronal Gene Expression Map & Network (CeNGEN). The aim of the project is to establish a comprehensive gene expression atlas of an entire nervous system at single-neuron resolution, described in [the announcement publication](https://doi.org/10.1016/j.neuron.2018.07.042). Their website is [cengen.org](https://cengen.org).

As described in their website: _We are performing 10x single-cell RNA-Seq on FACS-isolated neurons. Using 52,412 sequenced cells, 109/118 neuronal classes have been identified and computationally assigned to a cluster based on their gene expression fingerprint (93 confidently, 16 tentatively), and 9/118 classes have not been annotated yet._ 

They used 10x Genomics v2 and v3 chemistry to profile 65,450 cells from L4 stage larvae, split as below. Their annotations define 133 cell types.

| Experiment name | Cells | Strain  | Method | Cell Types Targeted                    |
|-----------------|-------|---------|--------|----------------------------------------|
| eat-4           | 12743 | OH9625  | 10xv2  | Glutamatergic neurons                  |
| acr-2           | 11719 | CZ631   | 10xv3  | Cholinergic ventral cord motor neurons |
| Pan             |  9216 | OH10689 | 10xv2  | All neurons                            |
| unc-3           |  6165 | OH11746 | 10xv2  | Ventral cord motor neurons             |
| tph-1_ceh-10    |  4810 | NC3580  | 10xv2  | Serotonergic neurons and AIY, RID, CAN |
| ift-20          |  4056 | OH11157 | 10xv2  | Ciliated sensory neurons               |
| cho-1_2         |  3849 | NC3579  | 10xv2  | Cholinergic neurons                    |
| cho-1_2         |  3471 | NC3579  | 10xv2  | Cholinergic neurons                    |
| unc-47_2        |  3123 | NC3582  | 10xv2  | GABAergic neurons                      |
| ceh-34          |  2648 | NC3583  | 10xv3  | Pharyngeal neurons                     |
| nmr-1           |  2389 | NC3572  | 10xv2  | Motor circuit command interneurons     |
| unc-47_1        |  1261 | NC3582  | 10xv2  | GABAergic neurons                      |


## Ben-David 2020 L2 dataset

Ben-David and friends. [Whole-organism mapping of the genetics of gene expression at cellular resolution](https://doi.org/10.1101/2020.08.23.263798) biorxiv 2020. 

In this dataset 5 separate 10x v2 lanes were run with about 10,000 L2 cells on each, each batch is a replicate. Their annotations define 99 cell types.

| Experiment name | Cells |
|-----------------|-------|
| F4_5            | 11633 |
| F4_4            | 11464 |
| F4_2            | 11424 |
| F4_1            | 11336 |
| F4_3            |  9651 |