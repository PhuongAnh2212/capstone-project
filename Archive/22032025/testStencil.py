import unreal

def set_stencil_for_template_actors(stencil_value=1):
    editor_actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    all_actors = editor_actor_subsystem.get_all_level_actors()

    updated_actors = []

    print(f"🔍 Setting stencil for TemplateActors with Static Mesh containing 'vehCar'...")

    for actor in all_actors:
        if "TemplateActor" in actor.get_name():  # Filter TemplateActor
            mesh_components = actor.get_components_by_class(unreal.StaticMeshComponent)

            for mesh_component in mesh_components:
                static_mesh = mesh_component.get_editor_property("static_mesh")

                if static_mesh and "vehCar" in static_mesh.get_name():  # Filter meshes with "vehCar"
                    print(f"✅ Updating: {actor.get_name()} | Mesh: {static_mesh.get_name()}")

                    # Enable stencil settings
                    mesh_component.set_editor_property("render_custom_depth", True)
                    mesh_component.set_editor_property("custom_depth_stencil_value", stencil_value)

                    actor.modify()  # Mark changes
                    updated_actors.append(actor.get_name())

    if updated_actors:
        print(f"\n🎯 Successfully updated {len(updated_actors)} actors:")
        for name in updated_actors:
            print(f" - {name}")
    else:
        print("\n⚠️ No TemplateActors with 'vehCar' meshes found. Check names.")

# Run the function
set_stencil_for_template_actors()
