
def add_data(todos):
    with open('todo.txt','w') as f:
        for t in todos:
            f.write(f'{t} \n')


def load_data():
    load = []
    with open('todo.txt','r') as f:
        for l in f:
            load.append(l.strip())
    return load

my_todos = ['1','2','3'] #just a number but string cause string is too long

add_data(my_todos)
print('Added')
for t in load_data():
    print(t)