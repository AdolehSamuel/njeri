from setuptools import setup, find_packages

setup(
    name="njeri-job-search",
    version="1.0.0",
    description="A job search application for women connecting to Fairygodboss resources",
    author="Njeri Team",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "njeri=main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
