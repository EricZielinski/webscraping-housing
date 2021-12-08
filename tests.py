import requests

from utilities.email_alerts import sendEmail


def test_broker_url():
    URL = ""
    page = requests.get(URL)
    if not page.status_code == 200:
        sendEmail(subject="Problem accessing url",
                  body=URL)
        assert False
    assert True