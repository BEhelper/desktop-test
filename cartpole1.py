import gym
import random
import numpy as np
import tflearn
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
from statistics import median, mean
from collections import Counter
#import universe
#from gym import Box2D
#from gym.envs.box2d.lunar_lander import LunarLander


##env = gym.make("Taxi-v2")
###env = gym.make("LunarLander-v2")
##
##observation = env.reset()
##for _ in range(100):
##  env.render()
##  action = env.action_space.sample() # your agent here (this takes random actions)
##  observation, reward, done, info = env.step(3)
##  print(reward, action, env.action_space.show())


LR = 1e-3
env = gym.make("CartPole-v0")
#env = gym.make("LunarLander-v2")

#env = gym.make("MountainCar-v0")
# env = gym.make("AirRaid-v0")
# env = gym.make("Breakout-ram-v0")
# env = gym.make("MsPacman-v0")


env.reset()
goal_steps = 500
score_requirement = 50
initial_games = 100

number_of_frames = 500



def some_random_games_first():
    totalScore = 0
    number_of_games = 10
    global number_of_frames

    # Each of these is its own game.
    score = 0
    for episode in range(number_of_games):
        print(" previous score: ", score)
        print("")
        print("-------------------------")
        print("       new game          ")
        print("-------------------------")
        score = 0
        env.reset()
        # this is each frame, up to 200...but we wont make it that far.
        for t in range(number_of_frames):
            # This will display the environment
            # Only display if you really want to see it.
            # Takes much longer to display it.
            env.render()

            # This will just create a sample action in any environment.
            # In this environment, the action can be 0 or 1, which is left or right
            action = env.action_space.sample()

            # this executes the environment with an action,
            # and returns the observation of the environment,
            # the reward, if the env is over, and other info.

            # 0 sit still
            # 1 fire
            # 2 right
            # 3 left?
            # 4 right shoot
            # 5 left shoot


            # if action == 2:
            #     action = 4
            # elif action == 3:
            #     action = 5


            observation, reward, done, info = env.step(action)
            # print(reward),
            score += reward
            totalScore += reward
            if t == (number_of_frames - 1):
                # number_of_frames is likely too small, so increase it
                number_of_frames = int(number_of_frames * 1.33)
                print("reached the end--------" * 10 )

            #print(action),
            if done:
                break

    average_score = totalScore / number_of_games
    print("average_score: ", average_score)
some_random_games_first()
