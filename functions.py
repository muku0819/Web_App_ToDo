def get_todos():
    with open('todos.txt', 'r') as file_local:
        """Read text file"""
        todos_local=file_local.readlines()
        return todos_local

def write_todos(todos_arg):
    """Write todos items"""
    with open('todos.txt', 'w') as file_arg:
        file_arg.writelines(todos_arg)

# this function helps to print below command only when you are executing functions.py
#if it is written under main function , you cannot print :help(get_todos())/"hello" outside the function.py
if __name__=="__main__":
    #print(help(get_todos()))
    print("hello")