from telethon.types import Message, MessageEntityPhone, MessageEntityUrl, MessageEntityEmail


def extract_contact_info(message: Message) -> dict[str, list[str]]:
    urls: list[str] = []
    emails: list[str] = []
    phone_numbers: list[str] = []

    for url_entity, inner_text in message.get_entities_text(MessageEntityUrl):        
        urls.append(inner_text)

    for email_entity, inner_text in message.get_entities_text(MessageEntityEmail):        
        emails.append(inner_text)

    for phone_entity, inner_text in message.get_entities_text(MessageEntityPhone):        
        phone_numbers.append(inner_text)
    
    
    return {
        'urls'          : urls,
        'emails'        : emails,
        'phone_numbers' : phone_numbers,
    }