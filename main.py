import json
from graph import graph





with open("./out.json", "r+") as file:
    obj = json.load(file)
    Dgraph = graph.Graph(obj)
    Dgraph.add_expression(
        r"H_{itCircleOutline}=\left(\left(x-C_{ircleX}\right)^{2}+\left(y-C_{ircleY}\right)^{2}\right)-h_{itCircleRadius}^{2}",
        color="#000000")
    file.truncate(0)
    file.seek(0)
    json.dump(Dgraph.return_json(), file)

    
"""
        {
          "type": "expression",
          "id": "26",
          "folderId": "7",
          "color": "#000000",
          "latex": "y=H_{itCircleOutline}",
          "lineOpacity": "H_{itCircleOpacity}"
        },
"""