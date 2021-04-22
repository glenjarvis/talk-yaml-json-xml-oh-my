#!/usr/bin/env python
"""Parse the file source.xml and convert it to a nested Python
dictionary.
"""

import xml.etree.ElementTree as ET

tree = ET.parse("source.xml")
root = tree.getroot()

print("Data from file")
print("==============")
ET.dump(root)
print()

# now we walk the tree and build the original Python dict
person = {}
assert root.tag=='Person'
person['First Name'] = root.find('FirstName').text
person['Surname'] = root.find('Surname').text
person['Preferred Pronouns'] = root.find('PreferredPronouns').text
person['Email'] = root.find('Email').text
person['GitHub'] = root.find('GitHub').text
person['LinkedIn'] = root.find('LinkedIn').text
person['Bitcoin Address'] = root.find('BitcoinAddress').text
address = {}
address_el = root.find('Address')
address['City'] = address_el.get('city')
address['Postal Code'] = int(address_el.get('postalCode'))
address['State'] = address_el.get('state')
address['Street Address'] = address_el.get('streetAddress')
person['Address'] = address
numbers_el = root.find('PhoneNumbers')
phone_numbers = []
for child in numbers_el.findall('PhoneNumber'):
    phone_numbers.append({'number':child.get('number'), 'type':child.get('type')})
person['Phone Numbers'] = phone_numbers
print("Converted")
print("=========")
print(repr(person))
