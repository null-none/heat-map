from setuptools import setup

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="heat-map",
    packages=["heat_map"],
    version="0.0.1",
    description="Draw image heatmaps in python",
    url="https://github.com/null-none/heat-mapy",
    keywords=["image", "heatmap", "heat map"],
    install_requires=required,
    classifiers=["Programming Language :: Python :: 3"],
    include_package_data=True,
)
