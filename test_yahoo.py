from yahoo_oauth import OAuth2

oauth = OAuth2(None, None, from_file="oauth2.json")   # opens a browser to authorize, first run only
r = oauth.session.get(
    "https://fantasysports.yahooapis.com/fantasy/v2/users;use_login=1/games;game_keys=nfl/leagues?format=json"
)
print(r.status_code)
print(r.text[:1000])
