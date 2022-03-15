# wombopy
**wombopy** is a commands-line program to generate and download images from [wombo.art](https://wombo.art). It requires Python interpreter, version 3.9+.

## Installation
```
pip install wombopy
```

## Documentation
wombopy --help
```
Usage: wombopy [OPTIONS] COMMAND [ARGS]...

Options:
  -v, --version         Show the application's version and exit.
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or
                        customize the installation.
  --help                Show this message and exit.

Commands:
  run  Create an image from wombo.art

```

wombopy run --help
```
Usage: wombopy run [OPTIONS] IDENTIFY_KEY PROMPT STYLE

  Create an image from wombo.art

Arguments:
  IDENTIFY_KEY  [required]
  PROMPT        [required]
  STYLE         [required]

Options:
  -s, --show  Show back the image
  --help      Show this message and exit.

```