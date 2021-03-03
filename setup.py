# Copyright 2018-2019 Bernardo Fontes <https://github.com/berinhard/pyp5js/>

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.

#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup, find_packages

with open("requirements.txt") as fd:
    requirements = [l.strip() for l in fd.readlines()]

with open("README.md") as fd:
    long_description = fd.read()

with open("VERSION") as fd:
    version = fd.read().strip()

setup(
    name="pyp5js",
    version=version,
    description='Simple tool to allow to transcrypt Python code that uses P5.js',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Bernardo Fontes',
    maintainer='Bernardo Fontes',
    maintainer_email='bernardoxhc@gmail.com',
    url="https://github.com/berinhard/pyp5js/",
    license='GNU Lesser General Public License version 3',
    packages=find_packages(exclude=["pyp5js.tests"]),
    package_data={
        'pyp5js': [
            'assets/*',
            'assets/static/**/*',
            'templates/*',
            'http/templates/*',
            'http/static/*',
        ]
    },
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': ['pyp5js = pyp5js.cli:command_line_entrypoint']
    },
    python_requires='>=3.6',
    install_requires=requirements,
    keywords="p5js processing creative coding",
)
