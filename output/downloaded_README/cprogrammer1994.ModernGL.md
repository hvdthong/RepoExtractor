<div align="center">

[![preview](https://github.com/cprogrammer1994/ModernGL/raw/master/.github/preview.png)](#readme)

</div>

# ModernGL

```sh
pip install ModernGL
```

- [Documentation](https://moderngl.readthedocs.io/)
- [Examples](https://github.com/cprogrammer1994/ModernGL/tree/master/examples/#readme)
- [ModernGL on Github](https://github.com/cprogrammer1994/ModernGL/)
- [ModernGL on PyPI](https://pypi.org/project/ModernGL/)

## Features

- GPU accelerated high quality graphics
- Rendering modern OpenGL scenes with less headache
- Simpler and faster than PyOpenGL
- Can render without a window
- 100% Pythonic

## Sample usage

```py
>>> import moderngl
>>> ctx = moderngl.create_standalone_context()
>>> buf = ctx.buffer(b'Hello World!')  # allocated on the GPU
>>> buf.read()
b'Hello World!'
```

For complete examples please visit the [Examples](https://github.com/cprogrammer1994/ModernGL/tree/master/examples/#readme).

## Easy to use with Pillow and Numpy

```py
>>> img = Image.open('texture.jpg')
>>> ctx.texture(img.size, 3, img.tobytes())
<Texture: 1>
```

```py
>>> ctx.buffer(np.array([0.0, 0.0, 1.0, 1.0], dtype='f4'))
<Buffer: 1>
```

## Compared to PyOpenGL

With the original OpenGL API you have to write a couple of lines to achieve a **simple task** like compiling a shader or running a computation on the GPU. With ModernGL you will need just a **few lines** to achieve the same result.

#### Using PyOpenGL

```py
vbo1 = glGenBuffers(1)
GL.glBindBuffer(GL_ARRAY_BUFFER, vbo1)
GL.glBufferData(GL_ARRAY_BUFFER, b'Hello World!', GL_STATIC_DRAW)

vbo2 = glGenBuffers(1)
GL.glBindBuffer(GL_ARRAY_BUFFER, vbo2)
GL.glBufferData(GL_ARRAY_BUFFER, b'\x00' * 1024, GL_DYNAMIC_DRAW)
```

#### Using ModernGL

```py
vbo1 = ctx.buffer(b'Hello World!')
vbo2 = ctx.buffer(reserve=1024, dynamic=True)
```

## Build

[![build](https://img.shields.io/travis/cprogrammer1994/ModernGL/master.svg?label=build)](https://travis-ci.org/cprogrammer1994/ModernGL)
[![build](https://img.shields.io/appveyor/ci/cprogrammer1994/ModernGL/master.svg?label=build)](https://ci.appveyor.com/project/cprogrammer1994/ModernGL)

```sh
python setup.py build_ext --inplace
```

## FAQ

### Is ModernGL faster than PyOpenGL?

In some cases **yes**, the core functions of ModernGL are written in C++, OpenGL functions are called in quick succession so these calls together count as a single python function call.

### What version of OpenGL is used?

Most of the calls only require **OpenGL 3.3** but Subroutines and Compute Shaders require **OpenGL 4.0** and **OpenGL 4.3**

### Is my old PC supported?

OpenGL 3.3 came out in February 2010. With **up to date drivers** you will be able to use the most of the ModernGL functions, even on integrated graphics cards. _(No, Compute Shaders won't work)_

### Where can I use ModernGL?

**Anywhere where OpenGL is supported.** ModernGL is capable of rendering using a [standalone_context] as well. Rendering to a window only requires a valid OpenGL context.

[standalone_context]: https://github.com/cprogrammer1994/ModernGL/tree/master/examples/standalone

### Can ModernGL create a Window?

**NO**, Window creation is up to you. You can choose from a large variety of modules that can create a window: [PyQt5], [pyglet], [pygame], [GLUT] and many others.

[PyQt5]: https://pypi.org/project/PyQt5/
[pyglet]: https://bitbucket.org/pyglet/pyglet/wiki/Home
[pygame]: https://www.pygame.org/news
[GLUT]: https://wiki.python.org/moin/PyOpenGL

### Limitations using ModernGL over PyOpenGL?

All the neccessary calls are (or can be) implemented in ModernGL. However you can interract with the ModernGL objects from PyOpenGL. If something is missing write an [issue](https://github.com/cprogrammer1994/ModernGL/issues) or raise a [PR](https://github.com/cprogrammer1994/ModernGL/pulls).

## Supported platforms

- [x] Windows
- [x] Linux
- [x] Mac

## Installing from source

### Installing on Ubuntu from source

```sh
apt-get install python3-dev libgl1-mesa-dev libx11-dev
python3 setup.py install
```

### Building the sphinx documentation

```sh
pip install -r docs/requirements.txt
python setup.py build_sphinx
```

### Running tests

```sh
pytest
```

> Some of the tests may be skipped when the supported OpenGL version is below the requirements of the given test.

### Headless rendering

```sh
apt-get install xvfb
alias xpy='xvfb-run -s "-screen 0 1x1x24" python3'
xpy -m ModernGL
```

## Code quality

Code is tested with [pep8], [flake8], [prospector] and [pylint]

[pep8]: https://www.python.org/dev/peps/pep-0008/
[flake8]: http://flake8.pycqa.org/en/latest/
[prospector]: https://prospector.landscape.io/en/master/
[pylint]: https://www.pylint.org/

## Community

- [Code of conduct](https://github.com/cprogrammer1994/ModernGL/blob/master/.github/CODE_OF_CONDUCT.md)

## Contributors

- [Szabolcs Dombi](https://github.com/cprogrammer1994)
- [SimLeek](https://github.com/SimLeek)
- [Aljenci](https://github.com/Aljenci)
- [MinchinWeb](https://github.com/MinchinWeb)
- [Silexstudio](https://github.com/Silexstudio)
- [stuaxo](https://github.com/stuaxo)
- [Tomi Aarnio](https://github.com/toaarnio)
- [Joshua Reibert](https://github.com/joshua-r)

and [many others](https://github.com/cprogrammer1994/ModernGL/graphs/contributors)

Thank You!

Contributions are welcome. _(Please add yourself to the list)_
