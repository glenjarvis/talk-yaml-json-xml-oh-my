#!/usr/bin/env python
"""Convert the customer dictionary defined in the source file to our xml format and
dump out the resulting representation.
"""

import xml.etree.ElementTree as ET

from source import CUSTOMER_DICT


person = ET.Element("Person")
fn = ET.SubElement(person, 'FirstName')
fn.text = CUSTOMER_DICT['First Name']
sn = ET.SubElement(person, 'Surname')
sn.text = CUSTOMER_DICT['Surname']
pn = ET.SubElement(person, 'PreferredPronouns')
pn.text = CUSTOMER_DICT['Preferred Pronouns']
em = ET.SubElement(person, "Email")
em.text = CUSTOMER_DICT['Email']
gh = ET.SubElement(person, "GitHub")
gh.text = CUSTOMER_DICT['GitHub']
li = ET.SubElement(person, 'LinkedIn')
li.text = CUSTOMER_DICT['LinkedIn']
bi = ET.SubElement(person, 'BitcoinAddress')
bi.text = CUSTOMER_DICT['Bitcoin Address']
address = CUSTOMER_DICT['Address']
ET.SubElement(person, 'Address',
              city=address['City'],
              postalCode=str(address['Postal Code']),
              state=address['State'],
              streetAddress=address['Street Address'])
phs = ET.SubElement(person, 'PhoneNumbers')
for number_entry in CUSTOMER_DICT['Phone Numbers']:
    ET.SubElement(phs, 'PhoneNumber',
                  number=number_entry['number'],
                  type=number_entry['type'])

print("The data in XML format")
print("======================")
ET.dump(person)
