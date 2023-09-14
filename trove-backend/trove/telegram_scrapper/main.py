import uuid
from dotenv import load_dotenv
import json
import logging
import os
from telethon import TelegramClient

from message_parser import extract_contact_info
from entities import Contact, Product
from db import Database

load_dotenv()

logging.basicConfig(
    filename="scrapper.log",
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)



API_ID = os.environ.get('TELEGRAM_API_ID')
API_HASH = os.environ.get('TELEGRAM_API_HASH')
IMAGE_DIRECTORY = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'images')
DATA_DIRECTORY = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data')


client = TelegramClient('scraper', API_ID, API_HASH)


async def scrape_channel(db: Database, channel_username: str, message_limit: int = 100):
    async for message in client.iter_messages(channel_username, limit=message_limit):           
        path = await client.download_media(message.media, file=IMAGE_DIRECTORY)
        contact = Contact(urls=[f'https://t.me/{channel_username[1:]}'],
                          emails=[],
                          phone_numbers=[])

        if message.entities:        
            contact_info = extract_contact_info(message)
            
            contact.urls.extend(contact_info['urls'])
            contact.emails.extend(contact_info['emails'])
            contact.phone_numbers.extend(contact_info['phone_numbers'])
        
        if message.grouped_id:
            product_id = str(message.grouped_id)
        else:
            product_id = str(uuid.uuid4())
            
        product = Product(
            id=product_id,
            vender=channel_username,
            name='',
            description='',
            raw_message=message.message,
            images=[path],
            attributes={},
            contact=contact         
        )        

        db.save(product)


async def main():    
    channels = ['@nevacomputer', '@computers4w']        

    db = Database()   

    for channel_username in channels:
        await scrape_channel(db, channel_username, message_limit=100)

        with open(os.path.join(DATA_DIRECTORY, f'{channel_username}.json'), 'w') as f:
            string = json.dumps(db.to_json())
            f.write(string) 

    

with client:
    client.loop.run_until_complete(main())