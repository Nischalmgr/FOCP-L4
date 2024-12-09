import sys
import requests

def check_website(url):
    try:

        response = requests.get(url, timeout=5)
        
       
        if response.status_code == 200:
            print(f"The website at '{url}' is working.")
        else:
            print(f"The website at '{url}' returned status code {response.status_code}.")
    except requests.ConnectionError:
        print(f"Unable to connect to '{url}'. The website may not exist or is not reachable.")
    except requests.Timeout:
        print(f"The request to '{url}' timed out.")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print("Usage: python check_website.py <URL>")
        sys.exit(1)
    
 
    url = sys.argv[1]
    check_website(url)
