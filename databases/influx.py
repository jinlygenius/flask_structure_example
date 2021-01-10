from influxdb import InfluxDBClient


class InfluxDB(object):

    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def _init_client(self):
        # 2.0 or 1.8
        # uri = self.app.config['INFLUXDB_URI']
        # token = self.app.config['INFLUXDB_TOKEN']
        # org = self.app.config.get('INFLUXDB_ORG', '-')
        # client = InfluxDBClient(url=f'{uri}', token=f'{token}', org=f'{org}')
        
        # 1.7
        self.host = self.app.config['INFLUXDB_HOST']
        self.port = self.app.config['INFLUXDB_PORT']
        self.ssl = self.app.config['INFLUXDB_SSL']
        self.username = self.app.config['INFLUXDB_USERNAME']
        self.password = self.app.config['INFLUXDB_PASSWORD']
        self.database = self.app.config['INFLUXDB_DB']
        self.measurement = self.app.config['INFLUXDB_MEASUREMENT']
        client = InfluxDBClient(host=f'{self.host}', port=f'{self.port}', ssl=self.ssl, username=f'{self.username}', password=f'{self.password}', database=f'{self.database}')
        return client

    def init_app(self, app):
        self.app = app
        self.client = self._init_client()

    def close(self):
        self.client.close()


influxdb = InfluxDB()
