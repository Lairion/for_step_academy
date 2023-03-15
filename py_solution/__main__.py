import sys
import time
from tr_tensor import train_model, check_picture
from windows import run_tuya


def exit():
    print("Exit...")
    sys.exit()


actions = {
    "train_model": train_model,
    "check_picture": check_picture,
    "run_tuya": run_tuya,
    "exit": exit
}


def print_parts(parts):
    for i in range(len(parts)):
        print(f"{i}:", f"{parts[i]}")


def main():
    list_key = list(actions.keys())
    print_parts(list_key)
    option = int(input("Choose option: "))
    start = time.time()
    actions[list_key[option]]()
    print("Finish:", time.time() - start)


if __name__ == '__main__':
    while True:
        main()
