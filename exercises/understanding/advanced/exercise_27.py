# -*- coding: utf-8 -*-
# Copyright (c) 2022, Silvio Peroni <essepuntato@gmail.com>
#
# Permission to use, copy, modify, and/or distribute this software for any purpose
# with or without fee is hereby granted, provided that the above copyright notice
# and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
# REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
# FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT,
# OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE,
# DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS
# ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS
# SOFTWARE.

from re import sub


def c_rec(chars, mat_list):
    result = ["a", "e", "i", "o", "u"]

    if len(mat_list) == 0:
        result = sorted(list(chars))
        return "".join(result)
    elif mat_list[0] % 2 == 0:
        idx = mat_list[0] % len(result)
        chars.add(result[idx])

    return c_rec(chars, mat_list[1:])
        


my_mat = list(input("Please provide your matriculation number: ").strip())
my_mat_list = [int(i) for i in my_mat]
my_chars = set(sub(" +", "", input("Please provide your full name: ").lower()))
print("Result:", c_rec(my_chars, my_mat_list))
