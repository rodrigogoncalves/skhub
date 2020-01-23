# skhub
A simple exercise with prime numbers.

This package contains a module for prime number checking and generation, and a module for printing matrices on the console.


## TOC

-   [Usage](#usage)
-   [Roadmap](#roadmap)
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
~/skhub$ python -m venv .
~/skhub$ source venv/bin/activate
```

### Make sure `prime.py` has execution bit set

```bash
(venv) ~/skhub$ chmod u+x algorithm/prime.py
```

### Use `get_n_primes` to retrieve a list of prime numbers up to `n`

```bash
(venv) ~/skhub$ chmod u+x algorithm/prime.py
(venv) ~/skhub$ ./algorithm/prime.py 10
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```


## Roadmap

1.  ~~Implement code to generate `n` prime numbers.~~
1.  Implement code to print a matrix on the console.
1.  Calculate timings for prime number generation code with inputs of different orders of magnitude.


## Contributing

### Guidelines for contributors

-   Try to follow PEP conventions as much as possible (i.e.: use non-opinionated tools like [pycodestyle](https://github.com/PyCQA/pycodestyle)).
-   Try to have all code documented with docstrings and doctest. It takes literally a couple of minutes to type them and that pays off in the long run. Not because you wrote it you will always remember how to use it.

### Improvement ideas

-   Implement more efficient algorithms for `prime` module.
-   Build distribution archives and deploy package to the Package Index.


## License

-   [MIT](https://opensource.org/licenses/MIT)
