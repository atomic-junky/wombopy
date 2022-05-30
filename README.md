[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# wombopy
**wombopy** is a commands-line program to generate and download images from [wombo.art](https://wombo.art). It requires Python interpreter, version 3.9+.

Please, <iframe src="https://ghbtns.com/github-btn.html?user=twbs&repo=bootstrap&type=star&count=true" frameborder="0" scrolling="0" width="150" height="20" title="GitHub"></iframe> this project to support it.

## Installation
```
pip install wombopy
```

## Documentation
See this issue to [#2](https://github.com/holy-tanuki/wombopy/issues/2) to start using wombopy.

And this issue to [#1](https://github.com/holy-tanuki/wombopy/issues/1) to know how to get an identify_key.

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