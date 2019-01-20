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

</div>
<br/>
<div class="speaker-bio">
    <h2>Who is {1}?</h2>
    <p>{2}</p>
</div>
"""

with open('PyCaribbean 2019 Speakers.json', 'r') as f:
    json_data = json.loads(f.read())
    speakers = []
    
    for speaker in json_data:
        
        # Slugify speaker name.
        file_name = '../speaker/{}.html'.format(speaker['name'].replace(' ', '-').lower())
        
        # write out the speaker's page.'
        with open(file_name, 'w') as wf:
            wf.write(speaker_template.format(
                speaker['avatar'],
                speaker['name'],
                # speaker['title'],
                # speaker['audience_level'],
                # speaker['description'],
                speaker['bio']))
            speakers.append({
                'avatar': speaker['avatar'],
                'name': speaker['name'],
                'url': '/speaker/{0}.html'.format(speaker['name'].replace(' ', '-').lower()),
                # 'title': speaker['title'],
                # 'audience_level': speaker['audience_level'],
                # 'description': speaker['description'],
                'bio': speaker['bio'],
            })

# Create speakers.json data. This is used to populate the speaker's pages created above.
with open('../_data/speakers.json', 'w') as speakers_json:
    speakers_json.write(json.dumps(speakers, indent=2))

print("Finished processing")