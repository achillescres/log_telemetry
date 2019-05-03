
"""Telemetry sensors log
    achillescres"""

__author__ = 'achillescres'

import logging
import logging.config
import datetime

data_path = ''
data = list()

class Log_line:
    def __init__(self, date='-1/-1/-1111', time="00:00 00.00", data="N/A",
                 key='0'):
        self.time = 'TIME: {}'.format(time)
        self.data = 'INFO: {}'.format(data)
        self.date = 'DATE: {}'.format(date)
        self.key  = int(key)
    def return_contat_line(self, key='0'):
        return '* ' + self.time + ' | ' + self.date + ' | ' + self.data+' '

#Write logs to .log file
def rec_logs(line_info=['null'], _date=datetime.datetime.now(), _log_temp=''):

    for line in line_info:
        _log_temp = Log_line(
                            time=str(_date.second) + ':' + str(_date.minute) + ':' + str(_date.hour),
                            date= str(_date.day)+'/'+str(_date.month)+'/'+str(_date.year),
                            data= line,
                            ).return_contat_line()
        #Is it my log?
        if _log_temp[0:2]=='* ':
            logging.INFO(str(_log_temp[:-2]))
            print(_log_temp[:-2])

#Main function
def log(dict_config='N/A', log_lines=['N/A'], _date=datetime.datetime.now()):
    if dict_config=='N/A':
        #make_log_file(filename='telemetry.log')
        logging.basicConfig(filename='logs\\telemetry.log', level='INFO')
        logging.INFO('New log session, {}{}{}:'.format(str(_date.day), str(_date.month), str(_date.year)))
        logging.INFO('Starting log without advanced dictionary config...')
    else:
        #File name from config dictionary
        #make_log_file(dict_config['handlers']['fileHandler']['filename'])
        logging.config.dictConfig(dict_config)
    rec_logs(line_info=log_lines)

def make_log_file(filename='logs\\telemetry.log'):
    _ = open(filename, 'w')