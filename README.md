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

Ultimately, we built our model using a graph...
todo

##### Simulation
todo

##### Visualizations
a paragraph about google maps vis

a paragraph about matplotlib vis

### Lessons Learned


### What's Next?
