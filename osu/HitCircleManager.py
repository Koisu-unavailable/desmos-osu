from graph import graph
from utils import convert_array_to_desmos

class HitCircleManager:
    def __init__(self, Dgraph: graph.Graph):
        self.graph : graph.Graph = Dgraph
        self._hitcircle_times : list[int] = []
        self.current_hitcircleID = 1
        self._hitcircle_positions : list[tuple[int]] = []
    def add_hitcircle(self, when_hit: int, pos_vector : tuple[int]):
        self._hitcircle_positions.append(pos_vector)
        self._hitcircle_times.append(when_hit)
    def compile_graph(self):
        self.graph.add_expression(f"H_{{times}}={convert_array_to_desmos.convert_array_to_desmos_list(self._hitcircle_times)}")
    
    



