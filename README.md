# talk-yaml-json-xml-oh-my
Beginners technical talk with examples on the different data types for cross language/platform communication

## Introduction

The Bay Area Python Interest Group (BAyPIGgies) wanted to revive their "newbie
nugget" -- small snippets of information for beginners so that everyone in the
audience can walk away with some knowledge. They asked me if I could come up
with a small talk to help kick it off.

I've seen beginners get stuck with the terms JSON ("Pronounced /ˈdʒeɪ.sən/, as
in 'Jason and The Argonauts'), YAML (pronounced yam-L), and XML. Most have
heard of XML, but didn't know what JSON nor YAML were.

Having data formats like this is becoming more and more important as people
have more systems that need to inter-connect and communicate. For example, some
systems may have a client written in Python to submit data and a different
system across the network written in Java to consume the data.

We will briefly go over each format, discuss its strengths and weaknesses and
then dive into some examples on how to produce and consume this data with the
Python programming language. If you are writing in another programming
language, the process is very similar -- that's the strength of these formats.

## Example Data

Most systems have customers. So, an easy example for us will be for us to have
a customer. Except for two fields below (can you guess which two?), the
following is a valid representation of my data if I were a customer to some
system:


```
    First Name: Glen
    Surname: Jarvis
    Preferred Pronouns: He, Him, His
    Email: glen@glenjarvis.com
    GitHub: https://github.com/glenjarvis
    LinkedIn: https://www.linkedin.com/in/glenjarvis
    Bitcoin Address: bc1q889z9ap6vjxtjgrgn4ldsl4kp8vn44qpksn9z3
    Address:
      Street Address: 555 Made-up Lane
      City: San Francisco 
      Postal Code: 94114
      State: CA
    Phone Numbers:
      - number: 415-555-1212
        type: Home
```

We will represent this data in different formats and practice parsing,
submitting it to another service (e.g., SQS Queue), etc.


## Strengths and Weaknesses

We're going to structure the above data in different formats (XML, JSON, YAML,
etc.). So, you may ask, why have different formats to represent the same thing.
Here's an easy tool that I use to break it down:

XML: For computers
JSON: For programmers
YAML: For people

Yes, programmers are people who program computers. But, the above is a simple
breakdown for why one would use a particular format.

Honestly, you are given the format from a data source. Whatever format that
they gave it to you is probably the format you'll have to consume.

If you have to choose a format to give to another service, avoid XML if
possible. And, when in dobut, choose JSON.

However, we'll see plenty of examples where these formats are very popular and
used frequently.


## Python Representation 

The Python representation of this data is as a dictionary as follows:

```
    {'First Name': 'Glen',
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
     'Phone Numbers': [{'number': '415-555-1212', 'type': 'Home'}]}
```

## JSON Format

Previously, I had said that JSON was for programmers. And, you are programmers,
so let's start there. Also, JSON is so similar to a Python dictionary that it
immediately familiar.

JSON is an acronym for JavaScript Object Notation. It looks a *lot* like a
Python dictionary. However, unlike a Python dictionary (as text, we aren't yet
ready to discuss pickle), JSON has been standardized by the Internet
Engineering Task Force as STD90 (https://tools.ietf.org/html/std90).

Although it is a subset of JavaScript, it maps almost perfectly to a
dictionary. However, JSON can be consumed by many languges, not just Python --
so it is a great format for serializing a data format for ingestion by another
internet service or another program.

Here is the same data represented as a JSON object:


```
{
  "First Name": "Glen",
  "Surname": "Jarvis",
  "Preferred Pronouns": "He, Him, His",
  "Email": "glen@glenjarvis.com",
  "GitHub": "https://github.com/glenjarvis",
  "LinkedIn": "https://www.linkedin.com/in/glenjarvis",
  "Bitcoin Address": "bc1q889z9ap6vjxtjgrgn4ldsl4kp8vn44qpksn9z3",
  "Address": {
    "City": "San Francisco",
    "Postal Code": 94114,
    "State": "CA",
    "Street Address": "555 Made-up Lane"
  },
  "Phone Numbers": [{
    "number": "415-555-1212",
    "type": "Home"
  }]
}
```


### Bringing a JSON file into Python

There is a python library for JSON built in. So, `import json`. There is a
method on this module called `loads`. So, if we have the file read and stored
as a varible called `data` (as a large string), we can do this:

```loaded_data = json.loads(data)```

See the `from_json.py` program that reads the `source.json` file, converts it
from JSON to a Python dictionary, and prints a few uses of this data.

