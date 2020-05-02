from mysql import connector

class Model:
    def __init__(self,config_db_file = 'config.txt'):
        self.__config_db_file = config_db_file
        self.__config_db = self.__read_config_db()
        self.__connect_to_db()
    
    def __read_config_db(self):
        d ={}

        with open(self.__config_db_file) as f_r:
            for line in f_r:
                (key, val) = line.strip().split(':')
                d[key] = val
        return d

    def __connect_to_db(self):
        self._cnx = connector.connect(**self.__config_db)
        self._cursor = self._cnx.cursor()

    def __close_db(self):
        self._cnx.close()             

