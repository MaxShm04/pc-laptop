
client_id= "123070"
client_secret= "b1dd2796163946a2faaee3b411875ee2fea4fb95"
refresh_token= "466003f264ff81962854221e7082a295ed1a3efb"
access_token = "0469d1f44912afb52278152c6fb6b8a81cef826a"
code = "be8151e8232bd0cce69e3e92c8dbc4f5a2d74eb9"

def get_client_id():
    return client_id

def get_client_secret():
    return client_secret


def get_refresh_token():
    return refresh_token


def get_access_token():
    return access_token

def get_code():
    return code


url = "https://www.strava.com/oauth/authorize?client_id=123070&redirect_uri=http://localhost&response_type=code&scope=activity:read_all"
url2 = "https://www.strava.com/oauth/token?client_id=123070d&client_secret=b1dd2796163946a2faaee3b411875ee2fea4fb95&code=340602b28d9f45abff225641f644a08ebc2d4611&grant_type=authorization_code"
