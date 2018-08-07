import datetime

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas_datareader as web
from dash.dependencies import Input, Output


# df.reset_index(inplace=True)
# df.set_index("Date", inplace=True)
# df = df.drop("Symbol", axis=1)


app = dash.Dash()
# input_data = 'TSLA'

app.layout = html.Div(children=[

    html.Div(children='''Symbol to graph:'''),
    dcc.Input(id='input', value='', type='text'),
    html.Div(id='output-graph')
])


@app.callback(
    Output(component_id='output-graph', component_property='children'),
    [Input(component_id='input', component_property='value')]
)
def update_value(input_data):
    start = datetime.datetime(2013, 1, 1)
    end = datetime.datetime.now()
    try:
        df = web.DataReader(input_data, 'iex', start, end)
        return dcc.Graph(
            id='example-graph',
            figure={
                'data': [
                    {'x': df.index, 'y': df.close, 'type': 'line', 'name': 'stock-data'}
                ],
                'layout': {
                    'title': input_data
                }
            }
        )
    except Exception as e:
        print(str(e))
        df = web.DataReader('TSLA', 'iex', start, end)
        return dcc.Graph(
            id='example-graph-no-fetch'
        )
        #set this on screen


    # df.reset_index(inplace=True)
    # df.set_index("date", inplace=True)
    # df = df.drop("symbol", axis=1)



if __name__ == '__main__':
    app.run_server(debug=True)
