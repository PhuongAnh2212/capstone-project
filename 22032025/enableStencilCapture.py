import unreal

def setup_scene_capture():
    """Find SceneCapture2D and enable stencil capture settings."""
    
    # Find an existing SceneCapture2D actor
    scene_capture = None
    for actor in unreal.EditorLevelLibrary.get_all_level_actors():
        if isinstance(actor, unreal.SceneCapture2D):
            scene_capture = actor
            break

    if not scene_capture:
        print("❌ No SceneCapture2D found! Add one to your scene.")
        return

    print(f"✅ Found SceneCapture2D: {scene_capture.get_name()}")

    # Get SceneCaptureComponent2D
    capture_component = scene_capture.get_component_by_class(unreal.SceneCaptureComponent2D)

    if not capture_component:
        print("❌ No SceneCaptureComponent2D found in SceneCapture2D!")
        return

    print(f"🎥 Found SceneCaptureComponent2D in {scene_capture.get_name()}")

    # Show available flag settings
    show_flags = capture_component.get_editor_property("show_flag_settings")
    print(f"🔹 Available Show Flags: {show_flags}")

# Run the function
setup_scene_capture()
