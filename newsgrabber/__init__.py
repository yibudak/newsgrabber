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
    def __init__(self, sitemap_url: str) -> None:
        """NewsGrabber class to parse news articles from
        Google News Sitemap structure.

        Args:
            sitemap_url (str): URL of the sitemap.
        """
        self.name = urlparse(sitemap_url).netloc
        self.sitemap_url = sitemap_url
        self.network_manager = NetworkManager()
        self.sitemap_content = None
        self.news_urls = []

    def __str__(self):
        return f"NewsGrabber: {self.name}"

    def __repr__(self):
        return f"NewsGrabber[{self.name}]"

    def parse(self) -> bool:
        self.sitemap_content = self.network_manager.fetch_sitemap(self.sitemap_url)
        parser = SitemapParser(self.sitemap_content)
        self.news_urls = parser.parse()
        return True
