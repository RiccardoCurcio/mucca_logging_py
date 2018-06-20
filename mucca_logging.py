import sys
from datetime import datetime
import os

class logging:
    @staticmethod
    def log_info(msg, file, line):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        level = "INFO"
        service_name = os.getenv("SERVICE_NAME")
        sys.stderr.write('[{}] {} {} {}:{} "{}"\n'.format(now,level, service_name, file, line, msg))
        return None

    @staticmethod
    def log_warning(msg, file, line):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        level = "WARNING"
        service_name = os.getenv("SERVICE_NAME")
        sys.stderr.write('[{}] {} {} {}:{} "{}"\n'.format(now,level, service_name, file, line, msg))
        return None

    @staticmethod
    def log_error(msg, file, line):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        level = "ERROR"
        service_name = os.getenv("SERVICE_NAME")
        sys.stderr.write('[{}] {} {} {}:{} "{}"\n'.format(now,level, service_name, file, line, msg))
        return None
