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
        """Builds a NewsUrl object.

        Args:
            url (str): An URL of the news article.
            title (str): Title of the news article.
            publication_date (str): The date of the publication.
            publication_name (str): Publisher of the news article.
            language (str): Language of the article
            last_modification (str, optional): Last modification of article. Defaults to None.
            keywords (str, optional): Keywords provided by the publisher. Defaults to None.
            genres (str, optional): Genres provided by the published. Defaults to None.
            image (str, optional): Image of the article. Defaults to None.
            image_caption (str, optional): Image caption. Defaults to None.
            image_title (str, optional): Title of the article's image. Defaults to None.
            image_geo_location (str, optional): Geolocation of the image. Defaults to None.
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
