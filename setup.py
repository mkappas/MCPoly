import setuptools

with open('README.md') as readme_file:
    README = readme_file.read()

setup_args = dict(
    name='MCPoly',
    version='0.0.2',
    description='Useful tools for Computational Chemistry for polymers',
    long_description_content_type="text/markdown",
    long_description=README
    license='MIT',
    packages=find_packages(),
    author='Omicron Fluor',
    author_email='cxs454@student.bham.ac.uk',
    keywords=['ORCA', 'Mechanical Property', 'Computational Chemistry'],
    url='https://github.com/Omicron-Fluor/MCPoly/',
)

install_requires = [
    'ase>=3.23',
    'ipywidgets>=8.0.0',
    'numpy>=1.22.0',
    'matplotlib>=3.6.0',
    'pandas>=1.4.0',
    'seaborn>=0.11.0',
    'py3dmol>=2.0.0',
    'rdkit>=2022.9.3',
    'scikit-learn>=1.1.2',
    're',
    'os'
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires,include_package_data=True)
