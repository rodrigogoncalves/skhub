# skhub
A simple exercise with matrices and number generators.

This package contains a module with prime and fibonacci number generators, and a module for handling matrices.

The `matrix` module contains a factory function for generating matrices of a given size, with a given number generator, and a given formula to compute each element of the matrix.


## TOC

-   [Usage](#usage)
-   [Contributing](#contributing)
-   [License](#license)


## Usage

### Clone project

```bash
~$ git clone https://github.com/rodrigogoncalves/skhub
~$ cd skhub
```

### Create and activate a virtual environment

```bash
~/skhub$ python -m venv venv
~/skhub$ source venv/bin/activate
```

### Run tests

```bash
(venv) ~/skhub$ pytest
```

### Use the package to generate some matrices and print them on the console

```
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


## Contributing

### Guidelines for contributors

-   Try to follow PEP conventions as much as possible (i.e.: use non-opinionated tools like [pycodestyle](https://github.com/PyCQA/pycodestyle)).
-   Try to have all code documented with docstrings and doctest. It takes literally a couple of minutes to type them and that pays off in the long run. Not because you wrote it you will always remember how to use it.
-   Try to maintain a stable interface for users between commits.
-   Try to avoid the usage of third-party as much as possible, so the chances of incurring into technical debt are mitigated.


## License

-   [MIT](https://opensource.org/licenses/MIT)
