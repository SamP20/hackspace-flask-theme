from setuptools import setup, find_namespace_packages

setup(
    name='bristolhackspace.flask_theme',
    packages=find_namespace_packages(include=['bristolhackspace.*']),
    package_data={
        "bristolhackspace.flask_theme": ["*"],
    },
    install_requires=[
        "flask>=2.0",
    ]
)