from setuptools import setup, find_packages

# Read the requirements.txt file to get the dependencies
def parse_requirements(file_name):
    with open(file_name, 'r') as file:
        return [line.strip() for line in file.readlines() if line.strip() and not line.startswith('#')]

# Get the list of dependencies from the requirements.txt file
requirements = parse_requirements('requirements.txt')

setup(
    name='mlproject',
    version='0.1',
    author='muaazsiddique',  # Add your name
    author_email='muaazsiddique97@gmail.com',  # Add your email
    description='An end-to-end machine learning project',
    long_description=open('README.md').read(),  # Read the long description from README.md
    long_description_content_type='text/markdown',  # Or 'text/rst' for reStructuredText
    url='https://github.com/muaazsiddique/mlproject',  # Your project URL, e.g., GitHub repo
    packages=find_packages(),
    install_requires=requirements,  # Use the parsed requirements

    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.7',
    ],
    
    python_requires='>=3.7',  # Specify Python version requirements

    include_package_data=True,  # If you have non-Python files
    zip_safe=False,  # If your package includes non-Python files
)
