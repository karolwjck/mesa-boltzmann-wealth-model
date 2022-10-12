import mesa
from MoneyModel import MoneyModel
from mesa.visualization.ModularVisualization import VisualizationElement, CHART_JS_FILE

def agent_portrayal(agent):
    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "r": 0.5}

    if agent.wealth > 0:
        portrayal["Color"] = "green"
        portrayal["Layer"] = 0
    else:
        portrayal["Color"] = "grey"
        portrayal["Layer"] = 1
        portrayal["r"] = 0.3
    return portrayal


# the ModularServer needs tobe prevfixed and written as "mesa.visualization.ModularServer.."
grid = mesa.visualization.CanvasGrid(agent_portrayal, 10, 10, 500, 500)
server = mesa.visualization.ModularServer(MoneyModel, [grid], "Mesa Boltzmann Wealth Model", {"N": 100, "width": 10, "height": 10})

# Gini Graph Vizualization
chart = mesa.visualization.ChartModule([{"Label": "Gini",
                      "Color": "Black"}],
                    data_collector_name='datacollector')

server = mesa.visualization.ModularServer(MoneyModel,
                       [grid, chart],
                       "Money Model",
                       {"N":100, "width":10, "height":10})

server.port = 8521 # The default