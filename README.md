# mesa-boltzmann-wealth-model
[Mesa](https://github.com/projectmesa/mesa) is a Python framework for [agent-based modeling](https://en.wikipedia.org/wiki/Agent-based_model). 

## How it works?
The tutorial model is a very simple simulated agent-based economy, drawn from econophysics and presenting a statistical mechanics approach to wealth distribution [Dragulescu2002]. The rules of our tutorial model:

1. There are some number of agents.
2. All agents begin with 1 unit of money.
3. At every step of the model, an agent gives 1 unit of money (if they have it) to some other agent.

![This is an image](/assets/gif.gif)

## How to run it?
To launch the interactive server, and run the application type in the following (keeping in mind you're in the correct directory)

```
    $ python3 src/run.py
```

## FAQ
**What if my browser doesn't open automatically when running run.py?**
###### Paste the following URL in your browser http://127.0.0.1:8521/. When the visualization loads, press Reset, then Run.


## Additional information

[Agent-based model, Wikipedia](https://en.wikipedia.org/wiki/Agent-based_model)

[Milakovic, M. A Statistical Equilibrium Model of Wealth Distribution. February, 2001.](https://editorialexpress.com/cgi-bin/conference/download.cgi?db_name=SCE2001&paper_id=214)

[Dragulescu, A and Yakovenko, V. Statistical Mechanics of Money, Income, and Wealth: A Short Survey. November, 2002](http://arxiv.org/pdf/cond-mat/0211175v1.pdf)

