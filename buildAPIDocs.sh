#!/bin/bash

sudo apt-get install python3-pip -y
pip3 install wheel
pip3 install apidoc

apidoc -c api_docs/apidoc_config.yml
