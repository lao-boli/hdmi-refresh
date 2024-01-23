#!/bin/bash
export DISPLAY=:0
xrandr --output HDMI-1 --off
sleep 0.5
xrandr --output HDMI-1 --auto
