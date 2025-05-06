import unreal

# Get the world and camera
world = unreal.EditorLevelLibrary.get_editor_world()
camera_actors = unreal.GameplayStatics.get_all_actors_of_class(world, unreal.CameraActor)
camera = camera_actors[0] if camera_actors else None

if camera:
    # Capture scene
    viewport = unreal.ViewportClient()
    viewport.take_high_res_screenshot(1920, 1080, "Segmentation.png")
    print("Segmentation captured!")

else:
    print("No camera found in the scene.")
