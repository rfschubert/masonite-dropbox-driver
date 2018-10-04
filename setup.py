from setuptools import setup

setup(
    name="masonite-dropbox-driver",
    packages=[
        'masonite',
        'masonite.contrib',
        'masonite.contrib.drivers',
        'masonite.contrib.providers',
    ],
    version='0.0.2',
    install_requires=[
        'dropbox',
    ],
    classifiers=[],
    author='Bjorn Theart',
    author_email='bjorntheart@gmail.com',
    url='https://github.com/bjorntheart',
    description='Dropbox upload driver for the Masonite framework',
    keywords=['python web framework', 'python3', 'masonite', 'dropbox'],
    include_package_data=True,
)
