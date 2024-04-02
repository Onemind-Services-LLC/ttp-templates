import os
from setuptools import find_packages, setup

# Read the contents of the README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

# Read the contents of the requirements file
with open(os.path.join(this_directory, "requirements.txt"), encoding="utf-8") as f:
    requirements = f.read().splitlines()

setup(
    name="ttp-templates",
    version="0.0.1",
    description="TTP templates collection",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Abhimanyu Saharan",
    author_email="asaharan@onemindservices.com",
    url="https://github.com/Onemind-Services-LLC/ttp-templates/",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    python_requires=">=3.8",
    zip_safe=False,
)
