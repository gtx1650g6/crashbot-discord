import time

def log(data: str, array: list) -> str:
    local = time.localtime()
    array.append(f"[DEBUG | {time.strftime("%d.%m.%Y %H:%M:%S", local)}] {data}")

def create(array: list) -> None:
    file_txt = open('loglist.txt', 'w')
    for data in array:
        file_txt.write(data+"\n")
    file_txt.close()