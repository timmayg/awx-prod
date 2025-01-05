import requests

def get_ip_info():
    # Get the public IP address
    ip_response = requests.get('https://api.ipify.org?format=json')
    ip_address = ip_response.json()['ip']

    # Query the IP Geolocation API
    api_key = '7d1a31b57db84952833f8244eb2249d4'  # Replace with your actual API key
    geo_response = requests.get(f'https://api.ipgeolocation.io/ipgeo?apiKey={api_key}&ip={ip_address}')
    geo_info = geo_response.json()

    # Display the IP address information
    print(f"IP Address: {geo_info['ip']}")
    print(f"Country: {geo_info['country_name']}")
    print(f"Region: {geo_info['state_prov']}")
    print(f"City: {geo_info['city']}")
    print(f"Latitude: {geo_info['latitude']}")
    print(f"Longitude: {geo_info['longitude']}")
    print(f"ISP: {geo_info['isp']}")

if __name__ == "__main__":
    get_ip_info()