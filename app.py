from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    numm = request.form.get('From')
    print(numm)

    resp = MessagingResponse()

    if msg == "Hi":
        resp.message("Welcome to Trust Banking {}".format(numm))

    elif msg == "Account balance":
        resp.message("Your Account Balance is 99999999999")

    elif msg == "Leave":
        resp.message("Your account Deleted Successfully ")

    else:
        resp.message("Type 'Hi' to Begin")

    # Create reply

    

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)