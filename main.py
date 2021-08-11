import plotly.graph_objects as go

import pandas as pd

spreadsheet = pd.read_csv('sheet.csv')
spreadsheet = spreadsheet.drop(['Status', 'Link', 'Notes'], axis=1)
spreadsheet = spreadsheet.dropna(how='any', axis=0)

spreadsheet['Valence Energy Level'] = spreadsheet['Valence Energy Level'] * -1
spreadsheet['Conduction Energy Level'] = spreadsheet['Conduction Energy Level'] * -1
spreadsheet.reset_index(inplace=True)
fig = go.Figure()
fig.update_layout(margin=dict(t=150))

annotationList = [go.Annotation(x=.1, y=0, text='Evacuum', showarrow=False)]

for index, row in spreadsheet.iterrows():
    row = row[1:]
    fig.add_trace(go.Box(y=[row[1], row[2]], name=row[0]))
    print(dict(x=index, y=float(row[1])+.15, text=str(row[1]*-1), showarrow=False))
    annotationList.append(go.Annotation(x=index, y=row[1]+.15, text=str(row[1]*-1), showarrow=False))
    annotationList.append(go.Annotation(x=index, y=row[2]-.15, text=str(row[2]*-1), showarrow=False))


fig.update_layout(
    uniformtext_minsize=8,
    uniformtext_mode='hide',
    yaxis1=dict(range=[-11, 0]),
    title="Comparison of Band Energies of Hole Blocking Layer Candidates",
    xaxis_title="Candidate Materials",
    yaxis_title="Band Energies",
    legend_title="Candidate Materials",
    font={
        'size': 25,
    },
    annotations=annotationList
)

fig.show()
fig.write_html('index.html')
