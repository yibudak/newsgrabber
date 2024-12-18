NewsGrabber: Google News Sitemap Parser
=======================================

|PyPI version| |Python versions| |Codacy-quality| |Codecov| |License|

**NewsGrabber** is a Python library that parses Google News sitemap
structures into Python objects, enabling developers to easily extract
and analyze news-related metadata.

Features
--------

-  Parses Google News sitemaps into structured Python objects.
-  Handles sitemap parsing with robust error tolerance.
-  Lightweight and efficient, leveraging:

   -  **lxml** for fast XML parsing.
   -  **requests** for HTTP requests.
   -  **python-dateutil** for flexible date parsing.

-  Python 3.11+ compatible.

Installation
------------

Install NewsGrabber via pip:

.. code:: bash

   pip install newsgrabber

Usage
-----

Parsing a Google News Sitemap
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

   from newsgrabber import NewsGrabber

   grabber = NewsGrabber("https://www.bbc.com/sitemaps/https-sitemap-com-news-1.xml")
   grabber.parse()
   print("\n".join(x.title for x in grabber.news_urls[:5]))

Example Output
~~~~~~~~~~~~~~

.. code:: plaintext

   BBC Look East: Latest weather forecast for the East
   Syria country profile
   Namibia country profile
   How working parents can get 15 and 30 hours free childcare
   South East England weather forecast

Requirements
------------

NewsGrabber requires Python 3.11+ and the following dependencies:

-  **lxml>=5.3.0**: For XML parsing.
-  **requests>=2.32.3**: For HTTP requests.
-  **python-dateutil>=2.1,<3.0.0**: For flexible date parsing.

Development and Testing
-----------------------

To set up a development environment:

1. Clone the repository:
   ``bash  git clone https://github.com/yibudak/newsgrabber  cd newsgrabber``
2. Install dependencies: ``bash  pip install -e .[test]``
3. Run tests: ``bash  pytest``

Contributing
------------

Contributions are welcome! If you’d like to contribute, please fork the
repository and submit a pull request. Make sure to include tests for any
new functionality.

License
-------

This library is licensed under the AGPL-3.0 License.

.. |PyPI version| image:: https://img.shields.io/pypi/v/newsgrabber
   :target: https://pypi.org/project/newsgrabber/
.. |Python versions| image:: https://img.shields.io/pypi/pyversions/newsgrabber
   :target: https://pypi.org/project/newsgrabber/
.. |License| image:: https://img.shields.io/pypi/l/newsgrabber
   :target: https://raw.githubusercontent.com/yibudak/newsgrabber/main/LICENCE
.. |Codacy-quality| image:: https://app.codacy.com/project/badge/Grade/596a51d1dd004f8ea76bbdc15caa463d
   :target: https://app.codacy.com/gh/yibudak/newsgrabber/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade
.. |Codecov| image:: https://codecov.io/github/yibudak/newsgrabber/graph/badge.svg?token=ZL6M47HN3L
   :target: https://codecov.io/github/yibudak/newsgrabber
