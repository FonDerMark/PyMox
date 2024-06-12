from setuptools import setup, find_packages

setup(
    name='pymox',
    version='0.0.1',
    description='Custom library similar to Proxmoxer',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Ваше Имя',
    author_email='ваш_email@example.com',
    url='https://github.com/ваш_проект/pymox',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        # Ваши зависимости
    ],
)
