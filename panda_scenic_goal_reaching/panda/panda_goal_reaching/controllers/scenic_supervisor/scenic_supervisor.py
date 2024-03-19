from controller import Supervisor, Robot

import scenic
from scenic.simulators.webots import WebotsSimulator

supervisor = Supervisor()
simulator = WebotsSimulator(supervisor)

path = supervisor.getCustomData()
print(f"Loading Scenic scenario {path}")
scenario = scenic.scenarioFromFile(path)
# current_time = 1.0

while True:
    scene, _ = scenario.generate()
    print("Starting new simulation...")
    simulator.simulate(scene, verbosity=2)
    # current_time = supervisor.getTime()
