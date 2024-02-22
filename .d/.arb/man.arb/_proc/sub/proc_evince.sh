#!/bin/bash

if type evince >/dev/null; then
    evince "$1"
fi
