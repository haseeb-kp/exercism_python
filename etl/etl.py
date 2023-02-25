def transform(legacy_data):
    result = {}
    for key in legacy_data.keys():
        for value in legacy_data[key]:
            result[value.lower()] = key
    return result
