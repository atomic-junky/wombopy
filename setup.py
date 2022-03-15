from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='wombopy',
    version='0.1.2',
    description='A module to generate wombo.art images',
    author='Holy Tanuki',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['wombopy'],
    install_requires=[
        "typer==0.4.0",
        "colorama==0.4.4",
        "shellingham==1.4.0",
        "pytest==7.0.1",
        "requests==2.27.1",
    ],
    python_requires=">=3.9",
)
