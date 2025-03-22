import unreal

world = unreal.EditorLevelLibrary.get_editor_world()

for actor in unreal.EditorLevelLibrary.get_all_level_actors():
    if isinstance(actor, (unreal.SceneCapture2D, unreal.CameraActor)):
        unreal.EditorLevelLibrary.destroy_actor(actor)

camera_location = unreal.Vector(0, 0, 1000) 
camera_rotation = unreal.Rotator(-90, 0, 0)

camera_actor = unreal.EditorLevelLibrary.spawn_actor_from_class(
    unreal.CameraActor, camera_location
)
camera_actor.set_actor_rotation(camera_rotation, False)

# Get Camera Component
camera_component = camera_actor.get_component_by_class(unreal.CameraComponent)
if camera_component:
    camera_component.set_projection_mode(unreal.CameraProjectionMode.ORTHOGRAPHIC)
    camera_component.set_ortho_width(2048)  # Adjust to match your scene
    camera_component.set_editor_property("field_of_view", 90)
    print(f"📷 Camera '{camera_actor.get_name()}' created at {camera_location}.")

# 3️⃣ Create a SceneCapture2D Actor
scene_capture_actor = unreal.EditorLevelLibrary.spawn_actor_from_class(
    unreal.SceneCapture2D, camera_location
)
scene_capture_actor.set_actor_rotation(camera_rotation, False)

scene_capture_component = scene_capture_actor.get_component_by_class(
    unreal.SceneCaptureComponent2D
)

if scene_capture_component:
    scene_capture_component.set_editor_property("capture_source", unreal.SceneCaptureSource.SCS_FINAL_COLOR_LDR)

    scene_capture_actor.attach_to_actor(
        camera_actor,  
        unreal.Name("None"),  # Use an empty socket name or "None" explicitly  
        unreal.AttachmentRule.SNAP_TO_TARGET,  # Location rule  
        unreal.AttachmentRule.SNAP_TO_TARGET,  # Rotation rule  
        unreal.AttachmentRule.SNAP_TO_TARGET,  # Scale rule  
        False  # Weld simulated bodies  
    )
    print("🎥 Scene Capture 2D set up and attached to the camera.")

# 4️⃣ Create a Render Target in the Content Browser
asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
package_path = "/Game/RenderTarget"
asset_name = "RenderTarget"

render_target = asset_tools.create_asset(
    asset_name, package_path, unreal.TextureRenderTarget2D, unreal.TextureRenderTarget2D()
)

if render_target:
    render_target.set_editor_property("size_x", 1024)
    render_target.set_editor_property("size_y", 1024)
    render_target.set_editor_property("clear_color", unreal.LinearColor(0, 0, 0, 1))  # Black background
    scene_capture_component.set_editor_property("texture_target", render_target)

    print(f"📸 Render Target '{asset_name}' created and assigned.")

# 5️⃣ Lock the camera in place (Prevent movement)
camera_actor.set_actor_transform(camera_actor.get_actor_transform(), False, False)

print("\n✅ Scene Capture 2D camera setup is complete!")
