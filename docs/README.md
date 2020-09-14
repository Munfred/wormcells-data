# Visit [de.wormcells.com](https://de.wormcells.com) to explore gene expression on C. elegans single cell RNA sequencing data

<br>
<br>


| Header 1  | Another header here | This is a long header |
| --------  | ------------------- | --------------------- |
| Some data | Some more data      | [A lineage-resolved molecular atlas of C. elegans embryogenesis at single-cell resolution](https://science.sciencemag.org/content/365/6459/eaax1971.long)                | 
| data      | Some long data here | more data             | 

## `wormcells-de` Exploring C. elegans single cell RNA sequencing data  

The `wormcells-de` app allows you to perform differential expression on data from C. elegans single cell RNA sequencing (scRNAseq). 21 experiments from 3 different studies were integrated and can be compared. That means you can select cells from two different experiments and perform differential expression on them!

Just select cell types and experiments to compare, some genes to highlight in your volcano plot, and leave your email. Results should arrive in less than 15 minutes. If they take more than an hour, something broke, so let me know by writing to eduardo@wormbase.org. Also feel free to write me if you have any feedback.

Just select cell types and experiments to compare, some genes to highlight in your volcano plot, and leave
    your email. You will receive an [interactive volcano plot](https://scvi-differential-expression.s3.us-east-2.amazonaws.com/plots/eduardo%40wormbase.org%4020200227-233946-results.html), a
    [csv file with results](https://scvi-differential-expression.s3.us-east-2.amazonaws.com/csv/eduardo%40wormbase.org%4020200227-233946-results.csv) and [a csv file with the selected groups and genes](https://scvi-differential-expression.s3.us-east-2.amazonaws.com/submissions/eduardo%40wormbase.org%2520200227-233946.csv").
        The example files linked show the result of the example submission below

The single cell gene count matrixes were processed using a machine learning framework called [Single-cell Variational Inference (scVI)](https://github.com/YosefLab/scVI). The scVI framework enables integrating data from different sources (different experiments, batches and technologies), clustering and label transfer, and performing differential expression between clusters.

To learn how the plots were made, check out [this Jupyter notebook](https://colab.research.google.com/drive/1hF7KSujhhHcyxzWkzAHy9lazXLexainr) which performs differential expression as is here here. It runs on Google Colab so you can start playing right away.

The `wormcells-de` app is still in development and on this tool will inform how WormBase may incorporate and display single cell data in the future. 


<br>
<br>
<br>

# About the data

The 21 experiments come from 3 different studies and are described below. To perform a comparison, you must choose two groups. Each group can have any number of pairs (`cell_type`, `experiment`) to be compared.

The experiments are described below, and a full table of how many cells of each type were seen in each experiment [can be accessed here](https://docs.google.com/spreadsheets/d/1xm0D-gqN8uMkmTYBjl-VJftCbB6NOkoX1C2RLreGsfY/edit?usp=sharing). Note that sometimes experiments used slightly different labels for the same cell type, which is why there might be repetition. This table provides the original study annotations. In the future we might re-annotate the data with harmonized labels. 

<br>
## Cao 2017 L2 Larva Dataset (reprocessed)	
Cao and friends. [Comprehensive single-cell transcriptional profiling of a multicellular organism](https://doi.org/10.1126/science.aam8940). Science 2017.

This was the first scRNAseq C. elegans data to be published. The single cell matrices used here were a newer version that was reprocessed and re-annotated and kindly provided by Robert Waterston and colleagues.

The technology used was sci-RNA seq. Two experiments with C. elegans at the L2 larval stage were performed with labels and cell counts as below. Their annotations define 117 cell types.


    L2_experiment_1    35480
    L2_experiment_2      507

<br>
## Packer 2019 Embryogenesis Dataset				
Packer and friends. [A lineage-resolved molecular atlas of C. elegans embryogenesis at single-cell resolution](https://science.sciencemag.org/content/365/6459/eaax1971.long). Science 2019.

In the paper supplements, the way the age of the embryos was defined is described as follows:
>_Around 250,000 L1 larvae were 29 plated onto four 100 mm petri plates seeded with NA22 bacteria and allowed to develop at 20 30 °C. As the worms reached the young adult stage, the population was closely monitored. When 31 about 20-30% of the adults had a single embryo in either arm of the gonad, worms were 32 subjected to hypochlorite treatment. The time hypochlorite was added to the worms was 33 considered t = 0._ 

They used 10x Genomics v2 chemistry to profile 89,701 cells, split as below. Their annotations define 183 cell types. 


    Waterston_400_minutes            25875		# 400 minute synchronized embryos
    Waterston_300_minutes            17168		# 300 minute synchronized embryos
    Murray_b01                       12129		# mixed time point. Unclear description of sample from the paper
    Waterston_500_minutes_batch_2    11589		# 500 minute synchronized embryos, replicate 1
    Waterston_500_minutes_batch_1    10532		# 500 minute synchronized embryos, replicate 2
    Murray_r17                        9363		# mixed time point. Unclear description of sample from the paper
    Murray_b02                        3045		# mixed time point. Unclear description of sample from the paper

<br>
## Taylor 2019 Neuron Dataset	
Taylor and friends. [Expression profiling of the mature C. elegans nervous system by single-cell RNA-Sequencing](https://www.biorxiv.org/content/10.1101/737577v2). biorxiv 2019.

This is the first data release of the C. elegans Neuronal Gene Expression Map & Network (CeNGEN). The aim of the project is to establish a comprehensive gene expression atlas of an entire nervous system at single-neuron resolution, described in [the announcement publication](https://doi.org/10.1016/j.neuron.2018.07.042). Their website is [cengen.org](https://cengen.org).

As described in their website: _We are performing 10x single-cell RNA-Seq on FACS-isolated neurons. Using 52,412 sequenced cells, 109/118 neuronal classes have been identified and computationally assigned to a cluster based on their gene expression fingerprint (93 confidently, 16 tentatively), and 9/118 classes have not been annotated yet._ 

They used 10x Genomics v2 chemistry to profile 65,450 cells from L4 stage larvae, split as below. Their annotations define 133 cell types. 

    eat-4                            12743		# pan-glutamate neurons from strain OH9625
    acr-2                            11719		# cholinergic MN from strain CZ631
    Pan                               9216		# neurons from pan-neural marker strain otIs355
    unc-3                             6165		# strain OH11746
    tph-1_ceh-10                      4810		# strain NC3580 and NC3580
    ift-20                            4056		# pan sensory neurons from strain OH11157
    cho-1_1                           3849		# pan-cholinergic 1 from strain OH13470
    cho-1_2                           3471		# pan-cholinergic 2 from strain OH13470
    unc-47_2                          3123		# pan-GABA 2 from strain EG1285 and NC3582
    ceh-34                            2648		# strains RW10754 and NC3583
    nmr-1                             2389		# strains VM484 and NC3572
    unc-47_1                          1261		# pan-GABA 1 from strain EG1285 and NC3582


### The previous prototype dashboard is still accessible.
### Visit [dash.wormcells.com](http://dash.wormcells.com) to explore the Packer 2019 dataset.
