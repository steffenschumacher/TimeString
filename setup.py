import setuptools

desc = "TimeString converts eg. 1w2d to 216 hours or datetime.timedelta or vice versa"
setuptools.setup(
    name="timestring",
    version="0.0.1",
    author="Steffen Schumacher",
    author_email="ssch@wheel.dk",
    description=desc,
    long_description=desc,
    long_description_content_type="text/markdown",
    url="https://github.com/steffenschumacher/TimeString.git",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
