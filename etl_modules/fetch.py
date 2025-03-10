import os
import requests

def fetch_data(url, staging_dir):
    '''
    This logic fetch data from the source and download them into a staging directory

    Parameters:
    - url : web address of the csv data soruce 
    - staging_dir: file system where fetched data are staged

    Return : None
    
    '''
    file_name = url.split('/')[-1]
    file_path = os.path.join(staging_dir, file_name)

    response = requests.get(url)
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded data from {url} to {file_path}")
        return file_path
    else:
        print(f"Failed to download data from {url}")
        return None

def fetch_all_data(urls, staging_dir):

    for url in urls:
        fetch_data(url, staging_dir)