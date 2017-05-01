import logging
import os

class SingerTaskLogger(logging.Handler):
    def __init__(self,baseFilename):
        self.baseFilename = baseFilename
        logging.Handler.__init__(self)

    def emit(self, record):
        taskId = record.__dict__['taskId']

        msg = self.format(record)
        _filePath = os.path.join(self.baseFilename,str(taskId))
        _dir = os.path.dirname(_filePath)
        try:
            if os.path.exists(_dir) is False:
                os.makedirs(_dir)
        except Exception:
            print "can not make dirs"
            print "filepath is " + _filePath
            pass
        try:
            _fobj = open(_filePath, 'a')
            _fobj.write(msg)
            _fobj.write("\n")
            _fobj.flush()
            _fobj.close()
        except Exception:
            print "can not write to file"
            print "filepath is " + _filePath
            pass

