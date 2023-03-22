import functools

def even(arr):
    dict = {"parni": [], "neparni": []}

    for value in arr:
        if int(value) % 2 == 0:
            dict["parni"].append(value)
        else:
            dict["neparni"].append(value)

    return dict


def type_to_dict(arr):
    dict = {}

    for item in arr:
        str_type = type(item).__name__
        if hasattr(dict, str_type):
            dict[str_type].append(item)
        else:
            dict[str_type] = [item]

    return dict


def inc_decr(arr):
	
