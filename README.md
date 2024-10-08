# Bluprint demo project

This project demonstrates a structure and notebook execution in a basic bluprint project.

## Installation

Install [uv](https://docs.astral.sh/uv/), then run:

```sh
git clone https://github.com/igor-sb/bluprint-demo.git
cd bluprint-demo
uv venv && uv sync
```

## Running notebooks

Open and run a notebook in your IDE of choice (VSCode, Jupyter, ...). Make sure
to select the correct kernel, which should point to the `.venv` virtual
environment inside this directory. In VSCode it will show as `.venv/bin/python`
and should be marked as "Recommended".
