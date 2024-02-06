''' Write a class MyList that inherits from list:

Public instance method: def print_sorted(self): that prints the list, but sorted (ascending sort)
You can assume that all the elements of the list will be of type int
You are not allowed to import any module
'''
class list:

    def print_sorted(self):
        # prints the sorted list
        print(sorted(self))

    class MyList(list):
        def __init__(self):
            super().__init__()

    print(issubclass(MyList, list)) 