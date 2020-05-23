import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="flush",
    version="0.0.1",
    author="Debesh Mandal",
    description="A poker package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/debeshmandal/illiteracy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)