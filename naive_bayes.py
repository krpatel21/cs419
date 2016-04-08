def file2list(fname):
    d = open(fname).read().split("\n")
    data = [instance.split(",") for instance in d if len(instance)>1]
    return data

