import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

grids = {"dev": {1: 'host-1.dev.lan',
                 2: 'host-2.dev.lan'},
         "qa": {1: 'host-1.qa.lan',
                2: 'host-2.qa.lan'},
         "stg": {1: 'host-1.stg.lan',
                 2: 'host-2.stg.lan'},
         "uk": {1: 'host-1.uk.lan',
                2: 'host-2.uk.lan'},
         "us": {1: 'host-1.us.lan',
                2: 'host-2.us.lan'}
                }

for grid in grids.keys():
    print(f"grid: {grid}")
    for host in grids.get(grid):
        try:
            r = requests.get(url=f"https://{grids[grid][host]}/health",
                             headers={},
                             files={},
                             auth=None,
                             verify=False)
            if r.status_code != 200:
                print(f'BAD Response:', grid, host, r.status_code)
            else:
                print(f"Host: {grids[grid][host].split('.')[0]} OK!")
        except Exception as e:
            print(e)

print("Done")
