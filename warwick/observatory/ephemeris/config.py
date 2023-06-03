#
# This file is part of ephemd
#
# ephemd is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ephemd is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ephemd.  If not, see <http://www.gnu.org/licenses/>.

"""Helper function to validate and parse the json config file"""

import json
from warwick.observatory.common import daemons, validation

CONFIG_SCHEMA = {
    'type': 'object',
    'additionalProperties': False,
    'required': ['daemon', 'latitude', 'longitude', 'altitude'],
    'properties': {
        'daemon': {
            'type': 'string',
            'daemon_name': True
        },
        'latitude': {
            'type': 'number',
            'minimum': -90,
            'maximum': 90
        },
        'longitude': {
            'type': 'number',
            'minimum': -180,
            'maximum': 180
        },
        'altitude': {
            'type': 'number',
            'minimum': 0
        }
    }
}


class Config:
    """Daemon configuration parsed from a json file"""
    def __init__(self, config_filename):
        # Will throw on file not found or invalid json
        with open(config_filename, 'r', encoding='utf-8') as config_file:
            config_json = json.load(config_file)

        # Will throw on schema violations
        validation.validate_config(config_json, CONFIG_SCHEMA, {
            'daemon_name': validation.daemon_name_validator
        })

        self.daemon = getattr(daemons, config_json['daemon'])
        self.latitude = float(config_json['latitude'])
        self.longitude = float(config_json['longitude'])
        self.altitude = float(config_json['altitude'])
