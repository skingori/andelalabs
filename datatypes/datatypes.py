def data_type(data):
    if data is None:
        return 'no value'
    if isinstance(data, str):
        return len(data)
    elif isinstance(data, bool):
        return data
    elif isinstance(data, int):
        if data < 100:
            return "less than 100"
        elif data == 100:
            return "equal to 100"
        return "more than 100"
    elif isinstance(data, list):
        return data[2] if len(data) > 2 else None
