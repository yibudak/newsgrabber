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
from requests import RequestException, Session


class NetworkManager:
    def __init__(self):
        # Todo: user agent should be configurable
        # Todo: add proxy
        self.user_agent = "Googlebot/2.1 (+http://www.google.com/bot.html)"
        self.session = Session()
        self.session.headers.update({"User-Agent": self.user_agent})

    def fetch_sitemap(self, url) -> bytes:
        try:
            response = self.session.get(url)
            response.raise_for_status()
            return response.content
        # TODO: check response size (?)
        # Todo: use logger and better exceptions
        except RequestException as e:
            raise e
        except Exception as e:
            raise e
