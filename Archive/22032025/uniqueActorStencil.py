import unreal

# Get all actors in the current level
actors = unreal.EditorLevelLibrary.get_all_level_actors()

# Dictionary to store unique stencil values per class
class_stencil_map = {}
stencil_counter = 1  # Start stencil values from 1

# Store results for printing
results = []

# Loop through each actor
for actor in actors:
    actor_class = actor.get_class().get_name()  # Get actor class name

    # Assign a new stencil value if class is not in the dictionary
    if actor_class not in class_stencil_map:
        class_stencil_map[actor_class] = stencil_counter
        stencil_counter += 1  # Increment for next class

    stencil_value = class_stencil_map[actor_class]

    # Get all mesh components in the actor
    mesh_components = actor.get_components_by_class(unreal.StaticMeshComponent)
    
    for mesh in mesh_components:
        # Enable custom depth rendering
        mesh.set_editor_property("render_custom_depth", True)
        # Set stencil value based on class
        mesh.set_editor_property("custom_depth_stencil_value", stencil_value)

    # Store result for this actor
    results.append(f"Actor: {actor.get_name()} | Class: {actor_class} | Stencil Value: {stencil_value}")

# Print the final results
print("\n--- Stencil Values Assigned ---")
for res in results:
    print(res)

print("\nStencil values updated for all actors!")
