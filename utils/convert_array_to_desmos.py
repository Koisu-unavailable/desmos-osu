def convert_int_array_to_desmos_list(arr : list[int]):
    arr_index = 0
    latex_str = f"\left[{arr[arr_index]}"
    for num in arr:
        if arr.index(num) == 0: 
            continue
        latex_str += f", \{arr[arr_index]}"
    latex_str += r"\right]"
    return latex_str

print(convert_int_array_to_desmos_list([1,2]))
