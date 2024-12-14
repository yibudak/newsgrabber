# Copyright (C) 2024 Ahmet Yiğit Budak (https://github.com/yibudak)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
import datetime

from newsgrabber import utils
from newsgrabber import NewsGrabber
from newsgrabber import NetworkManager


def test_parse_iso8601_date():
    assert utils.parse_iso8601_date("2018-01-12T21:57:27Z") == datetime.datetime(
        year=2018,
        month=1,
        day=12,
        hour=21,
        minute=57,
        second=27,
        tzinfo=datetime.timezone.utc,
    )
    assert utils.parse_iso8601_date("1997-07-16T19:20:30+01:00") == datetime.datetime(
        year=1997,
        month=7,
        day=16,
        hour=19,
        minute=20,
        second=30,
        tzinfo=datetime.timezone(datetime.timedelta(seconds=3600)),
    )
    assert utils.parse_iso8601_date("2024-01-01") == datetime.datetime(
        year=2024, month=1, day=1
    )
    assert utils.parse_iso8601_date("2024-01-01T00:00:00") == datetime.datetime(
        year=2024, month=1, day=1
    )


# NewsGrabber Class Methods


def test__get_domain_name():
    ng = NewsGrabber("https://example.com/sitemap.xml")
    assert ng._get_domain_name() == "example.com"


def test__build_network_manager():
    # Without any extra parameters
    ng = NewsGrabber("https://example.com/sitemap.xml")
    network_manager = NetworkManager()
    assert ng.network_manager.session.proxies == network_manager.session.proxies
    assert ng.network_manager.timeout == network_manager.timeout

    # With Proxy Dict
    proxy_dict = {"http": "socks5://127.0.0.1:1080", "https": "socks5://127.0.0.1:1080"}
    ng = NewsGrabber(
        "https://example.com/sitemap.xml",
        proxy=proxy_dict
    )
    network_manager = NetworkManager(proxy=proxy_dict)
    assert ng.network_manager.session.proxies == network_manager.session.proxies
    assert ng.network_manager.timeout == network_manager.timeout

    # With Timeout Parameter
    timeout = 30
    ng = NewsGrabber("https://example.com/sitemap.xml", timeout=timeout)
    network_manager = NetworkManager(timeout=timeout)
    assert ng.network_manager.timeout == network_manager.timeout


# TODO: Add more tests
