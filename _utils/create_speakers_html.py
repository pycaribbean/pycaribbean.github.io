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

speaker_template = """---
layout: page
---

<div class="speaker-wrapper">
  <div class="speaker-img-wrapper">
    <img class="speaker-img-large" src="{0}" />
  </div>
  <h1>{1}</h1>
  <div class="uk-grid">
    <div class="uk-width-1-2">
      <h3>Title: {2}</h3>
    </div>
    <div class="uk-width-1-2">
      <h3>Audience: {3}</h3>
    </div> 
  </div>
</div>
<div class="talk_content">
    <h2>Description</h2>
    <p>{4}</p>
</div>
<div class="speaker-bio">
    <h2>Who is {1}?</h2>
    <p>{5}</p>
</div
"""

with open('PyCaribbean 2017 Submissions.json', 'r') as f:
    json_data = json.loads(f.read())
    speakers = []
    
    for talk in json_data:
        
        # Slugify speaker name.
        file_name = '../speaker/{}.html'.format(talk['name'].replace(' ', '-').lower())
        
        # write out the speaker's page.'
        with open(file_name, 'w') as wf:
            wf.write(speaker_template.format(talk['avatar'], talk['name'],
                                             talk['title'], talk['audience_level'],
                                             talk['description'], talk['bio']))
            speakers.append({
                'avatar': talk['avatar'],
                'name': talk['name'],
                'url': 'speaker/{0}.html'.format(talk['name'].replace(' ', '-').lower()),
                'title': talk['title'],
                'audience_level': talk['audience_level'],
                'description': talk['description'],
                'bio': talk['bio'],
            })

# Create speakers.json data. This is used to populate the speaker's pages created above.
with open('../_data/speakers.json', 'w') as speakers_json:
    speakers_json.write(json.dumps(speakers, indent=2))

print("Finished processing")