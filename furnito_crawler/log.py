import datetime

class Log:
    def __init__(self):
        pass

    def log(self, log_text):
        '''
        @usage: for store user activity
        @args: log_text, string, user activity
        '''
        time_stamp = str(datetime.datetime.now())
        log_path = self.log_path()
        log_path = u''.join((log_path, '/log/log.txt')).encode('utf-8').strip()
        log_content = u' '.join((time_stamp, log_text)).encode('utf-8').strip()
        with open(log_path, 'ab') as logfile:
            logfile.write(log_content)

    def error_log(self, log_text):
        '''
        @usage: for store error log
        @args: log_text, string, error log
        '''
        time_stamp = str(datetime.datetime.now())
        log_path = self.log_path()
        log_path = u''.join((log_path, '/log/error_log.txt')).encode('utf-8').strip()
        log_content = u' '.join((time_stamp, log_text)).encode('utf-8').strip()
        with open(log_path, "ab") as errorlog:
            errorlog.write(log_content)
    
    def log_path(self):
        '''
        @usage: get log path
        @return: log path
        '''
        path = os.path.dirname(os.path.realpath(__file__))
        return path  
