import random 
# Constants 
MISSION_TYPES = ["Exploration", "Diplomacy", "Combat", "Rescue", "Scientific Research"] 
# Ship systems, resources, and crew 
planets = ["Red", "Green", "Blue"]
ship = { 
		"systems": { 
		"shields": 100, 
		"weapons": 100, 
		"engines": 100, 
		"sensors": 100 
		}, 
		"resources": { 
			"energy": 1000, 
			"torpedoes": 10 
		}, 
		"crew": { 
			"Picard": "Command", 
			"Riker": "Command", 
			"Data": "Operations", 
			"Worf": "Operations", 
			"La Forge": "Operations", 
			"Crusher": "Sciences", 
			"Troi": "Sciences" 
		} 
	} 

def main(): 
	print("Welcome to the Star Trek: TNG Mission Simulator!") 
	score = 0 
	turns = 0 

	while True: 
		display_status() 
		action = get_user_action() 

	if action == "1": 
		score += run_mission(score) 
	elif action == "2": 
		repair_system() 
	elif action == "3": 
		add_crew_member() 
	elif action == "4": 
		print(f"Simulation ended. Final score: {score}") break
	else: 
		print("Invalid action. Please try again.") 
		
	turns += 1 
	handle_random_event() 

	if turns % 3 == 0: 
		replenish_resources() 

def display_status(): 
 tempval = ["1"]["2"]["3"]
 int(input("What wu"))
def get_user_action(): 
 user_action = int(input("Select your choice:" n\, "1 = Run mission" n\  "2 = Repair system" n\ "3 = Add a new crew member" n\ "4 = End Simulation"))

 def run_mission(score):
	mission_type = random.choice(MISSION_TYPES) 
	
	print(f"\nNew mission: {mission_type}") 
	if mission_type == "Exploration":
		print("roll for sensors check")
		import random
		skill_check = random.randint(1,6)
		print(skill_check)
		if skill_check == 1 or skill_check == 2:
			print("engine check failed") and ship["systems"]["sensors"] - 1
		else:
			print("you passed the check")
		print("Start mission")

		ship["crew"]["Picard"] 
		print("Command wishes for us to investigate this planet")
		Planet_explorarion = random.choice(planets)
		if planets == "Green":
			i = 1
			for i in range(1):
				Guess = int(input("Guess the right number between: 1 and 2"))
				if Guess == i:
					print("Exploration successful")
					mission_report = "mission succesful"
				else :
					print("exploration failed")
					mission_report = "mission failed"
		if planets == "Blue":
			x = random.randint(1,5)
			for x in range(5):
				Guess = int(input("Guess the right number between: 1, 2, 3, 4 and 5"))
				if Guess == i:
					print("Exploration successful")
					mission_report = "mission succesful"
				else:
					print("exploration failed")
					mission_report = "mission failed"
		if planets == "Blue":
			x = random.randint(1,10)
			for y in range(10):
				Guess = int(input("Guess the right number from 1 to 10"))
				if Guess == y:
					print("Exploration successful")
					mission_report = "mission succesful"
				else:
					print("exploration failed")
					mission_report = "mission failed"
		if mission_report == "mission succesful":
			new_score = score + 5	
		elif mission_report == "mission failed":
		  newscore = score - 5 			
			    

	

	# Return the score earned from the mission 

def repair_system(): 

# TODO: Implement system repair functionality
 
def add_crew_member(): 
# TODO: Implement functionality to add a new crew member 

def handle_random_event():
# TODO: Implement random events that can occur during the simulation 

def use_resource(resource, amount): 
# TODO: Implement resource usage logic 

def replenish_resources(): 
# TODO: Implement resource replenishment logic 

main()
