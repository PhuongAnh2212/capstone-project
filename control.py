import unreal
import time

# Get the world
editor_world = unreal.EditorLevelLibrary.get_editor_world()

# Find the car
vehicle_name = "SM_vehTruck_vehicle04"  # Change to match your vehicle's Blueprint name
vehicle = None

# Find the actor by its class
actors = unreal.GameplayStatics.get_all_actors_of_class(editor_world, unreal.Actor)
for actor in actors:
    if vehicle_name in actor.get_name():
        vehicle = actor
        break

if not vehicle:
    print("Vehicle not found. Make sure it's spawned in the scene.")
    exit()

print(f"Found vehicle: {vehicle.get_name()}")

# Function to apply movement (Throttle and Steering)
def apply_movement(throttle, steering):
    if not vehicle:
        return
    
    # Set throttle and steering using Blueprint functions
    vehicle.set_actor_location(vehicle.get_actor_location() + unreal.Vector(50 * throttle, 0, 0))  # Move Forward
    vehicle.set_actor_rotation(vehicle.get_actor_rotation() + unreal.Rotator(0, 0, -steering * 5))  # Turn

# Real-time control loop (Simulating user input)
try:
    while True:
        user_input = input("Enter movement (W/A/S/D or Q to quit): ").strip().lower()
        
        if user_input == "w":  # Move forward
            apply_movement(1, 0)
        elif user_input == "s":  # Move backward
            apply_movement(-1, 0)
        elif user_input == "a":  # Turn left
            apply_movement(0.5, 1)
        elif user_input == "d":  # Turn right
            apply_movement(0.5, -1)
        elif user_input == "q":  # Quit
            break
        else:
            print("Invalid input. Use W/A/S/D to control the car.")
            
except KeyboardInterrupt:
    print("Control stopped.")

print("Car control script ended.")
