def send_message_to_slack(text):
    from urllib import request, parse
    import json
    import os
    from os.path import join, dirname
    from dotenv import load_dotenv


    PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dotenv_path = join(PROJECT_DIR, 'hgbudva/settings/.env')
    load_dotenv(dotenv_path)

    SLACK_CHANNEL_WEBHOOK = os.getenv("SLACK_CHANNEL_WEBHOOK")

    post = {"text": "%s" % text}

    try:
        json_data = json.dumps(post)
        req = request.Request(SLACK_CHANNEL_WEBHOOK,
                              data=json_data.encode('ascii'),
                              headers={'Content-Type': 'application/json'})
        resp = request.urlopen(req)
    except Exception as em:
        print("EXCEPTION: " + str(em))
