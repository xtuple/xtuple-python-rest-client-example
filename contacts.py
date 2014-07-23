#!/usr/bin/python2.4
# -*- coding: utf-8 -*-
#
# Copyright (C) 2012 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Simple command-line sample that demonstrates xTuple 'Service Account'
OAuth 2.0 REST API scenario.

Lists all the Contacts in the xTuple database. Service accounts are created in
the xTuple Mobile Web Client. See the documentation for more information:

  https://github.com/xtuple/xtuple/wiki/OAuth-2.0-Service-Accounts-Scenario

Command Line Usage Run:
  $ python contacts.py

####################
TODO:
  Set all the OAuth 2.0 client settings and Discovery Document URL below.
####################
"""

__author__ = 'ben@xtuple.com (bendiy)'

import httplib2
import pprint
import sys

from apiclient.discovery import build
from oauth2client.client import SignedJwtAssertionCredentials
from apiclient.model import JsonModel

def main(argv):
  # Load the key in PKCS 12 format that you downloaded from the xTuple Mobile
  # Web Client OAuth 2.0 Client registration workspace when you created your
  # Service account client. Place the file in the same directory as this file.
  f = file('privatekey.p12', 'rb')
  key = f.read()
  f.close()

  # Create an httplib2.Http object to handle our HTTP requests and authorize it
  # with the Credentials. Note that the first parameter, service_account_name,
  # is the Client ID created for the Service Account.
  ####################
  # TODO: Set these parameters to match your OAuth 2.0 Client values.
  ####################
  credentials = SignedJwtAssertionCredentials('example_f8ad6a5f-883b-4d41-ea6a-1971af1919e8', #service_account_name
        key, #private_key
        'https://your-demo.xtuplecloud.com/your-db-name/auth', #scope
        private_key_password='notasecret',
        user_agent=None,
        token_uri='https://your-demo.xtuplecloud.com/your-db-name/oauth/token',
        revoke_uri='https://your-demo.xtuplecloud.com/your-db-name/oauth/revoke-token',
        prn='admin'
        )

  ####################
  # TODO: On production, do not disable_ssl_certificate_validation. Development only!!!
  ####################
  http = httplib2.Http(disable_ssl_certificate_validation=True)
  http = credentials.authorize(http)

  # By default, JsonModel is used and it sets alt_param = 'json'. The xTuple API
  # does not support an 'alt' query parameter, so we strip it off the model.
  # @See: google-api-python-client\apiclient\model.py _build_query()
  features = []
  model = JsonModel('dataWrapper' in features)
  model.alt_param = None

  # Fetch the Discovery Document and build a service for the resources.
  ####################
  # TODO: Set the discoveryServiceUrl parameter to match your OAuth 2.0 Client value.
  # Optionally, use a difference resource than contact.
  ####################
  service = build("contact", #serviceName
                  "v1alpha1", #version
                  http=http,
                  discoveryServiceUrl="https://your-demo.xtuplecloud.com/your-db-name/discovery/{apiVersion}/apis/{api}/{apiVersion}/rest",
                  model=model
                  )

  # List all the Contacts.
  lists = service.Contact().list().execute(http=http)
  pprint.pprint(lists)

if __name__ == '__main__':
  main(sys.argv)
