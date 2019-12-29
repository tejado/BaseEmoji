import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="emojibase", # Replace with your own username
    version="0.0.1",
    author="tejado",
    author_email="tjado@maecke.de",
    description="Encode any data to emojis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tejado/BaseEmoji",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    include_package_data=True,
    install_requires=[
        "regex",
    ],
    #data_files=[('x', ['BaseEmoji/data/emojis.json'])],
)