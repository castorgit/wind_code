# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 01:10:01 2019

@author: Manero
"""

from Wind.Results import DBResults
from Wind.Private.DBConfig import mongoremote,mongolocal,mongolocaltest
from plotly.offline import init_notebook_mode
init_notebook_mode(connected=True)
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

query = {"experiment": "JM_MLP_s2s","status":"done"}
results = DBResults(conn=mongolocal)
results.retrieve_results(query)
results.selected_size()

results.plot_map(dset=('test'),figsize=(1200,800),cmap='Viridis')