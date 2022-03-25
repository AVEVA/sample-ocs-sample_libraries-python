import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='ocs_sample_library_preview',
    version='0.7.1_preview',
    author='OSIsoft',
    license='Apache 2.0',
    author_email='dendres@osisoft.com',
    description='A preview of an OCS (OSIsoft Cloud Services) client library. Note: This library has been deprecated in favor of the AVEVA Data Hub library at https://pypi.org/project/adh-sample-library-preview/',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/osisoft/sample-ocs-sample_libraries-python',
    packages=setuptools.find_packages(),
    install_requires=[
        "adh_sample_library_preview>=0.7.1rc0",
    ],
    python_requires='>=3.7',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Development Status :: 7 - Inactive'
    ],
)
