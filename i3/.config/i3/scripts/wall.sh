#!/bin/bash
wall=$(find /home/cta/WallPAPERS -type f | shuf | head -n1 ) && (wal -a 90 -g -i $wall > /dev/null)

