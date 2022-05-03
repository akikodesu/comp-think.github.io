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


# Test case for the function
def test_nearest(list_i, expected):
    result = nearest(list_i)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def nearest(list_i):
    result = []

    for idx, v in enumerate(list_i):
        smaller = []
        
        for p in list_i[:idx]:
            if p < v:
                smaller.append(p)
        
        if smaller:
            result.append(smaller[-1])
        else:
            result.append(None)

    return result


# Tests
print(test_nearest([], []))
print(test_nearest([7], [None]))
print(test_nearest([7, 3], [None, None]))
print(test_nearest([3, 7], [None, 3]))
print(test_nearest([0, 8, 4, 12, 2, 10, 6, 14, 1], [None, 0, 0, 4, 0, 2, 2, 6, 0]))
