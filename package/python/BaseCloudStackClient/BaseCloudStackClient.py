import hmac, hashlib
import base64
import os, sys
import urllib,urllib2
import json

class BaseCloudStackClient:
    def __init__(self, url, apiKey=None, secretKey=None):

        if (apiKey and secretKey):
            self.apiKey = apiKey
            self.secretKey = secretKey
            self.auth = True
        else:
            self.auth = False

        self.url=url

    def request(self, method, arguments):
        command = "command="+method

        for arg in arguments:
            if arguments[arg] != '':
                command = command+'&'+arg+'='+arguments[arg]

        if self.auth:
            command = command+'&apikey='+self.apiKey+'&response=json'

            command = command.replace(' ','%20')

            # Sort command
            command = command.split("&")
            command.sort(key=lambda x: x[0])
            command = "&".join(command)

            command = urllib.quote(command,'&=')

            digest = base64.b64encode(hmac.new(self.secretKey, command.lower(), hashlib.sha1).digest())

            # generate the digest
            #transform the digest in an url compliant way
            digest = digest.replace('+','%2B')
            digest = digest.replace('=','%3D')
            
            command = command + '&signature=' + digest

        try:
            response = urllib2.urlopen(self.url+command).read()
            mydict = json.loads(response)
            return mydict
        except Exception, e:
            print 'Error !', e
