from setuptools import setup, find_packages

setup(
    name="hydraulics-solver",
    version="0.1.0",
    package_dir={"": "src"},  # Tells setuptools that the package is under src
    packages=find_packages(where="src"),  # Finds packages in src directory
)
