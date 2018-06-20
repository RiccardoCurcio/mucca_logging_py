import sys
from datetime import datetime
import os
from dotenv import load_dotenv
from dotenv import find_dotenv
import inspect

class logging:
    def __init__(self):
        load_dotenv(find_dotenv())

    def log_info(self, msg, file, line):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        level = "info"
        service_name = os.getenv("SERVICE_NAME")
        sys.stderr.write('[{}] {} {} {}:{} "{}"\n'.format(now,level, service_name, file, line, msg))
        return True

    def log_warning(self, msg, file, line):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        level = "warning"
        service_name = os.getenv("SERVICE_NAME")
        sys.stderr.write('[{}] {} {} {}:{} "{}"\n'.format(now,level, service_name, file, line, msg))
        return True

    def log_error(self, msg, file, line):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        level = "error"
        service_name = os.getenv("SERVICE_NAME")
        sys.stderr.write('[{}] {} {} {}:{} "{}"\n'.format(now,level, service_name, file, line, msg))
        return True

# log = logging()
# # get frame
# frame = inspect.currentframe()
# log.log_info("info test", frame.f_code.co_filename, frame.f_lineno)
# log.log_warning("warning test", frame.f_code.co_filename, frame.f_lineno)
# log.log_error("error test", frame.f_code.co_filename, frame.f_lineno)
