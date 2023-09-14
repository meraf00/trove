from dataclasses import dataclass

@dataclass
class Contact:
    urls: list[str]
    emails: list[str]
    phone_numbers: list[str]

    def to_json(self):
        return {
            'urls': self.urls,
            'emails': self.emails,
            'phone_numbers': self.phone_numbers
        }


@dataclass
class Product:
    id: str
    vender: str
    name: str
    attributes: dict[str, str]
    description: str
    raw_message: str
    contact: Contact
    images: list[str]

    def to_json(self):
        return {
            'id': self.id,
            'vender': self.vender,
            'name': self.name,
            'attributes': self.attributes,
            'description': self.description,
            'raw_message': self.raw_message,
            'contact': self.contact.to_json(),
            'images': self.images
        }