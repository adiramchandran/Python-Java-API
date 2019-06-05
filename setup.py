import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyjav_api_adarshr2",
    version="0.0.1",
    author="Adarsh Ramchandran",
    author_email="adarsh.ramchandran@gmail.com",
    description="example API for making requests of Python models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)