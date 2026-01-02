"""Setup file."""

from setuptools import setup

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="fragua-sets",
    version="1.0",
    author="SagoDev",
    description="Package of fragua sets with reutilizable functions for ETL process.",
    packages=["fragua_sets"],
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.10",
    url="https://github.com/SagoDev/fragua-sets",
    install_requires=[
        "fragua",
    ],
)
