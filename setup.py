from setuptools import find_packages, setup

from newsgrabber import __about__ as about


def __readme():
    with open("README.md", mode="r", encoding="utf-8") as f:
        return f.read()


tests_require = [
    # Mock HTTP server
    "requests_mock>=1.6.0,<2.0",
    # Running tests
    "pytest>=2.8",
]

setup(
    name="newsgrabber",
    version=about.__version__,
    description=" Google News Sitemap Parser",
    long_description=__readme(),
    author=about.__author__,
    author_email=about.__email__,
    url="https://github.com/mediacloud/ultimate-sitemap-parser",
    license="AGPL-3.0",
    keywords="sitemap, google news, parser",
    packages=find_packages(exclude=["tests"]),
    zip_safe=True,
    python_requires=">=3.11",
    install_requires=[
        # Parsing arbitrary dates (sitemap date format is standardized
        # but some implementations take liberties)
        "python-dateutil>=2.1,<3.0.0",
        # For parsing XML
        "lxml>=5.3.0",
        # For making HTTP requests
        "requests>=2.32.3",
    ],
    setup_requires=[
        # Running tests as part of setup.py
        "pytest-runner>=4.2,<5.0",
    ],
    tests_require=tests_require,
    extras_require={
        "test": tests_require,
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Internet :: WWW/HTTP :: Indexing/Search",
        "Topic :: Text Processing :: Indexing",
        "Topic :: Text Processing :: Markup :: XML",
    ],
)
