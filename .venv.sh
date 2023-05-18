#!/bin/sh

if [ -d ".venv" ]; then
    cd src; exec bash
else
    python3 -m venv .venv && pip install -r requirements.txt
fi
