import unreal

all_actors = unreal.EditorLevelLibrary.get_all_level_actors()

for actor in all_actors:
    mesh_components = actor.get_components_by_class(unreal.StaticMeshComponent)
    if not mesh_components:
        mesh_components = actor.get_components_by_class(unreal.SkeletalMeshComponent)

    for mesh_component in mesh_components:
        if mesh_component.get_editor_property("render_custom_depth"):
            stencil_value = mesh_component.get_editor_property("custom_depth_stencil_value")
            print(f"{actor.get_name()} | Stencil Value: {stencil_value}")
