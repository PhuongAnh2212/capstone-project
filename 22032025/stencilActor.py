import unreal

def set_stencil_for_specific_actor(actor_name, stencil_value=1):
    editor_actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    all_actors = editor_actor_subsystem.get_all_level_actors()

    for actor in all_actors:
        if actor.get_name() == actor_name:
            mesh_components = actor.get_components_by_class(unreal.StaticMeshComponent)

            if not mesh_components:
                print(f"❌ No StaticMeshComponent found in {actor_name}")
                return

            for mesh_component in mesh_components:
                print(f"✅ Updating: {actor_name} | Stencil: {stencil_value}")

                # Enable stencil settings
                mesh_component.set_editor_property("render_custom_depth", True)
                mesh_component.set_editor_property("custom_depth_stencil_value", stencil_value)

                actor.modify()  # Mark changes

            print(f"\n🎯 Successfully updated stencil for {actor_name}")
            return
    
    print(f"⚠️ Actor '{actor_name}' not found in the level.")

# Run the function with your actor's name
set_stencil_for_specific_actor("TemplateActor_UAID_D45D6454B40F8AF200_1565829781")
