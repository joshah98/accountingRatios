def getData(data):
    processedData = []

    for i in data:
        statement = {}
        for k, v in i.items():
            try:
                statement[k] = v['raw']
            except TypeError:
                continue
            except KeyError:
                continue

        processedData.append(statement)

    return processedData