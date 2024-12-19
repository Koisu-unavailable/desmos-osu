import json
from graph import graph
from osu import HitCircleManager



DEFAULT_OSU_GRAPH = r'''{
  "version": 11,
  "randomSeed": "62b086b88acfe053b5997d0a5a9b7c74",
  "graph": {
    "viewport": {
      "xmin": -18.26664112400944,
      "ymin": -13.485440331295433,
      "xmax": 28.467593846637584,
      "ymax": 16.832236179407605
    }
  },
  "expressions": {
    "list": [
      {
        "type": "expression",
        "id": "0",
        "color": "#c74440",
        "latex": "G_{ametime}=0",
        "slider": {
          "hardMin": true,
          "min": "0",
          "max": "138"
        }
      }
    ],
    "ticker": {
      "handlerLatex": "G_{ametime}\\to G_{ametime}+1",
      "minStepLatex": "33",
      "open": true
    }
  },
  "includeFunctionParametersInRandomSeed": true,
  "doNotMigrateMovablePointStyle": true
}'''
with open("./out.json", "r+") as file:
    obj = json.loads(DEFAULT_OSU_GRAPH)
    Dgraph = graph.Graph(obj)
    manager = HitCircleManager.HitCircleManager(Dgraph)
    manager.add_hitcircle(30, (1,0))
    manager.add_hitcircle(209, (3,7))
    manager.compile_graph()
    # Remove everything and go to beginning
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