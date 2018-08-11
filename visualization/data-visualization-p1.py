import dash
import dash_core_components as dcc
import dash_html_components as html


#dash is a flask app?


app = dash.Dash()

app.layout = html.Div(children=[
    html.H1('Dash tutorials'),
    dcc.Graph(id= 'example',
              figure = {
                  'data': [
                      {'x': [1, 5, 6, 7, 9], 'y': [5, 6, 7, 8, 9], 'type': 'line', 'name': 'boats'},
                      {'x': [1, 5, 6, 9, 9], 'y': [5, 7, 7, 8, 9], 'type': 'bar', 'name': 'cars'},
                      ],
                  'layout': {
                   'title': 'Basic Dash Example'
                  }
              })
    ])


if __name__ == '__main__':
    app.run_server(debug=True)

