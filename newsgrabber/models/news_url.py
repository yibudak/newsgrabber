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
class NewsUrl:
    """
    NewsUrl class to store news article information.
    """

    def __init__(
        self,
        url,
        title,
        publication_date,
        publication_name,
        language,
        last_modification=None,
        keywords=None,
        genres=None,
        image=None,
        image_caption=None,
        image_title=None,
        image_geo_location=None,
    ):
        """
        Builds a NewsUrl object.

        :param url: An URL of the news article.
        :type url: str
        :param title: Title of the news article.
        :type title: str
        :param publication_date: The date of the publication.
        :type publication_date: str
        :param publication_name: Publisher of the news article.
        :type publication_name: str
        :param language: Language of the article.
        :type language: str
        :param last_modification: Last modification of the article,
        defaults to None.
        :type last_modification: str, optional
        :param keywords: Keywords provided by the publisher, defaults to None.
        :type keywords: str, optional
        :param genres: Genres provided by the publisher, defaults to None.
        :type genres: str, optional
        :param image: Image of the article, defaults to None.
        :type image: str, optional
        :param image_caption: Image caption, defaults to None.
        :type image_caption: str, optional
        :param image_title: Title of the article's image, defaults to None.
        :type image_title: str, optional
        :param image_geo_location: Geolocation of the image, defaults to None.
        :type image_geo_location: str, optional
        """
        self.url = url
        self.title = title
        self.date = publication_date
        self.last_modification = last_modification
        self.source = publication_name
        self.language = language
        self.keywords = keywords
        self.genres = genres
        self.image = image
        self.image_caption = image_caption
        self.image_title = image_title
        self.image_geo_location = image_geo_location
        self._unique_id = self._generate_unique_id()

    def _generate_unique_id(self):
        return self.url + str(self.date)

    def __str__(self):
        return f"{self.title}"

    def __repr__(self):
        return f"{self.title}"

    def __eq__(self, other):
        return self._unique_id == other._unique_id
