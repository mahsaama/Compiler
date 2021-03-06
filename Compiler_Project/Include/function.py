import sys

class_type_objects = []
function_objects = []
function_table = {}
class_table = {}


class Type:
    name: str
    size: int

    def __init__(self, name=None, meta=None, size=0):
        self.name = name
        self.size = size
        self._meta = meta


class Class:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []
        self.variables = []
        self.functions = []
        class_type_objects.append(self)

    def find_function(self, name):

        counter = 0
        for func in self.functions:
            if func.name == name:
                return func, counter
            counter += 1
        return -1

    def find_var(self, ident):
        counter = 0
        for var in self.variables:
            if var[0] == ident:
                return self.variables[counter][1], counter
            else:
                counter += 1
        return self.variables[-1][1], -1


class Function:
    def __init__(self, name=None, label=None, return_type=Type(), formals=None):
        self.name = name
        self.return_type = return_type

        if formals is None:
            self.formals = []
        else:
            self.formals = formals

        self.label = label

    def find_formal(self, name: str):
        counter = 0
        for formal in self.formals:
            if formal[0] == name:
                return formal, counter
            counter += 1
        raise ChildProcessError()


def lib_functions():
    # Add library functions
    function_objects.append(
        Function(name='itob', label='root/itob', return_type=Type('bool'), formals=[['ival', Type('int')]])
    )

    function_table['itob'] = 0

    function_objects.append(
        Function(name='btoi', label='root/btoi', return_type=Type('bool'), formals=[['bval', Type('bool')]])
    )

    function_table['btoi'] = 1

    function_objects.append(
        Function(name='itod', label='root/itod', return_type=Type('double'), formals=[['ival', Type('int')]])
    )

    function_table['itod'] = 2

    function_objects.append(
        Function(name='dtoi_', label='root/dtoi_', return_type=Type('int'), formals=[['dval', Type('double')]])

    )

    function_table['dtoi_'] = 3

    function_objects.append(
        Function(name='ReadChar__', label='root/ReadChar__', return_type=Type('int'), formals=[])
    )

    function_table['ReadChar__'] = 4


lib_functions()


