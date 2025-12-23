def write_file(file_name, file_content):
    with open (f"{file_name}.txt", encoding="utf-8", mode="w") as txt_file:
        txt_file.write(file_content)

def append_file(file_name, append_content):
    with open (f"{file_name}.txt", encoding='utf-8', mode='a') as txt_file:
        txt_file.write(append_content)

def read_file(file_name):
    with open (f"{file_name}.txt", encoding='utf-8') as txt_file:
        return txt_file.read()
