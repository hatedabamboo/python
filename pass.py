#!/usr/bin/python3


import sys, random, string


def die():
    message = """Usage:
    {} <length>""".format(sys.argv[0])
    sys.exit(message)


def pass_gen():
    if len(sys.argv) == 2:
        length = int(sys.argv[1])
        chars = string.ascii_letters + string.digits + "!@#$%^&*()"
        password = ''.join(random.choices(chars, k=length))
        print(password)
    else:
        die()

pass_gen()
