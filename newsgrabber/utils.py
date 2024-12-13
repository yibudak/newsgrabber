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

from dateutil import parser as dateparse


def parse_iso8601_date(date_string: str) -> datetime.datetime:
    """
    Parse ISO 8601 date (e.g. from sitemap's <publication_date>)
    into datetime.datetime object.

    :param date_string: ISO 8601 date, e.g. "2018-01-12T21:57:27Z" or
    "1997-07-16T19:20:30+01:00".
    :return: datetime.datetime object of a parsed date.
    """
    return dateparse.parse(date_string)
