# -*- coding: utf-8 -*-
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

print("Hello frend 333")
print("Привет 1")


s = 5

name_user = input("You Name: ")

print("hello word", name_user)
