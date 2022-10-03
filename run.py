from money_model import *
# import numpy as np
import csv 
from matplotlib import pyplot as plt

# model = MoneyModel(50, 10, 10)
# for i in range(20):
#     model.step()

# agent_counts = np.zeros((model.grid.width, model.grid.height))
# for cell in model.grid.coord_iter():
#     cell_content, x, y = cell
#     agent_count = len(cell_content)
#     agent_counts[x][y] = agent_count
# plt.imshow(agent_counts, interpolation="nearest")
# plt.colorbar()

# If running from a text editor or IDE, remember you'll need the following:
# plt.show()

# model = MoneyModel(50, 10, 10)
# for i in range(100):
#     model.step()
    
# gini = model.datacollector.get_model_vars_dataframe()
# gini.plot()

# gini.to_csv("model_data.csv")

params = {"width": 10, "height": 10, "N": range(10, 500, 10)}

results = mesa.batch_run(
    MoneyModel,
    parameters=params,
    iterations=5,
    max_steps=100,
    number_processes=1,
    data_collection_period=1,
    display_progress=True,
)

keys = results[0].keys()
with open('batch_results.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(results)

