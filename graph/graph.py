class Graph():
    
    def __init__(self, json: any):
        '''
        Json needs to be pre-loaded
        '''
        self.__json = json 
        self.expressions : list[dict] = self.__json['expressions']['list']
        self.current_id = 1
    def add_expression(self, latex_expression : str, **kwargs) -> None:
        expr_json = {
        "type" : "expression",
        "latex" : latex_expression,
        "id" : self.current_id,
        **kwargs
    }
        self.expressions.append(expr_json)
        self.current_id += 1
    def add_folder(self, name: str) -> int:
        """Creates a folder and returns it's id"""
        expr_json = {
            "type" : "folder",
            "id" : self.current_id,
            "title" : name,
            "collapsed" : False
        }
        self.expressions.append(expr_json)
        self.current_id += 1
        return self.current_id
    def return_json(self):
        return self.__json
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