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

There is a python library for JSON already built in. So, `import json` to use
it. There is a method on this module called `loads`. So, if we have the file
read and stored as a varible called `data` (as a large string), we can do this:

```loaded_data = json.loads(data)```

See the `from_json.py` program that reads the `source.json` file, converts it
from JSON to a Python dictionary, and prints a few uses of this data.

### Converting PYTHON data to JSON

You can also go the other way. If you have Python data and you want to dump it
to a user who may consume it into any other program or service, you still use
the `json` module. The method to dump this data into JSON is `dumps`.

See the `to_json.py` example program that dumps the source data into JSON
format on the screen. Also, note that after this is converted, it is a
*string*. As far as any program is concerned, it's text. (Of course, the text
needs to be parsable as specified by https://tools.ietf.org/html/std90).

Also, note that this isn't formatted in a pretty way for humans. This is meant
to be consumed by other programs. Of course, if you want to beautify it, you
can. You may want to, for example, make an example that is more easily read by
an audience when describing JSON. There are libraries that you can pip install
that will do that. One example is jsbeautifier. See the "make.py" file for an
example. This file generates the source.* files in this repo so we can keep
things consistent.


### Examples of usefulness

Most APIs use JSON to return the data. For example, if you wanted to ask GitHub
for all of the commits in this repository, you will get the results back in
JSON format. Here's a command line example to:


``` 
curl -i "https://api.github.com/repos/glenjarvis/talk-yaml-json-xml-oh-my/commits"
```

Notice this commit `fda3470ea01a817865430dc0c75b32861139e0bd` that is returned
(among others). It's a JSON object with the hash (`sha`), the author, commiter,
message, and tree:

```
  {                                                                                                                                                    
    "sha": "fda3470ea01a817865430dc0c75b32861139e0bd",                                                                                                 
    "node_id": "MDY6Q29tbWl0MzU5OTg4NjY4OmZkYTM0NzBlYTAxYTgxNzg2NTQzMGRjMGM3NWIzMjg2MTEzOWUwYmQ=",                                                     
    "commit": {                                                                                                                                        
      "author": {                                                                                                                                      
        "name": "Glen Jarvis",                                                                                                                         
        "email": "glen@glenjarvis.com",                                                                                                                
        "date": "2021-04-21T03:55:57Z"                                                                                                                 
      },                                                                                                                                               
      "committer": {                                                                                                                                   
        "name": "Glen Jarvis",                                                                                                                         
        "email": "glen@glenjarvis.com",                                                                                                                
        "date": "2021-04-21T04:01:27Z"                                                                                                                 
      },                                                                                                                                               
      "message": "Add first portion of talk: JSON",                                                                                                    
      "tree": {                                                                                                                                        
        "sha": "9013886531aec018cd4964077765f0486a578da2",                                                                                             
        "url": "https://api.github.com/repos/glenjarvis/talk-yaml-json-xml-oh-my/git/trees/9013886531aec018cd4964077765f0486a578da2"                   
      },
   ...
  }
```

This is the information that is contained within the commit. If this repo were
checked out locally, you can see where this data comes from and compare:

```
$ git cat-file -p fda3470ea01a817865430dc0c75b32861139e0bd
tree 9013886531aec018cd4964077765f0486a578da2
parent f11a2428d7a6539b7ed93b15b077fe995bdb4dc8
author Glen Jarvis <glen@glenjarvis.com> 1618977357 -0700
committer Glen Jarvis <glen@glenjarvis.com> 1618977687 -0700
gpgsig -----BEGIN PGP SIGNATURE-----
 
 iQIzBAABCAAdFiEEMB3SOJ/POM37/w4YkXbi+wR53lwFAmB/o5kACgkQkXbi+wR5
 3lyK4w//dGmvy9n2XevR4ZkXQ4IA1I8pJjk4khLIlXUx5x0Pz9aAWG18VaO0M7lu
 lYa6vKAbAlwr+ebzsbPYnBlf4yxID6UAOZZTjG8qC1SkVXZW7RpL/uGl9eN81AWM
 12aPcRPOGP3K5ixk/neeW+6xrMMqJEQA9r1veI9Y3v2sn9ckOsBC8Oa5GRnMeNTA
 dDcNMi9wuxI3caWBezCmcivGLZxK2OO/eMsnJPIDakA07kT/cN+J/qbynLF5AskZ
 Qb38WZ4QrPb4hl6UORe1z8yM+8PLFMkMyOiockH6c6yAg4DOmQFARVfU/Zfx1KXh
 5wdlWzfCzkWcbIHWAETRgMu/Asios7Y3NvqPB5sQz8sc22LZ4JpgAI9QdpcUBpr3
 k1iAZgN+OTHmmaTydHIdwhW07DNym2dm03BJgZozQ9TZpV83gLezDGXTKK2f2b78
 zPKQOTlQTxCcKpqsZYS2yj+c9kPtomG30jOM2ZImdavMcl3d/ZBtEHPyp3qFM0RQ
 ljrXEtt8wLAnzedJ8ZbDIJmL2d1Ey0UDpW84eHYxchPAwrlfhmnE1IDrqlCUTXMt
 XTVKrroZ18VdoBqBnm+4aLfSkog8yravbCILzTAJRn/JksG+qTjM8WdndjqRpZ21
 ag0voQ0QDV1nhHwU11QBfWwIAHQZUiViZvhAPdQ4WYmBwykFWLY=
 =wJdn
 -----END PGP SIGNATURE-----
```

So, by interfacing with other endpoints with JSON (using the MIME type of
"application/json"), you can begin interacting with practically any API service
that is available on the internet.

