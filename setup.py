from setuptools import setup, find_packages

setup(
    name='myrino',
    version='1.1',
    author='amirali irvany',
    author_email='dev.metect@gmail.com',
    description='myrino is an api-based library for Rubino messengers',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/metect',
    install_requires=['requests'],
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.6',
)
