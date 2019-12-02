import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import numpy as np
# import plot_embedding
import anndata

# here's a hack to randomize categorical colors, since plotly can't do that in a straightforward manner
# we take the list of named css colors that it recognizes, and we picked a color based on the code of
# the cluster we are coloring
css_colors=[
'aliceblue','antiquewhite','aqua','aquamarine','azure','bisque','black','blanchedalmond','blue',
'blueviolet','brown','burlywood','cadetblue','chartreuse','chocolate','coral','cornflowerblue',
'crimson','cyan','darkblue','darkcyan','darkgoldenrod','darkgray','darkgrey','darkgreen','darkkhaki',
'darkmagenta','darkolivegreen','darkorange','darkorchid','darkred','darksalmon','darkseagreen',
'darkslateblue','darkslategray','darkslategrey','darkturquoise','darkviolet','deeppink','deepskyblue',
'dimgray','dimgrey','dodgerblue','firebrick','floralwhite','forestgreen','fuchsia','gainsboro','ghostwhite',
'gold','goldenrod','gray','grey','green','greenyellow','honeydew','hotpink','indianred','indigo',
'ivory','khaki','lavender','lavenderblush','lawngreen','lemonchiffon','lightblue','lightcoral','lightcyan',
'lightgoldenrodyellow','lightgray','lightgrey','lightgreen','lightpink','lightsalmon','lightseagreen',
'lightskyblue','lightslategray','lightslategrey','lightsteelblue','lightyellow','lime','limegreen','linen',
'magenta','maroon','mediumaquamarine','mediumblue','mediumorchid','mediumpurple','mediumseagreen',
'mediumslateblue','mediumspringgreen','mediumturquoise','mediumvioletred','midnightblue','mintcream',
'mistyrose','moccasin','navajowhite','navy','oldlace','olive','olivedrab','orange','orangered','orchid',
'palegoldenrod','palegreen','paleturquoise','palevioletred','papayawhip','peachpuff','peru','pink','plum'
,'powderblue','purple','red','rosybrown','royalblue','saddlebrown','salmon','sandybrown','seagreen',
'seashell','sienna','silver','skyblue','slateblue','slategray','slategrey','snow','springgreen','steelblue',
'tan','teal','thistle','tomato','turquoise','violet','wheat','white','whitesmoke','yellow','yellowgreen']

# we just repeat the list of colors a bunch of times to ensure we always have more colors than clusters
css_colors = css_colors*100

categorial_features = {
'cell_type':'Cell Type',
'cell_subtype':'Cell Subtype',
'time_point': 'Time Point',
'batch':'Batch',
'plot_cell_type':'Cell type/subtype',
'embryo_time_bin':'Embryo time bin',
'raw_embryo_time_bin':'Raw embryo time bin',
'lineage':'Lineage'
}

cells = pd.read_csv(
                  'short_annotations25k.csv',
                  # 'packer_annotations_tsne_umap_coords.csv', 
                   index_col=0,
                   dtype={feature:'category' for feature in categorial_features.keys()})

top_expression = anndata.read('top10_expression_bayes_allgenes.h5ad')
top_expression.var['gene_description_html'] = top_expression.var['gene_description'].str.replace('\. ', '.<br>')
gene_description_text_matrix = np.tile((top_expression.var['gene_id'] + '<br>' + top_expression.var['gene_description_html']).values,
                                       (len(top_expression.obs['cell_type_name']),1) )

genes = pd.read_csv('gene_ids_names_descriptions_20222.csv', index_col=0)
genes['gene_description_html'] = genes['gene_description'].str.replace('\. ', '.<br>')
cell_types_summary = pd.read_csv('packer_cell_types_summary.csv')

cell_types_list=['nan',
'Body_wall_muscle',
'Hypodermis',
'Ciliated_amphid_neuron',
'Ciliated_non_amphid_neuron',
'Seam_cell',
'Pharyngeal_muscle',
'Glia',
'Intestine',
'Pharyngeal_neuron',
'Pharyngeal_marginal_cell',
'Coelomocyte',
'Pharyngeal_gland',
'GLR',
'Intestinal_and_rectal_muscle',
'Germline',
'Pharyngeal_intestinal_valve',
'Arcade_cell',
'Z1_Z4',
'Rectal_cell',
'M_cell',
'ABarpaaa_lineage',
'Rectal_gland',
'Excretory_cell',
'Excretory_gland',
'hmc',
'hmc_homolog',
'T',
'hmc_and_homolog',
'Parent_of_exc_gland_AVK',
'hyp1V_and_ant_arc_V',
'Excretory_duct_and_pore',
'Parent_of_hyp1V_and_ant_arc_V',
'G2_and_W_blasts',
'Excretory_cell_parent',
'Parent_of_exc_duct_pore_DB_1_3',
'XXX']

