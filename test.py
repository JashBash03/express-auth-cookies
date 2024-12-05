import requests

url = "http://localhost:3000"
r = requests.get(url)
print("[TEST] GET / =>", r.status_code)

r = requests.post(url+"/api/users", data={"user": "admin2", "password": "admin"})
print("[TEST] POST /api/users =>", r.status_code)

r = requests.get(url+"/api/users")
print("[TEST] GET /api/users =>", r.status_code)

r = requests.get(url+"/api/users/admin")
print("[TEST] GET /api/users/admin =>", r.status_code)

r = requests.post(url + "/api/login", data={"user": "admin", "password": "admin"})
print("[TEST] POST /api/login =>", r.status_code, r.cookies)
cookie = r.cookies
user = cookie.get("user")

r = requests.put(url + "/api/users/aaaaa", data={"password": "alvaroroman"})
print("[TEST] PUT /api/users/aaaaa =>", r.status_code, r.cookies)

# Obtener usuarios -> []
# Recorrer los usuarios y obtener su propiedad "user"


r = requests.delete(url= "/api/users",)
print("[TEST] DELETE /api/users =>", r.status_code, r.cookies)
