import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wombopy",
    version="0.2.3",
    description="A module to generate wombo.art images",
    author="AtomicDreamz",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "typer==0.9.0",
        "colorama==0.4.6",
        "shellingham==1.5.0post1",
        "pytest==7.3.1",
        "requests==2.31.0"
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7.13",
)
