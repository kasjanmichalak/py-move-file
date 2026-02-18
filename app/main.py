import os


def move_file(command: str):
    lista = command.split()
    if lista[0] != "mv" :
        return
    current_file_name = lista[1]
    dest_path = lista[2]

    if dest_path[-1] == "/":
        new_file_name = current_file_name.split("/")[-1]
        dest = dest_path + new_file_name
    else:
        dest = dest_path
    dirs = dest.split("/")[:-1]
    current = ""
    for d in dirs:
        current += d + "/"
        if not os.path.exists(current):
            os.mkdir(current)

    with open (current_file_name, "r") as file:
        content = file.read()
        with open (dest, "w") as file_new:
            file_new.write(content)
    os.remove(current_file_name)
