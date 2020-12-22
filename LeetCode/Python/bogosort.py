from random import shuffle

def is_sorted(data) -> bool:
    """Determine whether the data is sorted."""
    return all(data[i] <= data[i + 1] for i in range(len(data) - 1))

def bogosort(data) -> int:
    """Shuffle data until sorted."""
    count = 0
    while not is_sorted(data):
        shuffle(data)
        count += 1
    return count


# Counts how many times to get a bogosort in the first try
def bogocount(data) -> int:
    bogocount = 1
    new_data = data.copy()
    count = bogosort(new_data)
    while count > 1:
        new_data2 = data.copy()
        count = bogosort(new_data2)
        bogocount += 1
    return bogocount

a= [1,5,2,4,3, 6]

print(bogocount(a))