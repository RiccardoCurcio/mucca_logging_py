# Copyright 2018 Federica Cricchio
# fefender@gmail.com
#
# This file is part of mucca_logging.
#
# mucca_logging is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# mucca_logging is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with mucca_logging.  If not, see <http://www.gnu.org/licenses/>.
"""Mucca Logging."""
import sys
from datetime import datetime
import os


class logging:
    """Class logging."""

    @staticmethod
    def log_info(msg, file, line):
        """Log_info."""
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        level = "\x1B[32mINFO\x1B[0m"
        service_name = os.getenv("SERVICE_NAME")
        sys.stderr.write(
            '[{}] {} {} {}:{} "{}"\n'.format(
                now,
                level,
                service_name,
                file,
                line,
                msg
            )
        )
        return None

    @staticmethod
    def log_warning(msg, file, line):
        """Log_warning."""
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        level = "\x1B[33mWARNING\x1B[0m"
        service_name = os.getenv("SERVICE_NAME")
        sys.stderr.write(
            '[{}] {} {} {}:{} "{}"\n'.format(
                now,
                level,
                service_name,
                file,
                line,
                msg
            )
        )
        return None

    @staticmethod
    def log_error(msg, file, line):
        """Log_error."""
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        level = "\x1B[31mERROR\x1B[0m"
        service_name = os.getenv("SERVICE_NAME")
        sys.stderr.write(
            '[{}] {} {} {}:{} "{}"\n'.format(
                now,
                level,
                service_name,
                file,
                line,
                msg
            )
        )
        return None
