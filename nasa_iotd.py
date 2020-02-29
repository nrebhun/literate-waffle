import requests
import json, os, pwd
import xml.etree.ElementTree as ET

rss_url = "https://www.nasa.gov/rss/dyn/lg_image_of_the_day.rss"
destination = "/Users/" + pwd.getpwuid(os.getuid()).pw_name + "/Pictures/nasa_iotd"

response = requests.get(rss_url)
root = ET.fromstring(response.content)

image_urls = []
new_image_count = 0

if not os.path.exists(destination):
  print("Creating directory: '%s'" % (destination))
  os.mkdir(destination)
else:
  print("Adding to existing directory: '%s'" % (destination))

for item in root[0].iter("item"):
  for entry in item.iter("enclosure"):
      image_urls.append(entry.attrib["url"])

for image_url in image_urls:
  filename = image_url.split('/')[-1]
  path = "%s/%s" % (destination, filename)

  if not os.path.isfile(path):
    new_image_count += 1
    print("Requesting '%s'" % (filename))
    response = requests.get(image_url)
    if response.status_code == 200:
      with open(path, 'wb') as f:
        f.write(response.content)

print("Done! %s new image%s added." % (new_image_count if new_image_count else "No", "s" if new_image_count != 1 else ""))
