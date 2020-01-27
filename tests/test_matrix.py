#!/usr/bin/env python3
"""
This script implements tests for skhub.matrix module.
"""

from itertools import count

import pytest

from skhub.matrix import *


def test_N_of_x_plus_N_of_y_formula():
    """
    Test formula N_of_x_plus_N_of_y.
    """

    f = N_of_x_plus_N_of_y(10, 10, count)

    assert f.get(0, 0) == 0
    assert f.get(5, 9) == 14
    assert f.get(9, 5) == 14
    assert f.get(9, 9) == 18
    with pytest.raises(IndexError):
        f.get(0, 10)

def test_N_of_x_times_N_of_y_formula():
    """
    Test formula N_of_x_times_N_of_y.
    """

    f = N_of_x_times_N_of_y(10, 10, count)

    assert f.get(0, 0) == 0
    assert f.get(5, 9) == 45
    assert f.get(9, 5) == 45
    assert f.get(9, 9) == 81
    with pytest.raises(IndexError):
        f.get(0, 10)

def test_N_of_x_plus_y_plus_1_formula():
    """
    Test formula N_of_x_plus_y_plus_1.
    """

    f = N_of_x_plus_y_plus_1(10, 10, count)

    assert f.get(0, 0) == 1
    assert f.get(5, 9) == 15
    assert f.get(9, 5) == 15
    assert f.get(9, 9) == 19
    with pytest.raises(IndexError):
        f.get(0, 10)

def test_matrix_factory():
    """
    Test matrix factory.
    """

    m = matrix_factory(20, 10, count, N_of_x_plus_y_plus_1)

    assert m[(0, 0)] == 1
    assert m[(0, 9)] == 10
    assert m[(19, 9)] == 29
    with pytest.raises(KeyError):
        m[(0, 10)]

def test_matrix_print(capsys):
    """
    Test matrix print.
    """

    cap = capsys.readouterr()

    m = matrix_factory(20, 20, count, N_of_x_plus_N_of_y)
    m.print()
    expected_output = """0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21
3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22
4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28
10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29
11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31
13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32
14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33
15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34
16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35
17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36
18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37
19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38
"""

    captured = capsys.readouterr()
    assert captured.out == expected_output

def test_matrix_pretty_print(capsys):
    """
    Test matrix pretty-print.
    """

    cap = capsys.readouterr()

    m = matrix_factory(20, 20, count, N_of_x_times_N_of_y)
    m.print(pretty=True)
    expected_output = """  0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
  0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19
  0   2   4   6   8  10  12  14  16  18  20  22  24  26  28  30  32  34  36  38
  0   3   6   9  12  15  18  21  24  27  30  33  36  39  42  45  48  51  54  57
  0   4   8  12  16  20  24  28  32  36  40  44  48  52  56  60  64  68  72  76
  0   5  10  15  20  25  30  35  40  45  50  55  60  65  70  75  80  85  90  95
  0   6  12  18  24  30  36  42  48  54  60  66  72  78  84  90  96 102 108 114
  0   7  14  21  28  35  42  49  56  63  70  77  84  91  98 105 112 119 126 133
  0   8  16  24  32  40  48  56  64  72  80  88  96 104 112 120 128 136 144 152
  0   9  18  27  36  45  54  63  72  81  90  99 108 117 126 135 144 153 162 171
  0  10  20  30  40  50  60  70  80  90 100 110 120 130 140 150 160 170 180 190
  0  11  22  33  44  55  66  77  88  99 110 121 132 143 154 165 176 187 198 209
  0  12  24  36  48  60  72  84  96 108 120 132 144 156 168 180 192 204 216 228
  0  13  26  39  52  65  78  91 104 117 130 143 156 169 182 195 208 221 234 247
  0  14  28  42  56  70  84  98 112 126 140 154 168 182 196 210 224 238 252 266
  0  15  30  45  60  75  90 105 120 135 150 165 180 195 210 225 240 255 270 285
  0  16  32  48  64  80  96 112 128 144 160 176 192 208 224 240 256 272 288 304
  0  17  34  51  68  85 102 119 136 153 170 187 204 221 238 255 272 289 306 323
  0  18  36  54  72  90 108 126 144 162 180 198 216 234 252 270 288 306 324 342
  0  19  38  57  76  95 114 133 152 171 190 209 228 247 266 285 304 323 342 361
"""

    captured = capsys.readouterr()
    assert captured.out == expected_output
