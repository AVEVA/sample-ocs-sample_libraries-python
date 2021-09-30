import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='ocs_sample_library_preview',
    version='0.4.2_preview',
    author='OSIsoft',
    license='Apache 2.0',
    author_email='dendres@osisoft.com',
    description='A preview of an OCS (OSIsoft Cloud Services) client library',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/osisoft/sample-ocs-sample_libraries-python',
    packages=setuptools.find_packages(),
    install_requires=[
        'requests>=2.26.0',
        'python-dateutil>=2.8.2',
        'jsonpatch>=1.32'
    ],
    python_requires='>=3.9',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
)
