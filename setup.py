from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="dry2life-platform",
    version="1.0.0",
    author="Asmaa Alaa",
    author_email="asmaaalaatohamy@gmail.com",
    description="Bio-Digital Intelligence Platform for Soil Salinity Management",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/moamn/DRY2LIFE-BioDigital-Platform",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Agriculture",
        "Development Status :: 4 - Beta",
    ],
    python_requires=">=3.8",
    install_requires=[
        "streamlit>=1.28.0",
        "pandas>=2.0.0",
        "numpy>=1.24.0",
        "plotly>=5.15.0",
    ],
)