#!/bin/env sh
export MONITOR=eDP1
pkill polybar

sleep 1;

polybar example &
