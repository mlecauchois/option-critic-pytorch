#!/bin/bash 
python main.py --switch-goal True --env fourrooms --num-options 4 --noise 0.05 --bottleneck-size 4 --learning-rate 0.001 --max_steps_ep 500 --seed 0 --termination-reg 0
python main.py --switch-goal True --env fourrooms --num-options 4 --noise 0.05 --bottleneck-size 64 --learning-rate 0.001 --max_steps_ep 500 --seed 0 --termination-reg 0
python main.py --switch-goal True --env fourrooms --num-options 4 --noise 0.05 --bottleneck-size 4 --learning-rate 0.001 --max_steps_ep 500 --seed 1 --termination-reg 0
python main.py --switch-goal True --env fourrooms --num-options 4 --noise 0.05 --bottleneck-size 4 --learning-rate 0.001 --max_steps_ep 500 --seed 2 --termination-reg 0
python main.py --switch-goal True --env fourrooms --num-options 4 --noise 0.05 --bottleneck-size 64 --learning-rate 0.001 --max_steps_ep 500 --seed 1 --termination-reg 0
python main.py --switch-goal True --env fourrooms --num-options 4 --noise 0.05 --bottleneck-size 64 --learning-rate 0.001 --max_steps_ep 500 --seed 2 --termination-reg 0

