import unreal

def check_selected_stencil():
    editor_actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    selected_actors = editor_actor_subsystem.get_selected_level_actors()

    if not selected_actors:
        print("⚠️ No actor selected. Please select an actor in the viewport.")
        return

    for actor in selected_actors:
        mesh_components = actor.get_components_by_class(unreal.StaticMeshComponent)

        if not mesh_components:
            print(f"❌ No StaticMeshComponent found in selected actor: {actor.get_name()}")
            continue

        for mesh_component in mesh_components:
            stencil_value = mesh_component.get_editor_property("custom_depth_stencil_value")
            render_custom_depth = mesh_component.get_editor_property("render_custom_depth")

            print(f"🎯 Selected Actor: {actor.get_name()}")
            print(f"   - Stencil Value: {stencil_value}")
            print(f"   - Custom Depth Enabled: {render_custom_depth}")

# Run the function
check_selected_stencil()
