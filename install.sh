#!/bin/bash
# ------------------------------------
# [Stefano Latini (Delta Biologicals)]

sudo apt-get update
sudo apt-get install -y build-essential python-dev
git clone https://github.com/b00leant/VL53L0X_rasp_python.git
cd VL53L0X_rasp_python
make