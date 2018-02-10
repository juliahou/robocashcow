import json
import requests
import base64

key_words = {"circle", "silver", "coin"}

def encode_image(path):
  image = open(path, "rb")
  image_content = image.read()
  return base64.b64encode(image_content)

def send_image(path):
  image_enc = encode_image(path)
  data = '{"requests":[{"image":{"content":"'+image_enc+'"},"features":[{"type":"LABEL_DETECTION","maxResults":10}]}]}'
  r = requests.post("https://vision.googleapis.com/v1/images:annotate?key=AIzaSyBshqEAh-ixbpMMKniwd2kiyNTbIYi0OR0", data=data)
  labelAnnotations = r.json()["responses"][0]["labelAnnotations"]
  labels = []
  for thing in labelAnnotations:
    labels.append(thing["description"])
  return labels

def check_coin(path):
  labels = send_image(path)
  print(labels)
  for label in labels:
    label = label.encode('ascii','ignore')
    if label in key_words:
      return True
  return False

