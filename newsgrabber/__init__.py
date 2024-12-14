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
from urllib.parse import urlparse

from .network_manager import NetworkManager
from .parser import SitemapParser


class NewsGrabber:
    def __init__(self, sitemap_url: str, timeout=15, proxy=None) -> None:
        """NewsGrabber class to parse news articles from
        Google News Sitemap structure.

        Args:
            sitemap_url (str): URL of the sitemap.
            timeout (int, optional): Request timeout. Defaults to 15.
            proxy (_type_, optional): Proxy JSON in dict format. Defaults to None.
        """
        self.sitemap_url = sitemap_url
        self.name = self._get_domain_name()
        self.timeout = timeout
        self.proxy = proxy
        self.network_manager = self._build_network_manager()

        # Placeholder attributes
        self.sitemap_content = None
        self.news_urls = []

    def _build_network_manager(self) -> NetworkManager:
        return NetworkManager(proxy=self.proxy, timeout=self.timeout)

    def _get_domain_name(self) -> str:
        return urlparse(self.sitemap_url).netloc

    def __str__(self):
        return f"NewsGrabber: {self.name}"

    def __repr__(self):
        return f"NewsGrabber[{self.name}]"

    def parse(self) -> bool:
        self.sitemap_content = self.network_manager.fetch_sitemap(self.sitemap_url)
        parser = SitemapParser(self.sitemap_content)
        self.news_urls = parser.parse()
        return True
