import unreal

# def listAssetPaths():
#     # print ('reloaded')
#     EAL = unreal.EditorAssetLibrary

#     assetPaths = EAL.list_assets('/Game')

#     for i in assetPaths: 
#         print (i)

# def getSelectionContentBrowser():
#     EUL = unreal.EditorUtilityLibrary

#     selectedAssets = EUL.get_selected_assets()
    
#     for i in selectedAssets: 
#         print(i)

# LABEL = {
#     "Car": 1;
#     "Pedestrian": 2;
#     "TraffiLight": 3;
#     "Building": 4;
# }

# all_actors = unreal.EditorLevelLibrary.get_all_level_actors()

# for actor in all_actors:
#     actor_name = actor.get_name()

#     for label, stencil_values in LAEBL.items():
#         if label.lower() in actor_name.lower():


VEHICLE_STENCIL_VALUE = 1

# Get all actors in the level
all_actors = unreal.EditorLevelLibrary.get_all_level_actors()

print("\n🎬 Checking for 'vehCar' meshes:")
for actor in all_actors:
    # Get mesh components (Static or Skeletal)
    mesh_components = actor.get_components_by_class(unreal.StaticMeshComponent)
    if not mesh_components:
        mesh_components = actor.get_components_by_class(unreal.SkeletalMeshComponent)

    if mesh_components:
        for mesh_component in mesh_components:
            mesh = mesh_component.get_editor_property("static_mesh") if isinstance(mesh_component, unreal.StaticMeshComponent) else mesh_component.get_editor_property("skeletal_mesh")
            
            if mesh:
                mesh_name = mesh.get_name()
                
                # Check if the mesh name contains "vehCar"
                if "vehCar" in mesh_name:
                    print(f"🚗 Found Vehicle: {mesh_name} (Applying Stencil {VEHICLE_STENCIL_VALUE})")
                    
                    # Enable custom depth and assign stencil value on the Mesh Component
                    mesh_component.set_editor_property("render_custom_depth", True)
                    mesh_component.set_editor_property("custom_depth_stencil_value", VEHICLE_STENCIL_VALUE)

print("\n✅ Stencil applied to 'vehCar' meshes!")
