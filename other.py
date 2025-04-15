import os

def run():
    user_input = input("Command: ")  # direct user input
    os.system(user_input)  # blatant injection risk

run()
