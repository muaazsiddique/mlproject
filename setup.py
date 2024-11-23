from setuptools import setup, find_packages

def parse_requirements(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('#')]
setup(
    name="mlproject",
    version="0.1.0",
    description="A Python package for training and predicting with a Random Forest ML model.",
    author="Muaaz Siddique",
    author_email="your.email@example.com",
    packages=find_packages(),  # Automatically find all packages
    install_requires=parse_requirements('requirements.txt'),  # Use requirements.txt,
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
