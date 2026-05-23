# Lesson: Api Handling

# First have to install sudo pacman -S python-requests\

# import the requests lib
import requests

 # now create object where get the value
url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"

try: 
    response = requests.get(url, timeout=5) # timeout for forever wating problem

    #Raise error for bat status codes (404, 500, etc.)
    response.raise_for_status()

    data = response.json() #first converting request.object string into the json data and store as a dict in data

    username = (
        data.get("data", {}) #if data is not there the return empty by ("data", {} wit this)
            .get("login", {}) 
            .get("username")
    )

    if username:
        print(username)
    else:
        print("Username not found")


except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")

except requests.exceptions.ConnectionError:
    print("No internet connection")

except requests.exceptions.Timeout:
    print("Request time out")

except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")




