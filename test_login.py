import urllib.request
import urllib.parse
import http.cookiejar


def test_login():
    base_url = "http://localhost:5000"

    cookie_jar = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_jar))

    req = urllib.request.Request(f"{base_url}/login")
    resp = opener.open(req)
    print(f"Login page: {resp.status}")

    data = urllib.parse.urlencode({"username": "root", "password": "root"}).encode()
    req = urllib.request.Request(f"{base_url}/login", data=data)
    resp = opener.open(req, allow_redirects=True)
    print(f"POST login: {resp.status}")
    print(f"URL after login: {resp.url}")

    html = resp.read().decode()
    if "dashboard" in html.lower():
        print("SUCCESS: Llegó al dashboard!")
        return True
    else:
        print(f"FAIL: Quedó en {resp.url}")
        return False


test_login()
