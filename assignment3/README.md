# Statistical Techniques for Data Science & Robotics
# Assignment 3: Application of Sampling

## Overview
The problem was to solve the traveling salesman problem using the Simulated Annealing method. 30 most populated Russian cities was selected for TSP. The SA method was implemented in Python. 
## Data Processing
The data about Russian cities (name, location, and population) were taken from [HFLabs git repository](https://github.com/hflabs/city/blob/master/city.csv). To calculate the distance, the GeoPy library was used. The simualated annealing method was implemented from scratch. 
## Results
### Find optimal path
To find the optimal path, we set annealing rate to 0.99. This contributed to the fact that a global, not a local optimum was found. The resulting distance is equal to 18813.84 km. The picture below shows the path:
![The optimal path for TSP](https://drive.google.com/uc?export=view&id=1fZcvFYF5aPgBjgCCifFnQKUyI3sLNYmj "The optimal path for TSP")
### Compare the speed of convergence

The task was to compare the speed of convergence for fast, slow, and middle cooling. To define the type of cooling, we set different annealing rates. So, for slow cooling rate is 0.99, for middle - 0.85, and for fast - 0.7.   
Initaily, we decresed the temperature every 100 steps for all experiments, but in such a case the slow cooling takes much more time than others. To make the visualization more convinient, we decided to decrease temerature every 50 steps for slow cooling and limited maximimum number of iteration by 5000 for all cases. The result is following:
![Compare the speed of convergence](https://drive.google.com/uc?export=view&id=1x5ud04PYoetTG6ZL6mg8LYOzjr468B9k "Compare the speed of convergence")

The slow cooling found a path 25210.90 km long.  
The middle cooling found a path 21179.85 km long.  
The fast cooling found a path 22165.77 km long.   

Also we could nitice, that the fast and middle cooling converge completely, while the slow cooling stopped its work because of limitted number of iterations. We could assume, that the fast and middle cooling found out the local optimum. It happens because of inappropriate chouce of annealing rate. 

### Visulization

For visualization we used matplotlib animations methods. The video shows how changed the temerature and the total distance during the search for the optimal path. 


https://user-images.githubusercontent.com/54397314/164974427-dd7f5d38-2e5e-4d88-9606-f52d90d14e85.mp4

