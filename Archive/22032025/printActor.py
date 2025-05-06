import unreal

# Get all actors in the current level
actors = unreal.EditorLevelLibrary.get_all_level_actors()

# Print all actor names
print(f"Total Actors in Scene: {len(actors)}")
for actor in actors:
    print(f"Actor: {actor.get_name()}, Class: {actor.get_class().get_name()}")
