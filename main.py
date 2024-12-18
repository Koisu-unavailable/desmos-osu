import json
from graph import graph
from osu import HitCircleManager




with open("./out.json", "r+") as file:
    obj = json.load(file)
    Dgraph = graph.Graph(obj)
    manager = HitCircleManager.HitCircleManager(Dgraph)
    manager.add_hitcircle(30, (1,0))
    manager.compile_graph()
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