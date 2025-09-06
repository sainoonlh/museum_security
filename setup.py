from setuptools import setup, find_packages

setup(
    name="museum-security",  # PyPI package name
    version="0.3",            # bump version!
    packages=find_packages(),
    description="Museum Security Project",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/sainoonlh/museum_security",
    author="Sai Noon Leng Harn",
    author_email="sainoonlengharn@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    project_urls={
        "Source": "https://github.com/sainoonlh/museum_security",
    },
    python_requires='>=3.6',
)
