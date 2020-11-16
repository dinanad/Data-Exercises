import plotly
import plotly.graph_objects as go
import plotly.express as px
import plotly.figure_factory as ff
import json
from cleaning_data import data_case

def bar1():
    df = data_case()
    barplot1 = df['case1_risk_diabet'].value_counts()

    fig = go.Figure([
        go.Bar(x=barplot1.index, y=barplot1.values)
        
    ])
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

def bar2():
    df = data_case()
    barplot1 = df[df['case1_risk_diabet']=='risk_diabet']['weight_stat'].value_counts()

    fig = go.Figure([
        go.Bar(x=barplot1.index, y=barplot1.values)
        
    ])
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

def bar3():
    df = data_case()
    barplot1 = df['case2_diabet'].value_counts()

    fig = go.Figure([
        go.Bar(x=barplot1.index, y=barplot1.values)
        
    ])
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

def bar4():
    df = data_case()
    barplot1 = df[df['case2_diabet']=='prediabet/undiag']['weight_stat'].value_counts()

    fig = go.Figure([
        go.Bar(x=barplot1.index, y=barplot1.values)
        
    ])
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

