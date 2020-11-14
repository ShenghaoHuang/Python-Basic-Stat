def mode(list_in):
    mode_dict = {}
    mode_list = []
    for key in list_in:
        mode_dict[key] = list_in.count(key)

    most = max(mode_dict.values())
    for key, value in mode_dict.items():
        if value == most:
            mode_list.append(key)
    return mode_list

