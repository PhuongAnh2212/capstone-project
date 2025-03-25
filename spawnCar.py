import unreal

# Get world reference
world = unreal.EditorLevelLibrary.get_editor_world()

# Load the car blueprint
vehicle_blueprint_path = "Game/Vehicle/vehCar_vehicle02/BP_vehCar_vehicle02"
vehicle_blueprint = unreal.EditorAssetLibrary.load_asset(vehicle_blueprint_path)

if not vehicle_blueprint:
    print("Error: Could not load vehicle blueprint.")
    exit()

# Get the player pawn (character or vehicle)
player_pawn = unreal.GameplayStatics.get_player_pawn(world, 0)

if not player_pawn:
    print("Error: Could not find player.")
    exit()

# Get the player's location and rotation
spawn_location = player_pawn.get_actor_location()
spawn_rotation = player_pawn.get_actor_rotation()

# Adjust the position slightly to prevent overlap
spawn_location.z += 100  # Raise the car slightly above the ground

# Spawn the vehicle at the player's position
spawned_vehicle = unreal.GameplayStatics.begin_deferred_actor_spawn_from_class(
    world, vehicle_blueprint, unreal.Transform(spawn_location, spawn_rotation)
)

if spawned_vehicle:
    unreal.GameplayStatics.finish_spawning_actor(spawned_vehicle, unreal.Transform(spawn_location, spawn_rotation))
    print(f"Spawned vehicle at player's location: {spawn_location}")
else:
    print("Vehicle spawn failed.")
