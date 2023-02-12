import json
import time
from io import StringIO, BytesIO

import requests

from wombopy.logging import wombolog


def task(session, id):
    r = session.get(f"https://paint.api.wombo.ai/api/tasks/{id}")

    rep = r.json()
    wombolog.info(f"Status: {rep['state']}")
    return rep


def show_img(url):
    try:
        from PIL import Image
    except ImportError:
        raise ImportError("Pillow image is needed to use this function.")

    r = requests.get(url)

    with Image.open(BytesIO(r.content)) as im:
        im.show()

        return im


def create(id_token: str, prompt: str, style: int):
    s = requests.Session()
    s.headers.update(
        {
            "Authorization": "bearer " + id_token,
            "Origin": "https://paint.api.wombo.ai/",
            "Referer": "https://paint.api.wombo.ai/",
            "User-Agent": "Mozilla/5.0",
        }
    )

    def init_task():
        body = StringIO()
        json.dump({"premium": False}, body)

        r = s.post("https://paint.api.wombo.ai/api/tasks", data=body.getvalue())

        return r.json()["id"]

    id = init_task()
    
    display_freq = 10
    
    body = {
        "input_spec": {
            "prompt": prompt,
            "style": style,
            "display_freq": display_freq,
        },
        "is_premium": False
    }

    body = json.dumps(body)
    print(body)
    r = s.put(f"https://paint.api.wombo.ai/api/tasks/{id}", data=body)
    
    print(r.json())

    wombolog.info(f"Status: {r.json()['state']}")
    display_freq = display_freq / 10

    latest_task = task(s, id)
    while latest_task["state"] != "completed":
        time.sleep(display_freq)
        latest_task = task(s, id)

    result = s.post(f"https://paint.api.wombo.ai/api/tradingcard/{id}")
    img_uri = result.json()

    if img_uri:
        wombolog.info(f"Url result: {img_uri}")
        return img_uri
    else:
        wombolog.info("Invalid image uri, can't download result!")
