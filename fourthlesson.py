def my_range(start, stop, step=1):
    result = []
    actual = start
    while actual < stop:
        result.append(actual)
        actual += step 
        return result





if __name__ == "__main__":
    print(list(range(1, 10, 2,)))
    print(my_range(2, 11, 2))



def my_enumerate(interable, start=0):
    result = []
    index = 0 
    while index < len(interable):
        result.append( (index, interable[index]))
        index += 1
        return result


if __name__ == "__main__":

    text = "abcdef"
    print(list(enumerate(text, 100)))
    print(my_enumerate(text, 100))

    

