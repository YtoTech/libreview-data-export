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
        "{}/glucoseHistory?numPeriods=5&period=14".format(settings["api_endpoint"]),
        headers={"Authorization": "Bearer {}".format(settings["api_token"])},
    )
    return response.json()


if __name__ == "__main__":
    data = read_data_from_libreview_api(loads_settings(DEFAULT_SETTINGS_FILE_PATH))
    pprint.pprint(data)
