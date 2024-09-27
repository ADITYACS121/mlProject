from setuptools import find_packages, setup

def parse_requirements(filename):
    """Load requirements from a requirements file, ignoring '-e .'"""
    with open(filename) as f:
        return [
            line.strip()
            for line in f
            if line.strip() and not line.startswith('#') and not line.startswith('-e')
        ]

setup(
    name='mlProject',  # Replace with your project name
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=parse_requirements('requirement.txt'),  # Dynamically load install_requires
)
