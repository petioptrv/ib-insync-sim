#!/usr/bin/python3
# Adapted from 
# https://github.com/FedericoStra/cython-package-example/blob/master/setup.py

import os
from setuptools import setup, Extension

try:
    from Cython.Build import cythonize
except ImportError:
    cythonize = None


# # https://cython.readthedocs.io/en/latest/src/userguide/source_files_and_compilation.html#distributing-cython-modules
# def no_cythonize(extensions, **_ignore):
#     for extension in extensions:
#         sources = []
#         for sfile in extension.sources:
#             path, ext = os.path.splitext(sfile)
#             if ext in ('.pyx', '.py'):
#                 if extension.language == 'c++':
#                     ext = '.cpp'
#                 else:
#                     ext = '.c'
#                 sfile = path + ext
#             sources.append(sfile)
#         extension.sources[:] = sources
#     return extensions


def build_extension(ext_name: str) -> Extension:
    ext_path = ext_name.replace('.', os.path.sep)+'.pyx'
    extension = Extension(name=ext_name, sources=[ext_path])
    return extension


extensions = [
    build_extension('ib_sim.ib'),
    build_extension('ib_sim.main'),
    # Extension(
    #     'cypack.sub.wrong',
    #     ['src/cypack/sub/wrong.pyx', 'src/cypack/sub/helper.c']
    # ),
]

# CYTHONIZE = bool(int(os.getenv('CYTHONIZE', 0))) and cythonize is not None

# if CYTHONIZE:
#     compiler_directives = {'language_level': 3, 'embedsignature': True}
#     extensions = cythonize(
#         extensions, compiler_directives=compiler_directives
#     )
# else:
#     extensions = no_cythonize(extensions)
compiler_directives = {'language_level': 3, 'embedsignature': True}
extensions = cythonize(
    extensions, compiler_directives=compiler_directives, build_dir='build'
)

with open('requirements.txt') as fp:
    install_requires = fp.read().strip().split('\n')

with open('requirements-dev.txt') as fp:
    dev_requires = fp.read().strip().split('\n')

setup(
    packages=['sim_ib'],
    include_package_data=True,
    ext_modules=extensions,
    install_requires=install_requires,
    extras_require={
        'dev': dev_requires,
        'docs': ['sphinx', 'sphinx-rtd-theme']
    },
)
