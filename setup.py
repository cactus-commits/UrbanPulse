from setuptools import setup, find_packages

setup(
    name="bokoll",
    packages=find_packages(where="bokoll/src"),
    package_dir={"": "bokoll/src"},
)