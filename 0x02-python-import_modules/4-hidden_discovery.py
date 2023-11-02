#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)
    number = len(dir(hidden_4))
    for i in range(number):
        temp = names[i]
        if temp[:2] != "__":
            print(names[i])
