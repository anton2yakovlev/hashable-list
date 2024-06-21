from setuptools import setup, find_packages

setup(
    name="hashable-list",
    version="0.2.0",
    packages=find_packages(),
    description="A hashable list type in Python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/anton2yakovlev/hashable-list",
    author="Anton Yakovlev",
    author_email="anton2yakovlev@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.9",
)
