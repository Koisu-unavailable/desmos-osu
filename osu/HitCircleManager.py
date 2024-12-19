from graph import graph
from utils import convert_array_to_desmos


class HitCircleManager:
    def __init__(self, Dgraph: graph.Graph):
        self.graph: graph.Graph = Dgraph
        self._hitcircle_times: list[int] = []
        self.current_hitcircleID = 1
        self._hitcircle_positions: list[tuple[int]] = []
        self._hit_cirlce_opacities: list[float] = 0
        self._hitcircles = 0

    def add_hitcircle(self, when_hit: int, pos_vector: tuple[int]):
        self._hitcircle_positions.append(pos_vector)
        self._hitcircle_times.append(when_hit)
        self._hitcircles += 1

    def compile_graph(self):
        x_positions = []
        y_positions = []
        hitcircle_folder_id = self.graph.add_folder(r"HCircleOutlines")
        hitcircle_fill_folder_id = self.graph.add_folder(r"HOutlines")

        for i in range(self._hitcircles):
            # Actual index of hit circle since desmos is 1-indexed
            act_value = i + 1
            self.graph.add_expression(
                f"y=\left(\left(x-H_{{X}}\left[{act_value}\\right]\\right)^{{2}}+\left(y-H_{{Y}}\left[{act_value}\\right]\\right)^{{2}}\\right)-10^{{2}}",
                folderId = hitcircle_folder_id
            )

        for vector in self._hitcircle_positions:
            x_positions.append(vector[0])
            y_positions.append(vector[1])
        self.graph.add_expression(
            f"H_{{times}}={convert_array_to_desmos.convert_array_to_desmos_list(self._hitcircle_times)}"
        )
        self.graph.add_expression(
            f"H_{{X}}={convert_array_to_desmos.convert_array_to_desmos_list(x_positions)}"
        )
        self.graph.add_expression(
            f"H_{{Y}}={convert_array_to_desmos.convert_array_to_desmos_list(y_positions)}"
        )
