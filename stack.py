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


# Checks if a string of parentheses is balanced.
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


print(par_checker("((()))"))
print(par_checker("((()()))"))
print(par_checker("(()"))
print(par_checker(")()"))


# Checks if a string of parentheses, brackets, and braces is balanced.
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


# Helper function for balance_checker.
def matches(sym_left, sym_right):
    all_lefts = "([{"
    all_rights = ")]}"
    return all_lefts.index(sym_left) == all_rights.index(sym_right)


print(balance_checker("{({([][])}())}"))
print(balance_checker("[{()]"))


# converts an integer to a binary string
def divide_by_2(decimal_num):
    rem_stack = Stack()

    while decimal_num > 0:
        decimal_num, rem = divmod(decimal_num, 2)
        rem_stack.push(rem)

    bin_string = ""
    while not rem_stack.is_empty():
        bin_string += str(rem_stack.pop())

    return bin_string


print(divide_by_2(32))
print(divide_by_2(127))


# converts an integer to a base string
def base_converter(decimal_num, base):
    digits = "0123456789ABCDEF"
    rem_stack = Stack()

    while decimal_num > 0:
        decimal_num, rem = divmod(decimal_num, base)
        rem_stack.push(rem)

    new_string = ""
    while not rem_stack.is_empty():
        new_string += digits[rem_stack.pop()]

    return new_string


print(base_converter(25, 8))
print(base_converter(256, 16))


def infix_to_postfix(infix_expr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    op_stack = Stack()
    postfix_list = []
    token_list = infix_expr.split()

    for token in token_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfix_list.append(token)
        elif token == "(":
            op_stack.push(token)
        elif token == ")":
            top_token = op_stack.pop()
            while top_token != "(":
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        else:
            while not op_stack.is_empty() and prec[op_stack.peek()] >= prec[token]:
                postfix_list.append(op_stack.pop())
            op_stack.push(token)
    
    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())
    
    return " ".join(postfix_list)

print(infix_to_postfix("A * B + C * D"))
print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))


def postfix_eval(postfix_expr):
    operand_stack = Stack()
    token_list = postfix_expr.split()

    for token in token_list:
        if token in "0123456789":
            operand_stack.push(int(token))
        else:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = do_math(token, operand1, operand2)
            operand_stack.push(result)
    return operand_stack.pop()

def do_math(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2


print(postfix_eval("7 8 + 3 2 + /"))