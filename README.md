# skhub
A simple exercise with matrices and number generators.

This package contains a module with prime and fibonacci number generators, and a module for handling matrices.

The `matrix` module contains a factory function for generating matrices of a given size, with a given number generator, and a given formula to compute each element of the matrix.


## TOC

-   [Usage](#usage)
-   [Customization](#customization)
-   [Contributing](#contributing)
-   [License](#license)


## Usage

### Clone project

```bash
~$ git clone https://github.com/rodrigogoncalves/skhub
~$ cd skhub
```

### Create and activate a virtual environment, and install dependencies

```bash
~/skhub$ python -m venv venv
~/skhub$ source venv/bin/activate
~/skhub$ pip install -r requirements.txt
```

### Run tests

```bash
(venv) ~/skhub$ pytest
```

### Use the package to generate some matrices and print them on the console

```bash
>>> from skhub.matrix import matrix_factory, N_of_x_plus_N_of_y
>>> from skhub.numbers import prime
>>> m = matrix_factory(10, 20, prime, N_of_x_plus_N_of_y)
>>> m.print(pretty=True)
  4   5   7   9  13  15  19  21  25  31  33  39  43  45  49  55  61  63  69  73
  5   6   8  10  14  16  20  22  26  32  34  40  44  46  50  56  62  64  70  74
  7   8  10  12  16  18  22  24  28  34  36  42  46  48  52  58  64  66  72  76
  9  10  12  14  18  20  24  26  30  36  38  44  48  50  54  60  66  68  74  78
 13  14  16  18  22  24  28  30  34  40  42  48  52  54  58  64  70  72  78  82
 15  16  18  20  24  26  30  32  36  42  44  50  54  56  60  66  72  74  80  84
 19  20  22  24  28  30  34  36  40  46  48  54  58  60  64  70  76  78  84  88
 21  22  24  26  30  32  36  38  42  48  50  56  60  62  66  72  78  80  86  90
 25  26  28  30  34  36  40  42  46  52  54  60  64  66  70  76  82  84  90  94
 31  32  34  36  40  42  46  48  52  58  60  66  70  72  76  82  88  90  96 100
>>> m = matrix_factory(10, 20, fibonacci, N_of_x_plus_N_of_y)
>>> m.print(pretty=True)
   0    1    1    2    3    5    8   13   21   34   55   89  144  233  377  610  987 1597 2584 4181
   1    2    2    3    4    6    9   14   22   35   56   90  145  234  378  611  988 1598 2585 4182
   1    2    2    3    4    6    9   14   22   35   56   90  145  234  378  611  988 1598 2585 4182
   2    3    3    4    5    7   10   15   23   36   57   91  146  235  379  612  989 1599 2586 4183
   3    4    4    5    6    8   11   16   24   37   58   92  147  236  380  613  990 1600 2587 4184
   5    6    6    7    8   10   13   18   26   39   60   94  149  238  382  615  992 1602 2589 4186
   8    9    9   10   11   13   16   21   29   42   63   97  152  241  385  618  995 1605 2592 4189
  13   14   14   15   16   18   21   26   34   47   68  102  157  246  390  623 1000 1610 2597 4194
  21   22   22   23   24   26   29   34   42   55   76  110  165  254  398  631 1008 1618 2605 4202
  34   35   35   36   37   39   42   47   55   68   89  123  178  267  411  644 1021 1631 2618 4215
```


## Customization

### Custom formulas

Implementing a custom formula is as simple as subclassing Formula class and implementing the logic for building the correct sequence of numbers in its constructor, and the getter for an element:

```bash
>>> from skhub.numbers import *
>>> from skhub.matrix import *
>>> class MyFormula(Formula):
...     def __init__(self, m, n, number_generator):
...         super().__init__(m, n, number_generator)
...         self.numbers = list(islice(number_generator(), 0, m*n+3))
...     def get(self, x, y):
...         super().get(x, y)
...         return self.numbers[x*y+30]
...
>>> m = matrix_factory(10, 20, prime, MyFormula)
>>> m.print(pretty=True)
 127  127  127  127  127  127  127  127  127  127  127  127  127  127  127  127  127  127  127  127
 127  131  137  139  149  151  157  163  167  173  179  181  191  193  197  199  211  223  227  229
 127  137  149  157  167  179  191  197  211  227  233  241  257  269  277  283  307  313  331  347
 127  139  157  173  191  199  227  239  257  271  283  311  331  349  367  383  401  421  439  457
 127  149  167  191  211  233  257  277  307  331  353  379  401  431  449  467  499  523  563  587
 127  151  179  199  233  263  283  317  353  383  419  443  467  503  547  577  607  641  661  701
 127  157  191  227  257  283  331  367  401  439  467  509  563  599  631  661  709  751  797  829
 127  163  197  239  277  317  367  409  449  491  547  593  631  673  727  769  823  863  919  971
 127  167  211  257  307  353  401  449  499  563  607  653  709  761  823  877  937  991 1039 1093
 127  173  227  271  331  383  439  491  563  613  661  733  797  857  919  983 1039 1097 1171 1231
```


## Contributing

### Guidelines for contributors

-   Try to follow PEP conventions as much as possible (i.e.: use non-opinionated tools like [pycodestyle](https://github.com/PyCQA/pycodestyle)).
-   Try to have all code documented with docstrings and doctest. It takes literally a couple of minutes to type them and that pays off in the long run. Not because you wrote it you will always remember how to use it.
-   Try to maintain a stable interface for users between commits.
-   Try to avoid the usage of third-party as much as possible, so the chances of incurring into technical debt are mitigated.


## License

-   [MIT](https://opensource.org/licenses/MIT)
