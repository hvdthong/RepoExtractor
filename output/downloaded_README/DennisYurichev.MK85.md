# MK85 - toy-level, simple SMT solver under ~3000 SLOC of C++

It's very early sneak preview.
It supports only bools and bitvecs. No integers, let alone reals and arrays and tuples and whatnot.
Its complexity is comparable to simple LISP interpreter.

However, it can serve as education tool (hopefully).
This is also my playground.

It parses input SMT-LIB file (see "tests" and "examples"), constructs digital circuit, which is then converted to CNF form using Tseitin transformations.
This is also called "bitblasting".

Stay tuned, it will be evolved.

Requires: flex/bison.
In Ubuntu Linux, type "make".
It wasn't checked on other OS-es.

Since it's early preview, it was only checked on "tests" and "examples" you can find here.
Anything else can fail.
Also, error reporting is somewhat user-unfriendly.
First, you can check your .smt files using other SMT solver (I used z3, Boolector, STP, Yices, CVC4).

## Thanks

[Armin Biere](http://fmv.jku.at/biere/) patiently helped with my endless boring-to-death questions.

Xenia Galinskaya, for support.

## Installation

	make

	sudo make install (copies python files and .so library to dist-package...)

## Non-standard SMT-LIB commands

Aside from SMT-LIB standard, I also added two more commands: (get-all-models) and (count-models) (see "tests").

## Non-standard SMT-LIB functions

bvmul_no_overflow, see: https://github.com/DennisYurichev/MK85/blob/master/examples/surd.smt

## Name

It was previously named "ToySMT", but then I got to know about existence of another project called [toysmt](https://github.com/msakai/toysolver).

Since other SMT-solvers use cryptic acronyms as names, and since the name of Z3 has probably been taken from [Z3 computer](https://en.wikipedia.org/wiki/Z3_%28computer%29),
I choose a "MK85" name (after Soviet programmable calculator [Elektronika MK-85](http://www.leningrad.su/museum/show_calc.php?n=224)).

## History

I've written many SAT examples in Python, based on my Python library (or API):
https://github.com/DennisYurichev/SAT_SMT_article/blob/master/libs/Xu.py
Many SAT Python-based examples has been published in my blog: https://yurichev.com/blog/

And at some point I realised I can do simple SMT-solver, I need only to add parser and keep tabs on variables.
This is what I did.

Hence, in order to fully understand MK85, you can first try to understand my SAT Python-based examples.

21-Jan-2018: minimize/maximize using Open-WBO solver: https://github.com/DennisYurichev/MK85/blob/master/optimization.md

31-Jan-2018: PicoSAT and incremental SAT. Thanks to incremental SAT, examples involving model counting/enumeration are now way faster, including these:
https://github.com/DennisYurichev/MK85/blob/master/examples/factorize.smt
https://github.com/DennisYurichev/MK85/blob/master/examples/2.smt
https://github.com/DennisYurichev/MK85/blob/master/examples/3.smt

## Internals

There are two main structures.

"struct expr" used during parsing.

"struct SMT_var" is a "high level" structure reflecting each SMT variable, which can be bool or bitvector.
The structure has linked "SAT_var", which is number of variable on SAT level + width.
For boolean, only one SAT variable is used.
For bitvector of width w, SMT variable occupies [SAT_var, SAT_var+w-1] SAT variables.

## Extreme simplicity

It has no optimizations at all.
If it encounters two "(bvadd x y)", two adders would be generated instead of one.
Maybe SAT-solver (minisat/picosat in this case) could optimize this out, or maybe not.

## Further reading

I've found these papers/articles/books helpful: 

* [Armin Biere - Using High Performance SAT and QBF Solvers](http://fmv.jku.at/biere/talks/Biere-TPTPA11.pdf)
* https://en.wikipedia.org/wiki/Tseytin_transformation
* [Martin Finke - Equisatisfiable SAT Encodings of Arithmetical Operations](http://www.martin-finke.de/documents/Masterarbeit_bitblast_Finke.pdf)

* Henry Warren - Hacker's Delight.
Some people say these branchless tricks and hacks were only relevant for old RISC CPUs, so you don't need to read it.
Nevertheless, these hacks and understanding them helps immensely to get into boolean algebra and all the mathematics.

