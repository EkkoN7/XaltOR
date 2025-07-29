import os
from pathlib import Path
from Framework import frame_files, frame_input

directory_path = Path(r"C:\Users\Ekko\Documents\Test")


user_key = ("Password")
key = user_key.encode()
print(key)

#user_select = input("Welcome. Would you like to encrypt/decrypt a TXT file or a message? (txt/msg): ").lower().strip()
user_select = "msg" #testmode

if user_select == "txt":
    for files in directory_path.iterdir():
        extension = frame_files.split_extension(files)
        if extension == ".txt":
            with open (files, "r") as f:
                text = f.read()
                print (text)

if user_select == "msg":
    user_mode = input("Would you like to (e)nrypt or (d)ecrypt a message? ").lower().strip()
    if user_mode == "e":
        user_msg = input("Message: ").strip()
        result = []
        bmsg = user_msg.encode()
        bmsg_list = list(bmsg)

        key_list = list(key)
        bmsg_len = len(bmsg)
        key_len = len(key)
        for char in range(bmsg_len):
            xor = bmsg_list[char] ^ key_list[char % key_len]
            result.append(xor)
        new_result = "".join(str(result))
        print(new_result[1:-1])

    if user_mode == "d":
        user_msg = input("Message: ").strip()
        user_msg_list = list(user_msg)
        user_msg_int = []
        for num in user_msg:
            user_msg_int.append(int(num))


        print(type(user_msg_list))
        original_bytes_list = []
        msg_len = len(user_msg_list)
        key_len = len(key)

        for i in range(msg_len):
            xor_result = user_msg_list[i] ^ key[i % key_len]
            original_bytes_list.append(xor_result)

        original_bytes = bytes(original_bytes_list)
        decode_msg = original_bytes.decode('utf-8')
        print(decode_msg)

