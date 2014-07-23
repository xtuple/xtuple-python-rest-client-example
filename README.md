xTuple ERP Python REST API Client Example
=========================================

xTuple ERP Python REST API Client Example using the [Google APIs Client Library for Python](https://developers.google.com/api-client-library/python/)
to interface with xTuple's REST API.

WARNING: This example in in no way secure or using best practices
for Python application. This is meant for educational purposes only.

Install and Run the Client
--------------------------
1. Clone or download this repo:

  ```
  git clone git@github.com:xtuple/xtuple-python-rest-client-example.git
  ```

2. Register for an OAuth 2.0 "Services Account" Client in your xTuple Mobile
Client's "OAUTH2" interface. You will be prompted to download a PK12 keystore
file. See [OAuth 2.0 Service Accounts Scenario](https://github.com/xtuple/xtuple/wiki/OAuth-2.0-Service-Accounts-Scenario)
for more information.
3. Save the PK12 keystore file in the same directory as this file and the
`contacts.py` file.
3. Edit the `contacts.py` file and set all your OAuth 2.0 Client settings. See
all of the `TODO`s in the file to find out where to do that.
4. Make sure your xTuple Mobile Client is running before `contacts.py`.

Using the Example
-----------------
Run the `contacts.py` script from the command line:

```
$ python contacts.py
```

You should be presented with a JSON object containting a list of contacts.

## Credits

  - [bendiy](http://github.com/bendiy)

## License

[Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0.html)

Copyright (c) 2012-2013 xTuple [http://www.xtuple.com/](http://www.xtuple.com/)
