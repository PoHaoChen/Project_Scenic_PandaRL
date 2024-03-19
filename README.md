This project is a case study based on model in https://github.com/aidudezzz/deepworlds/tree/dev/examples/panda made by Yung Tai Shih, Tsu Hsiang Chen, Chun Kai Yang, Yan Feng Su, Hsuan Yu Liao, Jiun Kai Yang and supervised by Prof. Chih-Tsun Huang from Dept. of Computer Science, National Tsing Hua University.

Repuirements:

Deepbots: 
https://github.com/aidudezzz/deepbots

Webots (version 2022b was used):
https://cyberbotics.com/ 

Scenic:
https://scenic-lang.readthedocs.io/en/latest/index.html

Explaination:
Models are trained models, copy and paste "ddpg" into "panda/panda_goal_reaching/controllers/robot_supervisor_manager/tmp" to apply. "panda_scenic_goal_reaching" uses Scenic script to control the objects and train for a goal reaching task.
"panda_obstacle" uses Scenic script to control the objects and train for a goal reaching while avoiding fixed obstacle task.
"panda/panda_goal_reaching/controllers/robot_supervisor_manager/PlotTestingData.py" will plot the testing datas.

How to run:

1. Open the .wbt file under "panda/panda_goal_reaching/world" in Webots.
1. If a new training / testing is wanted, "tmp" or "export" need to be manually clean up.
1. Scenic scripts can be re-write in order to perform various scenarios, but settings of the model need to be change as well.