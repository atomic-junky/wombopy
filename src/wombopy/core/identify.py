import requests
import typer

from wombopy.logging import wombolog


def sign_up(key):
    body = {"key": key}

    r = requests.post(
        f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={key}",
        data=body,
    )

    if r.status_code != requests.codes.ok:
        error = f"Error during identification. Status code error: {r.status_code}"
        wombolog.info(error, err=True)
        assert False, error

    wombolog.info("Google identification sign up.")
    id_token = r.json()["idToken"]
    wombolog.info("  => idToken got.")
    return id_token


def look_up(identify_key, id_token):
    body = {"idToken": id_token}

    r = requests.post(
        f"https://identitytoolkit.googleapis.com/v1/accounts:lookup?key={identify_key}",
        data=body,
    )

    if r.status_code != requests.codes.ok:
        assert False, f"Error during identification. Status code error: {r.status_code}"

    wombolog.info("Google identification look up.")
    local_id = r.json()["users"][0]["localId"]
    wombolog.info("  => localId got.")
    return local_id


def identify(identify_key):
    id_token = sign_up(identify_key)
    local_id = look_up(identify_key, id_token)
    wombolog.info("Identification done!")

    return {"id_token": id_token, "local_id": local_id}
