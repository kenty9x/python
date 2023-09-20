import requests  # Requests library http://docs.python-requests.org
import json

baseUrl = 'https://api.alertsite.com/api/v3'
username = ''  # Replace with your AlertSite login email
password = ''          # Replace with your AlertSite password
sla_id = 472072

# Log in
payload = {'username': username, 'password': password}
r = requests.post(baseUrl + '/access-tokens', data=json.dumps(payload), headers={'Content-Type': 'application/json'})
token = r.json()['access_token']

# Get all SLAs
r = requests.get(baseUrl + '/slas', headers={'Authorization': 'Bearer ' + token})
result = r.json()

if r.status_code == requests.codes.ok:
    slas = result['results']
    print('Total SLAs found:', len(slas), '\n')

    for sla in slas:
        print('SLA: {name} (ID {id})\n'
              'Monitor: {monitor_name} (ID {monitor_id})\n'
              'Objectives:\n'
              'Availability: {availability}%\n'
              'Response time: {response_time} sec\n'.format(**sla))
else:
    print('Could not get SLAs. The following error(s) occurred:', *result['errors'], sep='\n')

# Get the SLA configuration
# r = requests.get(baseUrl + '/slas/{}'.format(sla_id), headers={'Authorization': 'Bearer ' + token})
# if r.status_code == requests.codes.ok:
#     print(json.dumps(r.json(), indent=2))
# else:
#     print('Could not get SLA #{}. The following error(s) occurred:'.format(sla_id), *r.json()['errors'], sep='\n')
