import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import os
from tqdm import tqdm
from tensorboard.backend.event_processing.event_accumulator import EventAccumulator

TAG_NAME = "episode_lengths"
log_dir = "runs/no_termination_reg_experiment"

dfs = []
for experiment in tqdm(os.listdir(log_dir)):

    experiment = os.path.join(log_dir, experiment)
    seed = float(experiment.split("seed-")[1].split("-noise")[0])
    noise = float(experiment.split("noise-")[1].split("-bottleneck")[0])
    bottleneck = int(experiment.split("bottleneck-")[1].split("-")[0])
    event_accumulator = EventAccumulator(experiment)
    event_accumulator.Reload()

    steps = {x.step for x in event_accumulator.Scalars(TAG_NAME)}
    x = list(range(len(steps)))
    y = [x.value for x in event_accumulator.Scalars(TAG_NAME)]
    y = [np.mean(y[max(0,i-10):i+1]) for i in range(len(y))]
    df = pd.DataFrame({"steps": x, TAG_NAME: y})
    df["seed"] = seed
    df["noise"] = noise
    df["bottleneck"] = bottleneck
    print(bottleneck)
    print(noise)
    print(seed)
    dfs.append(df)
data = pd.concat(dfs).reset_index()
fig, ax = plt.subplots()
sns.lineplot(data=data, x="steps", y=TAG_NAME, hue="bottleneck")
fig.savefig("plot.png", dpi=300)