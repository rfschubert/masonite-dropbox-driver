from setuptools import setup

setup(
    name="masonite-dropbox-driver",
    packages=[
        'masonite_dropbox_driver',
        'masonite_dropbox_driver.drivers',
        'masonite_dropbox_driver.providers',
    ],
    version='0.0.1',
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
