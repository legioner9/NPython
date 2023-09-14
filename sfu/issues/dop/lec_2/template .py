def get_people_with_min_age(people):
    m = 100000000000
    for p in people:
        if p["age"] < m:
            m = p["age"]

    names = []
    for p in people:
        if p["age"] == m:
            names.append(p["name"])

    for i in range(len(names)):
        for j in range(len(names)):
            if i < j:
                if names[i] > names[j]:
                    names[i], names[j] = names[j], names[i]

    return names

def get_people_with_max_age(people):
    m = -100000000000
    for p in people:
        if p["age"] > m:
            m = p["age"]

    names = []
    for p in people:
        if p["age"] == m:
            names.append(p["name"])

    for i in range(len(names)):
        for j in range(len(names)):
            if i < j:
                if names[i] > names[j]:
                    names[i], names[j] = names[j], names[i]

    return names

def get_people_with_min_height(people):
    m = 100000000000
    for p in people:
        if p["height"] < m:
            m = p["height"]

    names = []
    for p in people:
        if p["height"] == m:
            names.append(p["name"])

    for i in range(len(names)):
        for j in range(len(names)):
            if i < j:
                if names[i] > names[j]:
                    names[i], names[j] = names[j], names[i]

    return names


def get_people_with_max_height(people):
    m = -100000000000
    for p in people:
        if p["height"] > m:
            m = p["height"]

    names = []
    for p in people:
        if p["height"] == m:
            names.append(p["name"])

    for i in range(len(names)):
        for j in range(len(names)):
            if i < j:
                if names[i] > names[j]:
                    names[i], names[j] = names[j], names[i]

    return names

def get_people_with_min_weight(people):
    m = 100000000000
    for p in people:
        if p["weight"] < m:
            m = p["weight"]

    names = []
    for p in people:
        if p["weight"] == m:
            names.append(p["name"])

    for i in range(len(names)):
        for j in range(len(names)):
            if i < j:
                if names[i] > names[j]:
                    names[i], names[j] = names[j], names[i]

    return names


def get_people_with_max_weight(people):
    m = -100000000000
    for p in people:
        if p["weight"] > m:
            m = p["weight"]

    names = []
    for p in people:
        if p["weight"] == m:
            names.append(p["name"])

    for i in range(len(names)):
        for j in range(len(names)):
            if i < j:
                if names[i] > names[j]:
                    names[i], names[j] = names[j], names[i]

    return names
