This website aims to be a handy collection of all publicly available C. elegans single cell and single nucleus RNA sequencing data. In addition to listing studies and the original data sources, for convenience the data has been repackaged and a direct download link to the data in [.h5ad](https://anndata.readthedocs.io/en/latest/) format is provided. The GitHub repository of this website is [https://github.com/munfred/wormcells-data](https://github.com/munfred/wormcells-data), and the .h5ad files are hosted on the repository's [releases page](https://github.com/Munfred/wormcells-data/releases).

The .h5ad files provided here with the annotations from different studies the here can be readily used to perform differential expression between cell types of interest using a tutorial notebook written to be run on Google Colab. Click the button below to open a notebook and run it. 

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Munfred/scdefg/blob/main/scdefg.ipynb)


It loads an example C. elegans dataset with 100k cells and 169 cell types with data from the data from the CeNGEN project published by [Taylor et al 2020](https://doi.org/10.1016/j.neuron.2018.07.042), and spins up a simple app for using a table like interface for performing differential expression. The code for the app is available at [https://github.com/munfred/scdefg](https://github.com/munfred/scdefg)



<font size="1" face="Arial">
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
<td> <a href="https://doi.org/10.1101/2020.12.15.422897">Molecular topography of an entire nervous system. </a> </td>
<td> <a href="https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE136049">GSE136049</a> </td>
<td> <a href="https://cengen.org">CeNGEN website </a> 
<a href="http://cengen.shinyapps.io/SCeNGEA"> Shiny R app to explore the data </a>
</td>
</tr>
