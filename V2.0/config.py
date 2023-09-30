#class DevelopmentConfig():
#    DEBUG = True
#    MYSQL_HOST = '20.118.187.218'
#    MYSQL_USER = 'admin01'
#    MYSQL_PASSWORD = 'admin01'
#    MYSQL_DB = 'UMA_DB'


class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = '127.0.0.1'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'raysin1230'
    MYSQL_DB = 'UMA_DB'

#dictionario
config = {
    'development': DevelopmentConfig,
}