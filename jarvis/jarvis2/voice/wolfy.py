import sys
import wolframalpha as w

app_id = 'UK9ERG-VX7H8K7G36'

client = w.Client(app_id)

res = client.query(query)
if len(res.pods) > 0:
	texts = ""
        pod = res.pods[1]
        if pod.text:
            texts = pod.text
        else:
            texts = "I have no answer for that"
        print(texts)
else:
        print("Sorry, I'm not sure.")
