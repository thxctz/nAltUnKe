from setuptools import setup, find_packages
setup(
    name ='animales'
    version



)

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ashleybuenosaludos",
    version="0.0.1",
    author="Ashley Bueno",
    author_email="adbueno2003@gmail.com",
    description="un paquete",
    long_description="Tarea de POO",
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)