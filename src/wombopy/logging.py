import logging



wombolog = logging.getLogger("wombo_log")
wombolog.setLevel(logging.INFO)

stream = logging.StreamHandler()

wombolog.addHandler(stream)