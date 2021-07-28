import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyodide-html",
    version="0.0.1",
    author="Xing Han Lu",
    author_email="github@xinghanlu.com",
    description="HTML elements for pyodide, implemented as Python functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xhlulu/pyodide-html",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=[],
)