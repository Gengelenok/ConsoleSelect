from setuptools import setup, find_packages

setup(
    name='conSel',
    version='1.0',
    packages=find_packages(),
    package_data={'': ['*.json'], },
    install_requires=[],  # Укажите зависимости, если они есть
    author='Gengelenok',
    author_email='gengelenok@gmail.com',
    description='Function for choosing from dictionary in console',
    url='https://github.com/Gengelenok/ConsoleSelect'
)
