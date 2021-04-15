#!/usr/bin/python3
# Adapted from 
# https://github.com/FedericoStra/cython-package-example/blob/master/setup.py

import os
from setuptools import setup, Extension, dist

# https://stackoverflow.com/questions/54117786/add-numpy-get-include-argument-to-setuptools-without-preinstalled-numpy
# dist.Distribution().fetch_build_eggs(
#     ['Cython>=0.15.1', 'numpy>=1.10']
# )

try:
    from Cython.Build import cythonize
except ImportError:
    cythonize = None
import numpy as np  # noqa: E402
import versioneer  # noqa

WITH_DEBUG = False


def build_extension(ext_name: str, with_np: bool = False) -> Extension:
    ext_path = ext_name.replace('.', os.path.sep)+'.pyx'
    include_dirs = []
    # if with_np:
    #     include_dirs.append(np.get_include())
    extension = Extension(
        name=ext_name,
        sources=[ext_path],
        include_dirs=include_dirs,
        db_debug=WITH_DEBUG,
    )
    return extension


extensions = [
    build_extension('ib_sim.ib'),
    # Extension(
    #     'cypack.sub.wrong',
    #     ['src/cypack/sub/wrong.pyx', 'src/cypack/sub/helper.c']
    # ),
]

compiler_directives = {'language_level': 3, 'embedsignature': True}
extensions = cythonize(
    extensions, compiler_directives=compiler_directives, build_dir='build'
)

install_requires = [
    'ib_insync >= 0.9.65, <1',
    'Cython >= 0.15.1',
    'numpy >= 1.10, <2',
]

dev_requires = [
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
    cmdclass=versioneer.get_cmdclass(),
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
    include_package_data=True,
    ext_modules=extensions,
    install_requires=install_requires,
    extras_require={
        'dev': dev_requires,
        'docs': ['sphinx', 'sphinx-rtd-theme']
    },
)
