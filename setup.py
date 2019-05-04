from setuptools import setup, find_packages

with open("requirements.txt") as fd:
    requirements = [l.strip() for l in fd.readlines()]

with open("README.md") as fd:
    long_description = fd.read()

setup(
    name="pyp5js",
    version="0.0.1",
    description='Simple tool to allow to transcrypt Python code that uses P5.js',
    long_description=long_description,
    author='Bernardo Fontes',
    maintainer='Bernardo Fontes',
    maintainer_email='bernardoxhc@gmail.com',
    license='GPL 3',
    packages=find_packages(),
    package_data={
        'pyp5js': [
            'assets/*',
            'static/*',
            'templates/*',
        ]
    },
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': ['pytop5js = pyp5js.cli:command_line_entrypoint']
    },
    python_requires='>=3.6',
    install_requires=requirements,
)
