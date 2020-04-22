from twilio.rest import Client
def call():

    call = client.calls.create(
                            url='http://demo.twilio.com/docs/voice.xml',
                            to='+16462434851',     # replace this with your mobile phone, start with country code
                            from_='+18504039627'  # select this from Twilio console
                        )
    print(call.sid)


account_sid = 'AC2f9dbbd3f1b6faec4add0d413c036bb7' # find this in Twilio
auth_token = '4ba410cc6f353f07307c725f43cf0a89' # And this.
#account_sid = os.environ['TWILIO_ACCOUNT_SID']
#auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

if __name__ == "__main__":
    call()