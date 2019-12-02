# wormcells

Visit [dash.wormcells.com/](http://dash.wormcells.com/) to see it live. 

## Exploring C. elegans single cell data  

This dashboard is a demonstration of how C. elegans single cell RNA sequencing data can be visualized. 

The 89,701 cells shown here comes from the article [A lineage-resolved molecular atlas of C. elegans embryogenesis at single-cell resolution](https://science.sciencemag.org/content/365/6459/eaax1971.long) (Packer et al, Science 2019).

For this demonstration the original data available on [GEO126954](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE126954) was processed using a machine learning framework called [Single-cell Variational Inference (scVI)](https://github.com/YosefLab/scVI). The scVI framework enables integrating data from different sources (different experiments, batches and technologies), clustering and label transfer, and performing differential expression between clusters.

To learn how the plots were made, check out [this Jupyter notebook](https://colab.research.google.com/drive/1hF7KSujhhHcyxzWkzAHy9lazXLexainr) which creates the plots shown here. It runs on Google Colab so you can start playing right away.

Feedback on this and other explorations will inform how [WormBase](https://wormbase.org/) may incorporate and display single cell data in the future. If you have any suggestions or comments, please create an issue on the GitHub repo at [https://github.com/Munfred/wormcells/issues](https://github.com/Munfred/wormcells/issues). 

This dashboard and the interactive plots were created using [Plotly Dash](https://dash.plot.ly/introduction) and developed with the online IDE [repl.it](https://repl.it/~). 
