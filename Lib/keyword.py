"""Keywords (from "Grammar/Grammar")

This file is automatically generated; please don't muck it up!

To update the symbols in this file, 'cd' to the top directory of
the python source tree and run:

    python3 -m Parser.pgen.keywordgen Grammar/Grammar \
                                      Grammar/Tokens \
                                      Lib/keyword.py

Alternatively, you can run 'make regen-keyword'.
"""

__all__ = ["iskeyword", "kwlist"]

kwlist = [
    'False',
    'Fałsz',
    'Nic',
    'None',
    'Prawda',
    'TODO_jak_to_nazwać',
    'True',
    'albo',
    'and',
    'anonim',
    'as',
    'assert',
    'async',
    'await',
    'break',
    'class',
    'continue',
    'def',
    'del',
    'dla',
    'dopóki',
    'elif',
    'else',
    'except',
    'finally',
    'for',
    'from',
    'global',
    'if',
    'import',
    'in',
    'inaczej',
    'is',
    'jako',
    'jest',
    'jeżeli',
    'klasa',
    'kontynuuj',
    'krzycz',
    'lambda',
    'lub',
    'nie',
    'nielokalny',
    'nonlocal',
    'not',
    'ode',
    'odpocznij',
    'or',
    'oraz',
    'ostatecznie',
    'pass',
    'poza',
    'przerwij',
    'raise',
    'return',
    'spośród',
    'spróbuj',
    'try',
    'usuń',
    'wewnątrz',
    'weźże',
    'while',
    'with',
    'wznieś',
    'yield',
    'zapewnij',
    'załaduj',
    'zwróć',
    'złap',
    'światowy'
]

iskeyword = frozenset(kwlist).__contains__
