#!/usr/bin/env python3

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import paramiko

stylesheet = ['style.css']

app = dash.Dash(__name__, external_stylesheets=stylesheet)

app.layout = html.Div(
    [
        html.H3('Input command'),
        dcc.Input(
            id='command',
            type='text',
            placeholder='Ex: ls | wc -l'
        ),
        html.Button('Submit', id='cmd-submit'),
        html.Div(id='output-submit'),
        html.H3('Input connection info'),
        dcc.Input(
            id='connectioninfo',
            type='text',
            placeholder='Ex: root@127.0.0.1'
        ),
        html.Button('Submit', id='connection-submit'),
        html.Div(id='output-connection'),
    ]
)
@app.callback(Output('output-submit', 'children'),
                [Input('cmd-submit', 'n_clicks')],
                [State('command', 'value')])
def storeCommand(clicked, input):
    if clicked:
        command = input
@app.callback(Output('output-connection', 'children'),
                [Input('connection-submit', 'n_clicks')],
                [State('command', 'value')])
def storeConnection(clicked, input):
    if clicked:
        sshinfo = input

if __name__ == '__main__':
    app.run_server(debug=True)