from django.core.management.base import BaseCommand

import requests
import os
from dotenv import load_dotenv

class Command(BaseCommand):

    def handle(self,*arg, **karg):
        self.stdout.write(self.style.SUCCESS('Data inserted!'))

    def insertdata(self):
        load_dotenv() 
        api = os.getenv("API_KEY")
        headers = {'x-api-key': api}
        # breed = 'poodle'
        base_url = 'https://api.thedogapi.com/v1/breeds'
        # url = f'{base_url}/search?q={breed}'
        
        response = requests.get(base_url, headers=headers)
        breeds = response.json()
        names = ''
        for breed in breeds:
            names =  names + breed['name'] + ', ' 
        
        names -= ', '
        print(names)
        return names