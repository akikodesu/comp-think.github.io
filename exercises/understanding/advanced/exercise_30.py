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


def cou(mat, n_char):
    n_char_in_mat = n_char % len(mat)
    idx = int(mat[n_char_in_mat])

    mat_l = []
    for c in mat:
        mat_l.append(c)

    result = []
    while len(mat_l) > 0:
        jdx = idx % len(mat_l)
        result.append(mat_l[jdx])
        mat_l = mat_l[:jdx]
    
    return result

my_name = sub(" +", "", input("Please provide your name: ").lower())
my_mat = sub(" +", "", input("Please provide your matriculation number: ").lower())
print("Result:", cou(my_mat, len(my_name)))
