import log

def prepare():
    log.delete_old_logs()
    log.create_logfile()