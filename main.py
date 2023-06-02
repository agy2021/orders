from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        text = request.form['text']

        payload = {
            "content":f"name: {name}, description: {text}"
        }

        headers = {
            "authorization":"OTU2MzAwOTkxNDI1MzE0ODc2.Gx191P.MFJaeUnbNXl7Q2PLosh5n5QIYpBnpLglyh66fw"
        }

        post = requests.post("https://discord.com/api/v9/channels/1114210277890723871/messages", data=payload, headers=headers)

        return "Order placed! Stay in the pls donate server until I give you the order."
    else:
        return render_template('order.html')

app.run()