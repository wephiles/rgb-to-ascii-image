#!/usr/bin/python
# -*- encoding: utf-8 -*-
# Author : JinYu@20866
# Email : wephiles@gmail.com
# FileName : main.py
# Version:
# Time : 2024/11/03 14:57:59
# Description :
# Website : https://github.com/wephiles
# Copyright : Copyright © 2024 by JinYu@20866, All rights reserved.

import os

from functools import wraps


def decorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'I am runing before {func.__name__}!')
        res =func(*args, **kwargs)
        print(f'Yeah, I am runing after {func.__name__}!')
        return res

    return wrapper


@decorator
def main():
    print(f"Hello, I am function {__name__}!")
    return 0


if __name__ == "__main__":
    main()

# --END--

