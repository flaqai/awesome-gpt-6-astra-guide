"""Original Blender teaching script. Run in a fresh background Blender process.

Creates an editable geometric desk robot and a 6-second assembly timeline.
No model API, downloads, external assets, render, or video export is performed.
Validated for Python syntax only; Blender runtime has not been tested here.
"""
from pathlib import Path
import bpy

if not bpy.app.background:
    raise RuntimeError('Use the documented background command, not an open editing session.')

output = Path.cwd() / 'outputs' / 'desk-robot'
blend_path = output / 'desk-robot.blend'
if blend_path.exists():
    raise FileExistsError(f'Choose a fresh working directory or move the previous output: {blend_path}')

bpy.ops.wm.read_factory_settings(use_empty=True)
scene = bpy.context.scene
scene.render.fps = 24
scene.render.fps_base = 1.0
scene.frame_start = 1
scene.frame_end = 144


def material(name, color):
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = (*color, 1)
    return mat


mint = material('MAT_mint', (0.25, 0.65, 0.52))
ink = material('MAT_ink', (0.06, 0.09, 0.14))
sun = material('MAT_sun', (0.95, 0.65, 0.20))
# Locations and dimensions are an original, deliberately simple silhouette.
parts = [
    ('BOT_body', (0, 0, 1.25), (1.1, 0.7, 1.1), mint, (0, 0, 0)),
    ('BOT_head', (0, 0, 2.25), (1.3, 0.8, 0.7), mint, (0, 0, 1.0)),
    ('BOT_eye_L', (-0.3, -0.43, 2.3), (0.16, 0.08, 0.2), ink, (-0.4, -0.4, 1.0)),
    ('BOT_eye_R', (0.3, -0.43, 2.3), (0.16, 0.08, 0.2), ink, (0.4, -0.4, 1.0)),
    ('BOT_foot_L', (-0.32, 0, 0.35), (0.5, 0.9, 0.7), ink, (-0.8, 0, 0)),
    ('BOT_foot_R', (0.32, 0, 0.35), (0.5, 0.9, 0.7), ink, (0.8, 0, 0)),
    ('BOT_antenna', (0, 0, 2.85), (0.14, 0.14, 0.5), sun, (0, 0, 1.4)),
]
for index, (name, location, dimensions, mat, offset) in enumerate(parts):
    bpy.ops.mesh.primitive_cube_add(size=1, location=location)
    obj = bpy.context.object
    obj.name = name
    obj.dimensions = dimensions
    obj.data.materials.append(mat)
    # Start exploded, assemble in staggered groups, hold the final pose.
    obj.location = tuple(value + delta for value, delta in zip(location, offset))
    obj.keyframe_insert(data_path='location', frame=1)
    obj.keyframe_insert(data_path='location', frame=24 + index * 6)
    obj.location = location
    obj.keyframe_insert(data_path='location', frame=72 + index * 6)
    obj.keyframe_insert(data_path='location', frame=144)

scene.frame_set(144)
output.mkdir(parents=True, exist_ok=True)
bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))
print(f'Saved {blend_path}; 7 editable meshes, frames 1–144 at 24 fps. No video rendered.')
