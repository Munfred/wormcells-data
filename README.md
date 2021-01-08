
#  A collection of all C. elegans single cell RNA sequencing data

This website aims to be a handy collection of all publicly available C. elegans single cell and single nucleus RNA sequencing data. In addition to listing studies and original data sources, for convenience a direct download link to the data in [.h5ad](https://anndata.readthedocs.io/en/latest/) format is provided. 

<font size="1" face="Arial" >
<table style="margin-left:auto;margin-right:auto;" class="tbl" cellspacing="0" cellpadding="0" >
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
<td> <a href="https://github.com/Munfred/wormcells-site/releases/download/bendavid2020/bendavid2020.h5ad"> 145MB </a> </td>
<td> L2 larvae</td>
<td> <a href="https://doi.org/10.1101/2020.08.23.263798">Whole-organism mapping of the genetics of gene expression at cellular resolution </a> biorxiv 2020.</td>
<td> - </td>
<td> Gene count matrix was kindly provided by the authors on request</td>
</tr>

<tr>
<td>Taylor 2020</td>
<td> 100,955 </td>
<td> 10x v2/v3</td>
<td> <a href="https://github.com/Munfred/wormcells-site/releases/download/taylor2020/taylor2020.h5ad"> 364MB </a> </td>
<td> L4 larvae neurons selected via flow cytometry </td>
<td> <a href="https://doi.org/10.1101/2020.12.15.422897">Molecular topography of an entire nervous system.</td>
<td> <a href="https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE136049">GSE136049</a> </td>
<td> <a href="https://cengen.org">CeNGEN website </a> 
<a href="http://cengen.shinyapps.io/SCeNGEA"> Shiny R app to explore the data </a>
</td>
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


## Taylor 2020 Neuron Dataset	

Taylor and friends. [Molecular topography of an entire nervous system](https://doi.org/10.1101/2020.12.15.422897). biorxiv 2019.

This is the second data release of the C. elegans Neuronal Gene Expression Map & Network (CeNGEN). The aim of the project is to establish a comprehensive gene expression atlas of an entire nervous system at single-neuron resolution, described in [the announcement publication](https://doi.org/10.1016/j.neuron.2018.07.042). Their website is [cengen.org](https://cengen.org).

The data matrix used used here was from the original unfiltered 10x matrices as outputted by cellranger, I kept the same barcodes they kept but skipped the soupX processing step as I don't think removing background from the matrix itself is a sensible thing. 

They used 10x Genomics v2 and v3 chemistry to profile 100,599 cells from L4 stage larvae, split as below. Their annotations define 133 cell types.

|dropbox_id|cell_types_targeted                                                  |experiment_code|strain                  |genotype                                                                                                                               |version10x|total_cells|
|----------|---------------------------------------------------------------------|---------------|------------------------|---------------------------------------------------------------------------------------------------------------------------------------|----------|-----------|
|1806-ST-1 |All neurons                                                          |Pan-1          |OH10689                 |otIs355 [rab-3p(prom1)::2xNLS::tagRFP] IV                                                                                              |v2        |642        |
|1806-ST-2 |All neurons                                                          |Pan-2          |OH10689                 |otIs355 [rab-3p(prom1)::2xNLS::tagRFP] IV                                                                                              |v2        |813        |
|2658-ST-1 |GABAergic neurons                                                    |unc-47_1       |NC3582                  |oxIs12 [unc-47p::GFP + lin-15(+)] X; otIs355 [rab-3p(prom1)::2xNLS::tagRFP] IV                                                         |v2        |185        |
|2966-ST-1 |GABAergic neurons                                                    |unc-47_2       |NC3582                  |oxIs12 [unc-47p::GFP + lin-15(+)] X; otIs355 [rab-3p(prom1)::2xNLS::tagRFP] IV                                                         |v2        |290        |
|3070-ST-1 |Motor circuit command interneurons                                   |nmr-1          |NC3572                  |akIs3 [nmr-1::GFP + lin-15(+)] V; otIs355 [rab-3p(prom1)::2x-NLS::tagRFP] IV                                                           |v2        |1371       |
|3131-ST-1 |Glutamatergic neurons                                                |eat-4          |OH9625                  |otIs292 [eat-4::mCherry + rol-6(su1006)]                                                                                               |v2        |417        |
|3183-ST-1 |Ventral cord motor neurons                                           |unc-3          |OH11746                 |pha-1(e2123) III; otIs447 [unc-3p::mCherry + pha-1(+)] IV                                                                              |v2        |724        |
|3239-ST-1 |Ciliated sensory neurons                                             |ift-20         |OH11157                 |pha-1(e2123) III; otIs393 [ift-20::NLS::tagRFP + pha-1(+)]                                                                             |v2        |490        |
|3441-ST-1 |Cholinergic neurons                                                  |cho-1_1        |NC3579                  |otIs354 [cho-1(fosmid)::SL2::YFP::H2B]; otIs355 [rab-3(prom1)::2xNLS-tagRFP] IV                                                        |v2        |507        |
|3441-ST-2 |Cholinergic neurons                                                  |cho-1_2        |NC3579                  |otIs354 [cho-1(fosmid)::SL2::YFP::H2B]; otIs355 [rab-3(prom1)::2xNLS-tagRFP] IV                                                        |v2        |455        |
|3465-ST-1 |Serotonergic neurons and AIY, RID, CAN                               |tph-1_ceh-10   |NC3580                  |zdIs13 [tph-1p::GFP] IV; hpIs202 [ceh-10p::GFP + lin-15(+)]                                                                            |v2        |547        |
|3495-ST-1 |Cholinergic ventral cord motor neurons                               |acr-2          |CZ631                   |juIs14 [acr-2p::GFP + lin-15(+)] IV                                                                                                    |v3        |12133      |
|3503-ST-1 |Pharyngeal neurons                                                   |ceh-34         |NC3583                  |stIs10447 [ceh-34p::HIS-24::mCherry + unc-119(+)]; evIs111 [F25B3.3::GFP + dpy-20(+)]                                                  |v3        |3345       |
|3697-ST-1 |unc-86 expressing cells                                              |unc-86         |CX5974                  |unc-86::myr-GFP + odr-1::RFP] IV                                                                                                       |v3        |3506       |
|3831-ST-1 |unc-53 expressing cells                                              |unc-53         |NC3636                  |hdIs1 [unc-53p::GFP + rol-6(su1006)]; otIs355 [rab-3prom1::2xNLS-tagRFP] IV                                                            |v3        |5141       |
|4138-ST-1 |PVT, nlp-13 expressing cells, I3, M3, NSM                            |nlp-13_ceh-2   |OH16007 + PS3504        |otIs742 [nlp-13p::GFP + lin-15(+)].  syIs54 [ceh-2::GFP + unc-119(+)]; unc-119 (ed4)                                                   |v3        |9024       |
|4170-ST-1 |M4, dopamine neurons, touch receptor neurons, O2-sensing neurons, SAB|ceh-28_dat-1   |nIs175 + NC3635 + NC3523|nIs175 [ceh-28p::4xNLS-GFP + lin-15(+)]. NC3635 egIs1 [dat-1p::GFP]; uIs152 [mec-3::RFP]; kyEx1162 [gcy-35p::GFP]. wdIs90 [unc-4c::GFP]|v3        |7370       |
