# https://hooks.slack.com/services/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

import requests
import json

from datetime import datetime

timer = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

SLACK = 'https://hooks.slack.com/services/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'

requests.post( SLACK, data = json.dumps({
    'text': timer,
    'username': u'me',
    'icon_emoji': u':ghost:',
    'link_names': 1,
}))

