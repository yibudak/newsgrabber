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
from lxml import etree

from .models.news_url import NewsUrl
from .utils import parse_iso8601_date


class SitemapParser:
    def __init__(self, sitemap_content):
        self.sitemap_content = sitemap_content
        self.xml_tree = etree.XML(self.sitemap_content)
        self.namespaces = self._build_namespaces()

    def _build_namespaces(self) -> dict:
        namespaces = self.xml_tree.nsmap

        if "news" not in namespaces:
            raise ValueError("News namespace not found in the sitemap.")

        if "image" not in namespaces:
            namespaces["image"] = "http://www.google.com/schemas/sitemap-image/1.1"

        return namespaces

    def _parse_loc(self, datum, el) -> bool:
        if el is None:
            # because its the only required element
            raise ValueError(
                "loc element not found in the sitemap."
            )  # Todo: check if this necessary
        datum["url"] = el.text
        return True

    def _parse_lastmod(self, datum, el) -> bool:
        if el is not None:
            datum["last_modification"] = el.text
        return True

    def _parse_publication(self, datum, el) -> bool:
        name = el.find("news:name", self.namespaces)
        language = el.find("news:language", self.namespaces)
        datum["publication_name"] = name.text
        datum["language"] = language.text
        return True

    def _parse_news(self, datum, el) -> bool:
        # Required elements
        title = el.find("news:title", self.namespaces)
        publication_date = el.find("news:publication_date", self.namespaces)
        datum["title"] = title.text
        datum["publication_date"] = parse_iso8601_date(publication_date.text)
        self._parse_publication(datum, el.find("news:publication", self.namespaces))

        # Optional elements
        keywords = el.find("news:keywords", self.namespaces)
        if keywords is not None:
            datum["keywords"] = keywords.text

        genres = el.find("news:genres", self.namespaces)
        if genres is not None:
            datum["genres"] = genres.text

        return True

    def _parse_image(self, datum, el) -> bool:
        if el is None:
            return False
        # Required elements
        loc = el.find("image:loc", self.namespaces)
        datum["image"] = loc.text

        # Optional elements
        caption = el.find("image:caption", self.namespaces)
        if caption is not None:
            datum["image_caption"] = caption.text

        title = el.find("image:title", self.namespaces)
        if title is not None:
            datum["image_title"] = title.text

        geo_location = el.find("image:geo_location", self.namespaces)
        if geo_location is not None:
            datum["image_geo_location"] = geo_location.text

        return True

    def parse(self):
        urls = []
        for url_elem in self.xml_tree.findall("url", self.namespaces):
            parsed_datum = {}
            self._parse_loc(parsed_datum, url_elem.find("loc", self.namespaces))
            self._parse_lastmod(parsed_datum, url_elem.find("lastmod", self.namespaces))
            self._parse_news(parsed_datum, url_elem.find("news:news", self.namespaces))
            self._parse_image(
                parsed_datum, url_elem.find("image:image", self.namespaces)
            )

            # Strip the values
            parsed_datum = {
                k: v.strip() if isinstance(v, str) else v
                for k, v in parsed_datum.items()
            }
            urls.append(NewsUrl(**parsed_datum))

        return urls
