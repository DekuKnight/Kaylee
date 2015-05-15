#!/usr/bin/python

import wolframalpha
import sys

app_id='UK9ERG-VX7H8K7G36'

client = wolframalpha.Client(app_id)

query = ' '.join(sys.argv[1:])
res = client.query(query)

if len(res.pods) > 0:
	texts = ""
	pod = res.pods[1]
	if pod.text:
		texts = pod.text
	else:
		texts = "I have no answer for that"
	texts = texts.encode("ascii","ignore")
	print(texts)
else:
	print("Sorry, I'm not sure.")
