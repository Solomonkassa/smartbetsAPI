from setuptools import setup
from smartbets_API import __version__, __author__


def get_file(nm: str) -> str:
    with open(nm) as file:
        return file.readlines()


setup(
    name="smartbetsAPI",
    packages=["smartbets_API"],
    version=__version__,
    install_requires=get_file("requirements.txt"),
    url="https://github.com/Simatwa/smartbetsAPI.git",
    license="GPL-3.0",
    author=__author__,
    author_email="smartwacaleb@gmail.com",
    maintainer="Smartwa Caleb",
    maintainer_email="smartwacaleb@gmail.com",
    description="Simple football prediction API",
    long_description="\n".join(get_file("README.md")),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Punters",
        "Intended Audience :: Bookmarkers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Soccer Predictions  :: Quality Assurance",
        "Topic :: Betting API",
    ],
    package_data={
        "smartbets_API": [
            "examples/bet_at_api_level.py",
            "examples/predict_using_dict.py",
            "examples/predict_using_list.py",
        ]
    },
    keywords=[
        "Betting",
        "Football",
        "Predictions",
        "Betting API",
        "Soccer predictions",
        "Football Predictions",
    ],
    entry_points={
        "console_scripts": ["smartbetsAPI = smartbets_API.interface:start_server"],
    },
)
