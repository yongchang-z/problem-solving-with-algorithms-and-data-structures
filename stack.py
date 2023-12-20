class Stack:
    def __init__(self):
        self._items = []
    
    def __str__(self):
        return str(self._items)
    
    def is_empty(self):
        return not bool(self._items)
    
    def push(self, item):
        self._items.append(item)
    
    def pop(self):
        return self._items.pop()
    
    def peek(self):
        return self._items[-1]
    
    def size(self):
        return len(self._items)
    


def par_checker(symbol_string):
    s = Stack()
    for symbol in symbol_string:
        if symbol == "(":
            s.push(symbol)
        else:
            if s.is_empty():
                return False
            else:
                s.pop()
    return s.is_empty()

print(par_checker('((()))'))
print(par_checker('((()()))'))
print(par_checker("(()"))
print(par_checker(")()"))


def balance_checker(symbol_string):
    s = Stack()
    for symbol in symbol_string:
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.is_empty():
                return False
            else:
                if not matches(s.pop(), symbol):
                    return False
    
    return s.is_empty()

def matches(sym_left, sym_right):
    all_lefts = "([{"
    all_rights = ")]}"
    return all_lefts.index(sym_left) == all_rights.index(sym_right)

print(balance_checker('{({([][])}())}'))
print(balance_checker('[{()]'))
