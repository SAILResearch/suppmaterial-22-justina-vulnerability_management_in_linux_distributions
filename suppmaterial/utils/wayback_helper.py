import requests
import json


def get_available_archive(url):
    turl = "http://archive.org/wayback/available?url="+url
    r = requests.get(turl)

    # print(r.text)
    obj = json.loads(r.text)
    wb_url = ""
    if "closest" in obj["archived_snapshots"].keys():
        if obj["archived_snapshots"]["closest"]["status"] == "200":
            wb_url = obj["archived_snapshots"]["closest"]['url']
    return wb_url