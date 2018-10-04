from setuptools import setup

setup(
    name="masonite-dropbox-driver",
    packages=[
        'masonite.contrib.dropbox',
        'masonite.contrib.dropbox.drivers',
        'masonite.contrib.dropbox.providers',
    ],
    version='0.0.5',
    install_requires=[
        'dropbox',
    ],
    classifiers=[],
    author='Bjorn Theart',
    author_email='bjorntheart@gmail.com',
    url='https://github.com/bjorntheart/masonite-dropbox-driver',
    description='Dropbox upload driver for the Masonite framework',
    keywords=['python web framework', 'python3', 'masonite', 'dropbox'],
    include_package_data=True,
)
