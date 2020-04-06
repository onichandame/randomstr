import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="randomstr", # Replace with your own username
    version="0.0.4",
    author="onichandame",
    author_email="zxinmyth@gmail.com",
    description="a random string generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/onichandame/randomstring",
    packages=setuptools.find_packages(),
    install_requires=[
        "rstr"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
