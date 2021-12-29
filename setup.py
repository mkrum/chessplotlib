import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="chessplotlib",
    description="Chess plots with matplotlib",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(where="chessplotlib"),
    python_requires=">=3",
    install_requires=["matplotlib","numpy"]
)
