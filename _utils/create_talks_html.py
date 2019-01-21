#!/usr/bin/env python3
"""
Generate speaker's list and talk profile html from the PyCaribbean 2017 Submissions.json
file from https://papercall.io.

First you must down load the submissions file from papercall.
1. Save it in the same directory as this file.
2. Execute this script.
3. A speakers.json file will be create in the _data folder.
4. A talk profile will be created for each speaker in the file.
"""

import json

talk_template = """---
layout: page
permalink: {7}
---

<div class="speaker-wrapper">
<a href="{6}">
  <div class="speaker-img-wrapper">
    <img class="speaker-img-large" src="{0}" />
      <h3>{1}</h3>
  </div>
    </a>
  <div class="uk-grid">
    <div class="uk-width-4-1">
      <h1>{2}</h1>
    </div>
  </div>
</div>
<br/>
<div>
    <h3>Audience: {3}</h3>
</div>
<br/>
<div class="talk_content">

    <h3>Description:</h3>
    <p>{4}</p>
    
</div>

"""

with open('PyCaribbean 2019 Talks.json', 'r') as f:
    json_data = json.loads(f.read())
    talks = []
    
    for talk in json_data:
        
        # Slugify talk name.
        file_name = '../talk/{}.html'.format(talk['title'].replace(' ', '-').lower().replace('/', '-').replace(',', '').replace('(', '').replace(')', ''))
        
        # write out the speaker's page.'
        with open(file_name, 'w') as wf:

            talks.append({
                'avatar': talk['avatar'],
                'name': talk['name'],
                'url': '/talk/{0}/'.format(talk['title'].replace(' ', '-').lower().replace('/', '-').replace(',', '').replace('(', '').replace(')', '')),
                'speaker_url': '/speaker/{0}/'.format(talk['name'].replace(' ', '-').lower()),
                'title': talk['title'],
                'audience_level': talk['audience_level'],
                'description': talk['description'],
                'bio': talk['bio'],
            })
            wf.write(talk_template.format(
                talk['avatar'], # {0}
                talk['name'], # {1}
                talk['title'], # {2}
                talk['audience_level'], # {3}
                talk['description'], # {4}
                talk['bio'], # {5}
                '/speaker/{0}/'.format(talk['name'].replace(' ', '-').lower()), # {6}
                '/talk/{0}/'.format(
                    talk['title'].replace(' ', '-').lower().replace('/', '-').replace(',', '').replace('(', '').replace(
                        ')', '')), # {7}
            ),

            )

# Create talks.json data. This is used to populate the talk's pages created above.
with open('../_data/talks.json', 'w') as talks_json:
    talks_json.write(json.dumps(talks, indent=2))

print("Finished processing")
