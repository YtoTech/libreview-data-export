# LibreView data export

Export device readings from [LibreView](https://www.libreview.com) API to a CSV file.

## Getting started

Install dependencies with [Pipenv](https://docs.pipenv.org/):

```sh
pipenv install
```

Create a configuration file `settings.json` from the sample:

```sh
cp settings.sample.json settings.json
```

Replace the `api_token` in the configuration file by your API token.

> Note: there is no direct access to API tokens on the UI; you can login and use your
browser Web Developer Network panel to search for a `Bearer` token on `Authorization`
request header to api.libreview.io.

Launch your first export:

```sh
pipenv run python export-data.py
```

This will export the data to `export-output.json`.
