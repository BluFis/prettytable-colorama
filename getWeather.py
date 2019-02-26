import urllib.request
import urllib.parse
import json
import socket
class GetWeather(object):
    def __init__(self):
        self.AK = '6HxqOQfZYwjbBZoVDpt8411js12DYToa'
        self.request_url = 'http://api.map.baidu.com/location/ip'
        self.AppKey = "10003"
        self.sign = 'b59bc3ef6191eb9f747dd4e83c99f2a4'
        self.weather_url = 'http://api.k780.com'

    def get_ip(self):
        myname = socket.getfqdn(socket.gethostname())
        return socket.gethostbyname(myname)

    def getCity(self):
        if self.get_ip()[0:3]=='192':
            postdata = urllib.parse.urlencode({'ak': self.AK}).encode('utf-8')
        else:
            postdata = urllib.parse.urlencode({'ip':self.get_ip(),'ak':self.AK}).encode('utf-8')
        request = urllib.request.Request(self.request_url, postdata)
        html = urllib.request.urlopen(request).read().decode('utf-8')
        if json.loads(html)['content']['address_detail']['city'][-1:]=="市":
            return(json.loads(html)['content']['address_detail']['city'][:-1])
        else:
            return(json.loads(html)['content']['address_detail']['city'])

    def getWeather(self):
        postdata = urllib.parse.urlencode({'app': 'weather.future', 'appkey': self.AppKey,'sign':self.sign,'format':'json','weaid':self.getCity()}).encode('utf-8')
        request = urllib.request.Request(self.weather_url, postdata)
        html = urllib.request.urlopen(request).read().decode('utf-8')
        if json.loads(html)['success']=="1":
            return json.loads(html)['result']