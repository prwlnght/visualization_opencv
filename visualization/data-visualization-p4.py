'''Getting data live and updating the graph
copyright @prwl_nght

todo:
0. Base impl of the tutorial
1. Get a (fake) tf flow session with epoch accuracies going on in a log file
2. Get something to show, and update on teh screen


'''

import random
from collections import deque

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Output, Event

X = deque(maxlen=4000)
Y = deque(maxlen=4000)

X.append(1)
Y.append(1)

app = dash.Dash(__name__)
app.layout = html.Div(
    [
        dcc.Graph(id='live-graph', animate=True),
        dcc.Interval(id='graph-update', interval=1 * 1000)
    ])


@app.callback(Output('live-graph', 'figure'), events=[Event('graph-update', 'interval')])
def update_graph():
    global X, Y
    X.append(X[-1] + 1)
    Y.append(Y[-1] + Y[-1] * random.uniform(-0.1, 0.1))

    data = go.Scatter(
        x=list(X),
        y=list(Y),
        name='Scatter',
        mode='lines+markers'
    )

    return {
        'data': [data],
        'layout': go.Layout(xaxis=dict(range=[0, 4000]), yaxis=dict(range=[min(Y), max(Y)]))
    }


if __name__ == "__main__":
    app.run_server(debug=True)
