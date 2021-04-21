"""Sample data in Python format"""

CUSTOMER_DICT = {
  'First Name': 'Glen',
  'Surname': 'Jarvis',
  'Preferred Pronouns': 'He, Him, His',
  'Email': 'glen@glenjarvis.com',
  'GitHub': 'https://github.com/glenjarvis',
  'LinkedIn': 'https://www.linkedin.com/in/glenjarvis',
  'Bitcoin Address': 'bc1q889z9ap6vjxtjgrgn4ldsl4kp8vn44qpksn9z3',
  'Address': {'City': 'San Francisco',
              'Postal Code': 94114,
              'State': 'CA',
              'Street Address': '555 Made-up Lane'},
  'Phone Numbers': [{'number': '415-555-1212', 'type': 'Home'}]
}


POTENTIAL_OUTPUT = {
  'Address': {'City': 'San Francisco',
              'Postal Code': 94114,
              'State': 'CA',
              'Street Address': '555 Made-up Lane'},
  'Bitcoin Address': 'bc1q889z9ap6vjxtjgrgn4ldsl4kp8vn44qpksn9z3',
  'Email': 'glen@glenjarvis.com',
  'First Name': 'Glen',
  'GitHub': 'https://github.com/glenjarvis',
  'LinkedIn': 'https://www.linkedin.com/in/glenjarvis',
  'Phone Numbers': [{'number': '415-555-1212', 'type': 'Home'}],
  'Preferred Pronouns': 'He, Him, His',
  'Surname': 'Jarvis'
}
