import logging


wombolog = logging.getLogger("wombolog")
wombolog.setLevel(logging.INFO)

wombolog.propagate = False