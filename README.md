# Roadmaps

*Members: Ziwei Gu, Tushar Khan, Kathy Byun, Ruchika Dongre, William Bekerman*

### Objectives

##### Modeling and Simulaing Traffic Networks
Our first task is to model a sample traffic network. We will start by generating our own "virtual" networks that may or may not be optimally designed, and later build models of existing networks for various cities. We also want to build an appealing interactive UI which will not only display the network but also incorporate useful visual indicators for important features of the network. Along with generating a network, we also want to generate simulation data for what traffic flow might look like on the given network. This is a more nuanced problem which will affect the rest of the pipeline significantly, so it will be a key focus over the course of this project.

##### Analyzing Traffic Networks
Our next task is to identify bottlenecks and stresses in the network from our simulations to determine where and how improvements to the network should be made. To do this, we will use heuristics to quantify certain properties of the network and specifically of its edges. We will also classify different types of networks and edges based on their capacity, effectiveness, accident rates, connectedness, etc. using unsupervised machine learning models. The goal here is to generate a comprehensive analysis report for any given network that we can use to begin "fixing" the network.

##### Optimizing Traffic Networks
Our ultimate task is to use the generated analysis reports to train supervised machine learning models to identify optimal networks. Optimal here may refer to a few things, such as minimized traffic density, traveling time, or even probability of an accident. We may even want to optimize a network within a certain constraint, such as a budget. Thus we will create various evaluation functions to quantify the properties we want to optimize, and use the data collected by our simulations to train our models. We want to use these models to suggest changes to a given traffic network that will improve some aspect of it. These changes may be minimal, like changing traffic light timings, or they may be drastic, like adding a new superhighway through the middle of the network. Whatever the case, these suggestions will be backed by simulations confirming their plausibility and could offer new insights into how to design an efficient and optimal traffic network for future projects.


### Progress
In our first semester working on this project, we successfully completed the first half of the pipeline. That includes building the model for the networks and a system to run simulations on top of it. We also built two visualizations to demonstrate how the simulation runs and the what analytics it produces.

##### Model
The model is our underlying representation of traffic networks. We had two goals in mind when designing our model - scalability and extensibility. We wanted our model to be scalable, in the sense that it should not be difficult to represent very large traffic networks the size of real cities once we could get it working for smaller networks. We also wanted it to be extensible, in the sense that it should be easy to add more features to the network representation to continually make it more realistic without breaking the rest of the pipeline.

Ultimately, we built our model as a directed graph. We designed our base classes as a general directed graph, with both the Node and Edge classes inheriting from a general Traversable class. The Traversable class contains a single method called `traverse`, which takes as input some starting time `t` and returns the amount of time it would take to cross the object as a function of `t`. Then, when computing the shortest path between any two nodes, we can call `traverse` on the graph component to get the weight of both edges and nodes. The reason for this design choice was that we wanted to be able to model nodes with a weight, since it actually takes time to cross an intersection in the real world, especially if that intersection is a stop sign or a red light. More importantly however, this allows us to change the behavior of `traverse` for each graph component to represent different kinds of things a car might have to cross, while still accurately reflecting the amount of time it takes to cross them. In other words, we could easily add features to our model like additional lanes, stop signs, traffic lights, even environmental effects - which directly affect the flow of traffic and therefore our simulation - without having to change anything in our codebase other than a single `traverse` method. This is an example of how we designed our model to be extensible.

We want to eventually be able to train models on the data we collect from our networks. Thus, we needed a way to generate random, dummy networks which we call *virtual networks*. Virtual networks are simply random traffic network models that are strongly connected, generated from some pre-defined parameters. One concern that was brought up was making these virtual networks as similar to real traffic networks as possible. This is the purpose of the parameters - so we can better control the randomness involved in generating the network. However, there is more we could do (see [What's Next?](https://github.com/CornellDataScience/Insights-Roadmaps/blob/master/README.md#whats-next) below). On the other hand, we have *real networks*, which are used to model traffic networks in the real world. Currently, we can generate very crude representations of these networks using a Python package called OSMnx, but this is also something that will need to be improved. These networks are generated by a network factory module that abstracts away the algorithms used to generate both real and virtual networks. 

##### Simulation
todo

##### Visualizations
a paragraph about google maps vis

a paragraph about matplotlib vis

### Lessons Learned


### What's Next?

##### Improving Model
There are many ways we can continue to improve our underlying traffic network model. First and foremost is making it more realistic. This is a requirement that will never be fully satisfied, as there are always real-world features of traffic networks that we could incoorporate into our model. Some of these that we have in mind are pedestrian crossing, vehicle-specific roads (like truck-only roads), and even environmental effects (like a bridge that has some probability of freezing over). Since we've built our model with extensiblity in mind, many of these improvements should not be very difficult to implement. 

We also need to improve how we generate both real and virtual networks. Currently to generate real networks, we simply extract the data from a Python package called OSMnx, and use the distances of roads as weights. But we actually don't capture as much information as our model can support. This is obviously one area of improvement we will need to focus on, especially as our model becomes more and more complex. Additionally, we want to improve the generation of virtual networks to make them more realistic, while still being random. One idea we have is to sample many real networks, break them apart, and stitch them back together in some controlled way to produce a virtual network built from real network components. There are of course many more variations of this idea, but the general principle is using real networks as the base of our virtual networks.

##### Improving Simulation
todo

##### Analysis and Optimization
This will be the focus of this project moving forward. We've spent a lot of time and thought in designing a reliable system to simulate traffic networks. The next step is to take these simulations, analyze them, and use the analysis to optimize new traffic networks. This will be an exciting problem to tackle, especially with much of the grunt work already out of the way. Below is an outline of some ideas we have on how to accomplish this.

When we say "analyze the simulation", we mean collect data on the results of the simulation that can be used in evaluation functions to determine the quality of some aspect of the network. For example, if we wanted to measure how much traffic congestion is accumulated on a given traffic network configuration, we might track the total waiting time of all the cars and return it as an evaulation function that we want to minimize. Thus, when we say we want to improve the analysis of our networks, we mean we want to collect much more detailed statistics about it, including which nodes or edges are particularly contributing to that statistic (is one road primarily responsible for traffic congestion in a network?). Some statistics that could be useful to collect include building a probability model for accident rates, interaction with pedestrians, fuel consumption (function of how often cars accelerate and decelerate), etc.

Once we have these statistics, we want to change the configuration of the traffic network within some constraint (like time or cost) to improve some particular aspect of it. Some ways we might be able to change a network's configuration is by adding or removing roads or lanes, globally changing the traffic light sequences, manipulating how intersections restrict traffic flow, etc. The way in which this optimization is carried out will be the real challenge. One way could be using genetic algorithms in which the fitness is the evaluation of a network and random mutations cause changes to these networks in a controlled way. A more difficult but rewarding approach could be using some supervised machine learning model trained on virtual networks.
