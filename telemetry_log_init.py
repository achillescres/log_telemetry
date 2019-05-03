import telemetry_logging_lib as logs
import urllib

log_level = 'INFO'
log_file_name = input('Logs file name: ')+'.log'

dict_log_config = dict({
        "version":1,
        "handlers":{
            "fileHandler":{
                "class":     "logging.FileHandler",
                "formatter": "myFormatter",
                "filename":  'logs/{}'.format(log_file_name),
            }
        },
        "loggers":{
            "exampleApp":{
                "handlers": ["fileHandler"],
                "level":    log_level,
            }
        },
        "formatters":{
            "myFormatter":{
                "format":   "%(ascdate)s - %(asctime)s - %(massage)s"
            }
        }

})

#Open data.txt
telemetry_data = open('data.txt', 'r').readlines()
#Initialising logs
logs.log(dict_config= dict_log_config, log_lines= telemetry_data)

#URL
url = ''
urllib.urlretrieve(url, log_file_name)