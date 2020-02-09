from setuptools import setup

setup(
    name='notly',
    packages=['notly'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask_session',
        'markupsafe'
    ],
)
