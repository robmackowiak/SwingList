from setuptools import setup

setup(
    name='golf-driving-range',
    description='Golf Driving Range Scheduler',
    version='1.0.0',
    packages=['golf-driving-range'],
    include_package_data=True,
    install_requires=[
        "matplotlib",
        "numpy",
        "pandas",
        "scipy",
        "xarray"
    ]
)