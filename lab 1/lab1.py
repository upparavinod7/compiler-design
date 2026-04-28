symbol_table = {}
def add_symbol(name, value):
    if name in symbol_table:
        print("Symbol already exists")
    else:
        symbol_table[name]=value
        print("symbol added")
def update_symbol(name,value):
    if name in symbol_table:
        symbol_table[name]=value
        print("symbol updated")
    else:
        print("symbol not found")
def find_symbol(name):
    if name in symbol_table:
        print("symbol found value", symbol_table[name])
    else:
        print("Symbol not found")
def delete_symbol(name):
    if name in symbol_table:
        del symbol_table[name]
        print("symbol deleted")
    else:
        print("symbol not found")
def show_symbols():
    for name in symbol_table:
        print("name", name, "value", symbol_table[name])
add_symbol("x", 20)
add_symbol("y" , 30)
add_symbol("z" , 40)
show_symbols()
update_symbol("x", 10)
show_symbols()
find_symbol("y")
delete_symbol("z")
