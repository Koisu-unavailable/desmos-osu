
def convert_array_to_desmos_list(arr: list[float]):
    arr_index = 0
    latex_str = f"\left[{arr[arr_index]}"
    for i in range(len(arr)):
        num = arr[i]
        # Skip first element, already added
        if i == 0:
            arr_index += 1
            continue
        latex_str += f", {arr[arr_index]}"
        arr_index += 1
    latex_str += r"\right]"
    return latex_str



