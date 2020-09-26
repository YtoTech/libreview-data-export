#!/bin/python
# -*- coding: utf-8 -*-
import json
import pprint
import requests

DEFAULT_SETTINGS_FILE_PATH = "settings.json"


def loads_settings(settings_file_path):
    print("Reading settings from file '{}'".format(settings_file_path))
    with open(settings_file_path, "r") as jfp:
        return json.load(jfp)


def read_data_from_libreview_api(settings):
    # TODO Get user settings: for device listing.
    # https://api.libreview.io/user
    # Get Glucose history.
    # https://api.libreview.io/glucoseHistory?numPeriods=5&period=14
    response = requests.get(
        "{}/glucoseHistory?numPeriods=5&period=7".format(settings["api_endpoint"]),
        headers={"Authorization": "Bearer {}".format(settings["api_token"])},
    )
    return response.json()


if __name__ == "__main__":
    data = read_data_from_libreview_api(loads_settings(DEFAULT_SETTINGS_FILE_PATH))
    pprint.pprint(data)
    output_json_file_path = "export-output.json"
    with open(output_json_file_path, "w") as ef:
        json.dump(data, ef)
        print("Written LibreView data to {}".format(output_json_file_path))


# CSV export.
# https://api-fr.libreview.io/export
# {"captchaResponse":"XXX","type":"glucose"}
# {"status":0,"data":{"url":"https://hub-fr.libreview.io/channel/XXX"},"ticket":{"token":"XXX","expires":1586543766}}

# Login
# POST:https://api-fr.libreview.io/auth/login
# {"email":"XXX","password":"XXX","fingerprint":"XXX"}
