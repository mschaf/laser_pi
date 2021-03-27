#!/bin/bash

set -e

WORKING_DIR=$(pwd)
echo "Cloning helios repository"
git clone https://github.com/Grix/helios_dac.git /tmp/helios_dac

if [ -z "${LIBUSB_LOCATION}" ]; then
  LIBUSB_LOCATION=$(ldconfig -p | grep libusb-1.0 | tr ' ' '\n' | grep /)
fi

echo "Building libHeliosDacAPI.so"

cd /tmp/helios_dac/sdk
g++ -Wall -std=c++14 -fPIC -O2 -c HeliosDacAPI.cpp
g++ -Wall -std=c++14 -fPIC -O2 -c HeliosDac.cpp
g++ -shared -o libHeliosDacAPI.so HeliosDacAPI.o HeliosDac.o $LIBUSB_LOCATION

echo "Copying libHeliosDacAPI.so to lib/"

cp libHeliosDacAPI.so $WORKING_DIR/lib/libHeliosDacAPI.so

echo "Cleaning up"

rm -Rf /tmp/helios_dac

echo "Done"
