symbol_table = {}
def add_symbol(name, value):
    if name in symbol_table:
        print("Symbol already exists")
    else:
        symbol_table[name]=value
        print("symbol added")
    