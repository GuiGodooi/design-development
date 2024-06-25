import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_all_urls(base_url, depth=1):
    urls = set()
    to_visit = {base_url}
    visited = set()

    for _ in range(depth):
        current_to_visit = to_visit
        to_visit = set()

        for url in current_to_visit:
            if url in visited:
                continue
            try:
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    for a_tag in soup.find_all('a', href=True):
                        full_url = urljoin(base_url, a_tag['href'])
                        if base_url in full_url:
                            to_visit.add(full_url)
                            urls.add(full_url)
            except requests.RequestException as e:
                print(f"Error fetching {url}: {e}")
            visited.add(url)
    return urls

# Use the function
base_url = 'https://hjgodoi.com.br'
urls = get_all_urls(base_url)
for url in urls:
    print(url)