external_stylesheets = ['https://codepen.io/chriddyp/pen/dZVMbK.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

################### TSNEEEEEE ###########
app.layout = html.Div([
  html.Div([
dcc.Markdown('''

# Exploring C. elegans single cell data  

This dashboard is a demonstration of how C. elegans single cell RNA sequencing data can be visualized. 

The 89,701 cells shown here comes from the article [A lineage-resolved molecular atlas of C. elegans embryogenesis at single-cell resolution](https://science.sciencemag.org/content/365/6459/eaax1971.long) (Packer et al, Science 2019).

For this demonstration the original data available on [GEO126954](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE126954) was processed using a machine learning framework called [Single-cell Variational Inference (scVI)](https://github.com/YosefLab/scVI). The scVI framework enables integrating data from different sources (different experiments, batches and technologies), clustering and label transfer, and performing differential expression between clusters.

To learn how the plots were made, check out [this Jupyter notebook](https://colab.research.google.com/drive/1hF7KSujhhHcyxzWkzAHy9lazXLexainr) which creates the plots shown here. It runs on Google Colab so you can start playing right away.

Feedback on this and other explorations will inform how WormBase may incorporate and display single cell data in the future. 

This dashboard and the interactive plots were created using [Plotly Dash](https://dash.plot.ly/introduction) and developed with the online IDE [repl.it](https://repl.it/~). 

''',
 style={'width': '60em'}
 ),

dcc.Markdown('''

## 🎨 t-SNE embedding of the cells
[t-SNE](https://distill.pub/2016/misread-tsne/) is a visualization technique that tries push together points that are close in space, and separate points that are not close, but distances are meaningless. You can color the t-SNE embedding according to the features below. The colors are random. Give it a few seconds to reload once you choose a new feature. 

**Color by:**
''',
 style={'width': '60em'}
 ),  
    dcc.RadioItems(
            id='tsne-feature-radio',
            value='cell_type',
            options=[{'label':categorial_features[feature], 'value': feature} for feature in categorial_features.keys()],
            labelStyle={'display': 'inline-block', 'margin-right': 20},
    )
    ]),
    dcc.Graph(id='tsne'),
    html.Br(),


    ################ UMAAAAAP ##########
  html.Div([
dcc.Markdown('''
## 🗺️ UMAP embedding of the cells
[UMAP](https://umap-learn.readthedocs.io/en/latest/how_umap_works.html) is a visualization technique that tries to stitch together points that form a manifold. You can color the UMAP embedding according to the features below. The colors are random. Give it a few seconds to reload once you choose a new feature.    

**Color by:**
''',
 style={'width': '60em'}
 ),  
    dcc.RadioItems(
            id='umap-feature-radio',
            value='cell_type',
            options=[{'label':categorial_features[feature], 'value': feature} for feature in categorial_features.keys()],
            labelStyle={'display': 'inline-block', 'margin-right': 20},
    )
    ]),
    dcc.Graph(id='umap'),
    html.Br(),
    ######################## VOLCANO #################

    html.Div([
dcc.Markdown('''

## 📊 Differential expression

The original annotations by Packer et al. annotations define 37 cell types. To speed things up for this demonstration the pairwise differential expression was pre-computed for the 666 possible combinations. 

Differential expression was not calculated between other annotated clusters (e.g. cell subtypes or embryo time points), but can be done in a relatively straightforward manner with scVI. To learn how scVI computes differential expression, see the original scVI paper [Lopez et al, arXiv:1709.02082](https://arxiv.org/abs/1709.02082) and the recent update described in [Boyeau et al, bioRxiv 2019. doi: 10.1101/794289](https://doi.org/10.1101/794289).


## 🌋 Volcano plot of differential expression between cell types

You can compare any two of the 37 cell types annotated in the original data. By mousing over the plot you can see the [WormBase concise gene descriptions](https://wiki.wormbase.org/index.php/How_WormBase_writes_a_concise_description). This volcano plot is colored according to the Bayes Factor with a color scheme plotly calls Magma 🌋.  
''',
 style={'width': '60em'}
 ), 
##DE-Ciliated_non_amphid_neuron-Ciliated_amphid_neuron

        html.Div([
            dcc.Dropdown(
                id='cell_type1',
                # options=[{'label': i, 'value': i} for i in ['Body_wall_muscle']],
                options=[{'label': 'Body_wall_muscle', 'value': 'Body_wall_muscle'}],

                value='Body_wall_muscle'
            ),
        ],
        style={'width': '48%', 'display': 'inline-block'}),

        html.Div([
            dcc.Dropdown(
                id='cell_type2',
                options=[{'label': i, 'value': i} for i in cell_types_list],
                value='Glia'
            ),
        ],style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
    ]),

    dcc.Graph(id='volcano-plot'),
    html.Br(),

    ############## HEATMAP ###############
dcc.Markdown('''

## 🌡️ Heatmap of top expressed genes per cell type

This heatmap shows the differential expression results between each of the 37 cell types and the remaining cells. Only the top 10 genes for each tissue were chosen to be displayed, totalling 339 genes. By mousing over the plot you can see the [WormBase concise gene descriptions](https://wiki.wormbase.org/index.php/How_WormBase_writes_a_concise_description). 

''',
 style={'width': '60em'}
 ),  

      dcc.Graph(
      id='heatmap',
      figure={
          'data': [dict(
                    z=top_expression.X.round(3),
                    x=top_expression.var['gene_name'],
                    y=top_expression.obs['cell_type_name'],
                    type = 'heatmap',
                    colorscale = 'Viridis',
                    hoverinfo='text',
                    text=gene_description_text_matrix,
                    customdata=np.round(top_expression.layers['bayes_factor'],2),
                    hovertemplate='Name: %{x}<br>Cell type: %{y}<br>Expression: %{z} <br>Bayes factor: %{customdata}   <extra>%{text}</extra>',
                    )],
          'layout': {
                  "title": {"text": "Top 10 expressed genes for each cell type"},
                  "height": 800,
                  'margin':{'l': 250, 'b': 240, 't': 60, 'r': 10},
                  },
      }
  ),
], style={'marginBottom': 60, 'marginTop': 60, 'marginRight': 60, 'marginLeft': 60})

########## TSNE CALLBACK ###################
@app.callback(
    Output('tsne', 'figure'),
    [Input('tsne-feature-radio', 'value')])
def update_figure(cluster_feature):
    cluster_ids = cells[cluster_feature].cat.codes.unique()
    id_to_cluster_map = dict( zip( cells[cluster_feature].cat.codes, cells[cluster_feature] ) )
    cluster_to_id_map  = dict([[v,k] for k,v in id_to_cluster_map.items()])
    traces = []
    for _cluster_id in cells[cluster_feature].cat.codes.unique():
        traces.append(dict(
            x=cells['tsne1'][cells[cluster_feature].cat.codes==_cluster_id],
            y=cells['tsne2'][cells[cluster_feature].cat.codes==_cluster_id],
            text=cells['cell_type'],
            mode='markers',
            opacity=0.7,
            marker={
                'size': 7,
                # we randomize colors by starting at a random place in the list of named css colors 
                 'color':css_colors[_cluster_id+np.random.randint(0,len(np.unique(css_colors)))]
            },
            name=str(id_to_cluster_map[_cluster_id]),
            hoverinfo=['name'],
            showlegend=True,
            type='scattergl',
        ))
    return {
        'data': traces,
        'layout': dict(
            xaxis={'title': 't-SNE 1'},
            yaxis={'title': 't-SNE 2'},
            margin={'l': 10, 'b': 40, 't': 60, 'r': 10},
            legend={'x': 1, 'y': 1},
            hovermode='closest',
            title="t-SNE colored by " + categorial_features[cluster_feature],
            height=800
        )
    }

########## TSNE CALLBACK ###################
@app.callback(
    Output('umap', 'figure'),
    [Input('umap-feature-radio', 'value')])
def update_figure(cluster_feature):
    cluster_ids = cells[cluster_feature].cat.codes.unique()
    id_to_cluster_map = dict( zip( cells[cluster_feature].cat.codes, cells[cluster_feature] ) )
    cluster_to_id_map  = dict([[v,k] for k,v in id_to_cluster_map.items()])
    traces = []
    for _cluster_id in cells[cluster_feature].cat.codes.unique():
        traces.append(dict(
            x=cells['umap1'][cells[cluster_feature].cat.codes==_cluster_id],
            y=cells['umap2'][cells[cluster_feature].cat.codes==_cluster_id],
            text=cells['cell_type'],
            mode='markers',
            opacity=0.7,
            marker={
                'size': 7,
                # we randomize colors by starting at a random place in the list of named css colors 
                 'color':css_colors[_cluster_id+np.random.randint(0,len(np.unique(css_colors)))]
            },
            name=str(id_to_cluster_map[_cluster_id]),
            hoverinfo=['name'],
            showlegend=True,
            type='scattergl',
        ))
    return {
        'data': traces,
        'layout': dict(
            xaxis={'title': 'UMAP 1'},
            yaxis={'title': 'UMAP 2'},
            margin={'l': 60, 'b': 60, 't': 50, 'r': 10},
            legend={'x': 1, 'y': 1},
            hovermode='closest',
            title="UMAP colored by " + categorial_features[cluster_feature],
            height=800
        )
    }

@app.callback(
    Output('volcano-plot', 'figure'),
    [Input('cell_type1', 'value'),
     Input('cell_type2', 'value')])
def update_graph(cell_type1, cell_type2):
    de=pd.read_csv('./DE1/DE-'+ cell_type1 + '-' + cell_type2 + '.csv')

    return {
        'data': [dict(
            x=de["log_scale_ratio"].round(3),
            y=de["abs_bayes_factor"].round(3),
            text=genes['gene_description_html'] ,
            mode='markers',
            type='scattergl',
            marker={
                'size': 7,
                'opacity': 0.4,
                'color':de["abs_bayes_factor"],
                'colorscale':'Magma', 
                'line': {'width': 0.0, 'color': 'white'}
            }
        )],
        'layout': dict(
            xaxis={
                'title': 'Log of scVI expression scale',
            },
            yaxis={
                'title': 'Absolute value of Bayes Factor',
            },
            margin={'l': 60, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest',
            # paper_bgcolor='red',
            plot_bgcolor='rgba(240,240,240,0.8)',
        )
    }

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')
