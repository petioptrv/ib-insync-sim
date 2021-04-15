#!/usr/bin/python3
# Adapted from 
# https://github.com/FedericoStra/cython-package-example/blob/master/setup.py

import os
from distutils.command.build_ext import build_ext
from typing import Callable

from setuptools import setup, Extension

from Cython.Build import cythonize

try:
    from Cython.Build import cythonize
    import numpy as np
except ImportError:
    cythonize = None
    np = None
import versioneer

WITH_DEBUG = False
CYTHONIZE = isinstance(cythonize, Callable)

print(f'CYTHONIZE {CYTHONIZE} - {cythonize}')
print(f'WITH_DEBUG {WITH_DEBUG}')


# https://cython.readthedocs.io/en/latest/src/userguide/source_files_and_compilation.html#distributing-cython-modules
def no_cythonize(extensions_, **_ignore):
    for extension in extensions_:
        sources = []
        for s_file in extension.sources:
            path, ext = os.path.splitext(s_file)
            if ext in ('.pyx', '.py'):
                if extension.language == 'c++':
                    ext = '.cpp'
                else:
                    ext = '.c'
                s_file = path + ext
            sources.append(s_file)
        extension.sources[:] = sources
    return extensions_


def build_extension(ext_name: str, with_np: bool = False) -> Extension:
    ext_path = ext_name.replace('.', os.path.sep) + '.pyx'
    include_dirs = []
    if with_np:
        include_dirs.append(np.get_include())
    extension = Extension(
        name=ext_name,
        sources=[ext_path],
        include_dirs=include_dirs,
        db_debug=WITH_DEBUG,
        language='c'
    )
    return extension


extensions = [
    build_extension('ib_sim.ib'),
]
if CYTHONIZE:
    compiler_directives = {'language_level': 3, 'embedsignature': True}
    extensions = cythonize(extensions, compiler_directives=compiler_directives)
else:
    extensions = no_cythonize(extensions)

install_options = {'build_ext': {'inplace': True}}
cmdclass = {'build_ext': build_ext} if CYTHONIZE else {}

install_requires = [
    'ib_insync >= 0.9.65, <1',
    'numpy >= 1.10, <2',
]

dev_requires = [
    'Cython',
    'pytest',
    'versioneer',
    'pylint',
    'pre-commit',
    'versioneer',
    'black',
    'flake8',
    'flake8-black',
    'twine',
    'sphinx',
    'sphinx_rtd_theme',
]

with open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

keywords = 'ibapi tws asyncio jupyter interactive brokers async cython testing'

setup(
    name='ib-sim',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(cmdclass=cmdclass),
    description='Testing/simulation framework for ib-insync',
    long_description=long_description,
    url='https://github.com/petioptrv/ib-insync-sim',
    author='Petio Petrov',
    author_email='petioptrv@icloud.com',
    license='BSD',
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Topic :: Office/Business :: Financial :: Investment',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords=keywords,
    packages=['ib_sim'],
    package_data={'ib_sim': ['*.pxd']},
    include_package_data=True,
    ext_modules=extensions,
    options=install_options,
    install_requires=install_requires,
    extras_require={
        'dev': dev_requires,
        'docs': ['sphinx', 'sphinx-rtd-theme']
    },
    zip_safe=False,
)
