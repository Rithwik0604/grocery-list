import json

import os

file = "./data.json"


def ascendSort(array):
    newList = []
    while len(array) > 0:
        smallest = 0
        for j in range(len(array)):
            if array[smallest]["item"] > array[j]["item"]:
                smallest = j
        newList.append(array.pop(smallest))
    return newList


def sortData(data: list, newData: dict = {}, first: bool = False):
    # print("Data in sortData", data)
    returnData: list = []
    categories = [
        "Fruit & Vegetables",
        "Dairy",
        "Poultry",
        "Pastas, Grains and sauces",
        "Frozen Foods"  ,
        "Snacks",
        "Breads",
        "Other",
    ]

    if first is True:
        for category in categories:
            currentList = []
            if data["category"] == category:
                currentList.append(data)
            returnData.append({category: currentList})

    else:
        for i, v in enumerate(data):
            key = list(v.keys())[0]
            if key == newData["category"]:
                data[i][key].append(newData)
                data[i][key] = ascendSort(data[i][key])
                break
        returnData = data

    # print(returnData)
    return returnData


def read():
    if os.path.getsize(file) == 0:
        return 1
    loadData: list = []
    with open(file, "r") as f:
        loadData = json.loads(f.read())
    # print(loadData)
    return loadData


def add(data):
    dumpData = data
    loadData: list = []
    if os.path.getsize(file) == 0:
        with open(file, "w") as f:
            f.write(json.dumps(sortData(dumpData, first=True), indent=4))
    else:
        with open(file, "r") as f:
            loadData = json.loads(f.read())
        # print("Check1: ", loadData)

        # check if item exists
        for category in loadData:
            # print("Category: ", category)
            for object in category:
                # print("Object", object)
                for i in category[object]:
                    if i["item"] == data["item"]:
                        return

        # print("LoadData is: ", loadData)

        with open(file, "w") as f:
            # loadData.append(data)
            loadData = sortData(loadData, data, False)
            f.write(json.dumps(loadData, indent=4))




def got(item:str, category:str):
    loadData = []
    with open(file,'r') as f:
        loadData = json.loads(f.read())
    for i in loadData:
        if list(i.keys())[0] == category:
            items = i[list(i.keys())[0]]
            for j in items:
                if j['item'] == item:
                    j['got'] = not j['got']
    with open(file,'w') as f:
        f.write(json.dumps(loadData))



def uncheckAll():
    loadData = []
    with open(file,"r") as f:
        loadData = json.loads(f.read())
    for i in loadData:
        items = i[list(i.keys())[0]]
        print(items)
        for j in items:
            j['got'] = False
    with open(file,'w') as f:
        f.write(json.dumps(loadData))


def edit(data):
    loadData = []
    with open(file,'r') as f:
        loadData = json.loads(f.read())

    for i in loadData:
        if list(i.keys())[0] == data['old_category']:
            items = i[list(i.keys())[0]]
            for index,j in enumerate(items):
                if j['item'] == data['old_item']:
                    items.pop(index)


    for index,i in enumerate(loadData):
        if list(i.keys())[0] == data['category']:
            items = i[list(i.keys())[0]]
            data.pop('old_item')
            data.pop('old_category')
            items.append(data)
            items = ascendSort(items)
            loadData[index] = { data['category']: items}
    with open(file,'w') as f:
        f.write(json.dumps(loadData))


def delete(item:str, category:str):
    loadData = []
    with open(file,'r') as f:
        loadData = json.loads(f.read())
    for i in loadData:
        if list(i.keys())[0] == category:
            items = i[list(i.keys())[0]]
            for index,j in enumerate(items):
                if j['item'] == item:
                    items.pop(index)
    with open(file,'w') as f:
        f.write(json.dumps(loadData))


def reset():
    with open(file,"w") as f:
        return