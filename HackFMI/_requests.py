import requests

skills = requests.get('https://hackbulgaria.com/hackfmi/api/skills/')
skills.encoding = 'ISO-8859-1'

mentors = requests.get('https://hackbulgaria.com/hackfmi/api/mentors/')

teams = requests.get('https://hackbulgaria.com/hackfmi/api/public-teams/')
teams.enconding = 'ISO-8859-1'
