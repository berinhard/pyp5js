from setuptools import setup, find_packages

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
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': ['pytop5 = pyp5js.cli:command_line_entrypoint']
    },
    python_requires='>=3.6',
    install_requires=[
        'Click==7.0',
        'cprint==1.1',
        'Jinja2==2.10.1',
        'PyYAML==5.1',
        'Transcrypt==3.7.12',
        'Unipath==1.1',
    ],
)
