from django.core.management.base import BaseCommand
from shelter_web.models import Breed

import requests
import os
from dotenv import load_dotenv

class Command(BaseCommand):

    def handle(self,*arg, **karg):
        load_dotenv() 
        api = os.getenv("API_KEY")
        headers = {'x-api-key': api}

        # url = f'{base_url}/search?q={breed}'
        base_url = 'https://api.thedogapi.com/v1/breeds'

        responses = requests.get(base_url, headers=headers).json()
        breeds = []
        for response in responses:
            breeds.append(response['name'])
        
        for breed in breeds:
            Breed.objects.create(breed=breed)
            
        self.stdout.write(self.style.SUCCESS('Data inserted!'))