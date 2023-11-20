#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    final = []
    
    for i in range(list_length):
        try:
            final.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
            final.append(0)
        except (TypeError, ValueError):
            print("wrong type")
            final.append(0)
        except IndexError:
            print("out of range")
            final.append(0)
        finally:
            pass

    return final
