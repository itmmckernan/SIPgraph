import plotly.graph_objects as go
import pandas as pd

spreadsheet = pd.read_csv('sheet.csv')
spreadsheet = spreadsheet.drop(['Status','Link','Notes'], axis=1,)
spreadsheet = spreadsheet.dropna(how='any', axis=0)

fig = go.Figure()

for index, row in spreadsheet.iterrows():

    print(row)
    fig.add_trace(go.Box(y=[row[1], row[2]], name=row[0]))

fig.show()
fig.write_html('index.html')
