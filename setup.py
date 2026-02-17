from setuptools import setup, find_packages

setup(
    name="Topsis-Ayushi-102317237",
    version="1.0.0",
    author="Ayushi",
    description="TOPSIS Implementation using Python",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy"
    ],
    entry_points={
        'console_scripts': [
            'topsis=topsis_package.topsis:main'
        ]
    },
)
