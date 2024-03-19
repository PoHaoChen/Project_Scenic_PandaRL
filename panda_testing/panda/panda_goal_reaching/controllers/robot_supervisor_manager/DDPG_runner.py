from numpy import convolve, ones, mean, random

from robot_supervisor_ddpg import PandaRobotSupervisor
from agent.ddpg import DDPGAgent
from controller import Supervisor

from robot_supervisor_manager import EPISODE_LIMIT, STEPS_PER_EPISODE, SAVE_MODELS_PERIOD, TESTING_LIMIT

def run(load_path):
    # Initialize supervisor object
    env = PandaRobotSupervisor()
    my_robot = env.getFromDef("Franka_Emika_Panda")
    my_robot.saveState("init")

    # The agent used here is trained with the DDPG algorithm (https://arxiv.org/abs/1509.02971).
    # We pass (10, ) as numberOfInputs and (7, ) as numberOfOutputs, taken from the gym spaces
    agent = DDPGAgent(alpha=0.000025, beta=0.00025, input_dims=[env.observation_space.shape[0]], tau=0.001, batch_size=64,  layer1_size=400, layer2_size=400, n_actions=env.action_space.shape[0], load_path=load_path) 
    
    episode_count = 0
    solved = False  # Whether the solved requirement is met

    # Run outer loop until the episodes limit is reached or the task is solved
    while not solved and episode_count < EPISODE_LIMIT:
        # state = env.reset()  # Reset robot and get starting observation
        my_robot.loadState("init")
        super(Supervisor, env).step(int(env.getBasicTimeStep()))
        state = env.get_default_observation()
        env.episode_score = 0

        print("===episode_count:", episode_count,"===")
        # env.target = env.getFromDef("TARGET%s"%(random.randint(1, 10, 1)[0])) # Select one of the targets
        # Inner loop is the episode loop
        for step in range(STEPS_PER_EPISODE):
            # In training mode the agent returns the action plus OU noise for exploration
            act = agent.choose_action(state)

            # Step the supervisor to get the current selectedAction reward, the new state and whether we reached the
            # the done condition
            new_state, reward, done, info = env.step(act*0.032)
            # process of negotiation
            while(new_state==["StillMoving"]):
                new_state, reward, done, info = env.step([-1])
            
            # Save the current state transition in agent's memory
            agent.remember(state, act, reward, new_state, int(done))

            env.episode_score += reward  # Accumulate episode reward
            # Perform a learning step
            if done or step==STEPS_PER_EPISODE-1:
                # Save the episode's score
                env.episode_score_list.append(env.episode_score)
                agent.learn()
                if episode_count%SAVE_MODELS_PERIOD==0:
                    agent.save_models()
                solved = env.solved()  # Check whether the task is solved
                break

            state = new_state # state for next step is current step's new_state

        print("Episode #", episode_count, "score:", env.episode_score)
        file = open("./exports/Episode-score.txt","a")
        file.write(str(env.episode_score)+'\n')
        file.close()
        episode_count += 1  # Increment episode counter

    # agent.save_models()
    # if not solved:
    #     print("Reached episode limit and task was not solved, deploying agent for testing...")
    # else:
    print("Task is solved, deploying agent for testing...")

    my_robot.loadState("init")
    super(Supervisor, env).step(int(env.getBasicTimeStep()))
    state = env.get_default_observation()
    test_count = 0
    while test_count < TESTING_LIMIT:
        record_step = 0
        env.episode_score = 0
        env.collision = False
        for step in range(STEPS_PER_EPISODE):
            act = agent.choose_action_test(state)
            state, reward, done, _ = env.step(act*0.032)
            # process of negotiation
            while(state==["StillMoving"]):
                state, reward, done, info = env.step([-1])
            
            env.episode_score += reward  # Accumulate episode reward
            record_step = record_step + 1
            if done or step==STEPS_PER_EPISODE-1:
                print("Testing #", test_count, "score:", env.episode_score)
                my_robot.loadState("init")
                super(Supervisor, env).step(int(env.getBasicTimeStep()))
                state = env.get_default_observation()
                break

        test_count += 1
        file = open("./exports/Episode-score.txt","a")
        file.write(str(env.episode_score)+'\n')
        file.close()
        file = open("./exports/Target-position.txt","a")
        file.write(str(env.target.getPosition()[0])+'\n')
        file.write(str(env.target.getPosition()[1])+'\n')
        file.write(str(env.target.getPosition()[2])+'\n')
        file.close()
        file = open("./exports/Episode-steps.txt","a")
        file.write(str(record_step)+'\n')
        file.close()
        file = open("./exports/Collision.txt","a")
        file.write(str(env.collision)+'\n')
        file.close()
        
