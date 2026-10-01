"""Build a basic whitebox/blockout of the clinic (operating room +
recovery room, connected by a doorway) for "The Ocean of Time" --
sc06/sc07 in episodes/the_ocean_of_time.json.

STATUS: UNVERIFIED. This is the first Unreal Python automation script
in this repo (see PIPELINE.md -- the Python automation layer was
explicitly flagged as "not yet verified against real behavior"). It's
written from the standard, documented `unreal` module API, but has not
been run inside a real Unreal Editor session. Run it, and if anything
errors or behaves differently than described below, report the exact
error message back rather than assuming the next fix -- that's how
this gets corrected against real behavior instead of more guessing.

WHY A BLOCKOUT, NOT A FINISHED ROOM: per
scenes/the_ocean_of_time/ASSET_SOURCING.md, no free (or even clearly
good paid) clinic/hospital asset pack was found. Rather than wait on
that, this builds a plain geometric blockout -- walls, floor, a
doorway gap -- using only Unreal's own built-in basic shapes
(/Engine/BasicShapes/Cube), the same kind of blockout approach used in
normal level-design workflow before dressing a space with real
furniture/props. It gives you a real, walkable room to block sc06/sc07
in while a proper clinic pack is still being sourced.

HOW TO RUN:
    Unreal Editor -> Window -> Developer Tools -> Output Log -> the
    "Cmd" box at the bottom accepts Python one-liners, but for a full
    script like this, use Tools -> Execute Python Script... and point
    it at this file. (Menu wording may differ slightly by engine
    version -- if "Execute Python Script" isn't where you expect, the
    Output Log's Python console can also `exec(open(r"<path>").read())`
    the file directly.)

    Requires the Python Editor Script Plugin enabled (Edit -> Plugins
    -> search "Python Editor Script Plugin" -> enable -> restart, if
    not already on).

ENGINE VERSION NOTE: this targets the UE 5.1+ subsystem-based API
(`unreal.EditorActorSubsystem`), which is the currently-recommended
replacement for the older `unreal.EditorLevelLibrary` spawn functions.
If your installed version is older and `EditorActorSubsystem` isn't
found, tell me the exact error -- there's a straightforward
EditorLevelLibrary equivalent to swap in instead.
"""

import unreal

# ---------------------------------------------------------------------------
# Configurable dimensions (Unreal units = centimeters)
# ---------------------------------------------------------------------------

WALL_HEIGHT = 300.0       # 3m
WALL_THICKNESS = 20.0     # 20cm

# Operating room (sc06) and recovery room (sc07), side by side,
# connected by a doorway in the shared wall.
OP_ROOM_SIZE = (600.0, 500.0)        # width (X), depth (Y) -- 6m x 5m
RECOVERY_ROOM_SIZE = (600.0, 500.0)  # 6m x 5m

DOORWAY_WIDTH = 120.0     # 1.2m gap left open in the shared wall
DOORWAY_HEIGHT = 220.0    # door opening height; wall above the opening still fills in

ORIGIN = unreal.Vector(0.0, 0.0, 0.0)  # operating room's near-left corner

CUBE_MESH_PATH = "/Engine/BasicShapes/Cube.Cube"

# ---------------------------------------------------------------------------

def _get_actor_subsystem():
    return unreal.get_editor_subsystem(unreal.EditorActorSubsystem)


def _spawn_cube(name, location, rotation, scale):
    """Spawns a StaticMeshActor using the engine's basic Cube mesh,
    then scales/positions it to act as a wall or floor segment.
    Cube.Cube is 100x100x100 units by default, so `scale` is in meters
    (scale of 1.0 on an axis = 100 Unreal units on that axis)."""
    actor_subsystem = _get_actor_subsystem()
    actor = actor_subsystem.spawn_actor_from_class(
        unreal.StaticMeshActor, location, rotation
    )
    if actor is None:
        unreal.log_error(f"Failed to spawn actor '{name}' -- spawn_actor_from_class returned None")
        return None

    actor.set_actor_label(name)
    mesh_component = actor.static_mesh_component
    cube_mesh = unreal.EditorAssetLibrary.load_asset(CUBE_MESH_PATH)
    if cube_mesh is None:
        unreal.log_error(f"Could not load {CUBE_MESH_PATH} -- is this a standard Unreal project with Engine content visible?")
        return actor
    mesh_component.set_static_mesh(cube_mesh)
    actor.set_actor_scale3d(scale)
    return actor


def _wall_segment(name, center_x, center_y, length, is_x_aligned, origin=ORIGIN):
    """A single solid wall segment (no doorway gap). The cube's local
    X axis always carries `length` and local Y carries `thickness`;
    for a north-south wall (is_x_aligned=False) a 90-degree yaw is
    what actually reorients that local X extent to run along world Y,
    not a different scale."""
    location = unreal.Vector(origin.x + center_x, origin.y + center_y, origin.z + WALL_HEIGHT / 2.0)
    rotation = unreal.Rotator(0.0, 0.0, 0.0 if is_x_aligned else 90.0)
    scale = unreal.Vector(length / 100.0, WALL_THICKNESS / 100.0, WALL_HEIGHT / 100.0)
    return _spawn_cube(name, location, rotation, scale)


def _wall_with_doorway(name_prefix, center_x, center_y, length, is_x_aligned,
                        door_width, door_height, origin=ORIGIN):
    """A wall split into two segments either side of a centered doorway
    gap, plus a lintel piece filling the wall above the opening."""
    side_length = (length - door_width) / 2.0
    half_total = length / 2.0

    # Left/first segment
    offset = -half_total + side_length / 2.0
    if is_x_aligned:
        loc1 = unreal.Vector(center_x + offset, center_y, 0.0)
    else:
        loc1 = unreal.Vector(center_x, center_y + offset, 0.0)
    _wall_segment(f"{name_prefix}_A", loc1.x, loc1.y, side_length, is_x_aligned, origin)

    # Right/second segment
    offset2 = half_total - side_length / 2.0
    if is_x_aligned:
        loc2 = unreal.Vector(center_x + offset2, center_y, 0.0)
    else:
        loc2 = unreal.Vector(center_x, center_y + offset2, 0.0)
    _wall_segment(f"{name_prefix}_B", loc2.x, loc2.y, side_length, is_x_aligned, origin)

    # Lintel: fills the wall from the top of the doorway up to the ceiling,
    # spanning the doorway's width.
    lintel_height = WALL_HEIGHT - door_height
    if lintel_height > 0.0:
        lintel_location = unreal.Vector(
            origin.x + center_x,
            origin.y + center_y,
            origin.z + door_height + lintel_height / 2.0,
        )
        rotation = unreal.Rotator(0.0, 0.0, 0.0 if is_x_aligned else 90.0)
        scale = unreal.Vector(door_width / 100.0, WALL_THICKNESS / 100.0, lintel_height / 100.0)
        _spawn_cube(f"{name_prefix}_Lintel", lintel_location, rotation, scale)


def _floor(name, center_x, center_y, size_x, size_y, origin=ORIGIN):
    location = unreal.Vector(origin.x + center_x, origin.y + center_y, origin.z)
    rotation = unreal.Rotator(0.0, 0.0, 0.0)
    scale = unreal.Vector(size_x / 100.0, size_y / 100.0, WALL_THICKNESS / 100.0 / 2.0)
    return _spawn_cube(name, location, rotation, scale)


def build_clinic_blockout():
    op_w, op_d = OP_ROOM_SIZE
    rec_w, rec_d = RECOVERY_ROOM_SIZE

    unreal.log("[build_clinic_blockout] Building operating room...")

    # --- Operating room floor ---
    _floor("Clinic_OpRoom_Floor", op_w / 2.0, op_d / 2.0, op_w, op_d)

    # --- Operating room walls (3 solid outer walls; the 4th, shared
    # with the recovery room, gets the doorway) ---
    _wall_segment("Clinic_OpRoom_Wall_West", 0.0, op_d / 2.0, op_d, is_x_aligned=False)
    _wall_segment("Clinic_OpRoom_Wall_North", op_w / 2.0, op_d, op_w, is_x_aligned=True)
    _wall_segment("Clinic_OpRoom_Wall_South", op_w / 2.0, 0.0, op_w, is_x_aligned=True)

    unreal.log("[build_clinic_blockout] Building recovery room...")

    recovery_origin = unreal.Vector(ORIGIN.x + op_w, ORIGIN.y, ORIGIN.z)

    # --- Recovery room floor ---
    _floor("Clinic_RecoveryRoom_Floor", rec_w / 2.0, rec_d / 2.0, rec_w, rec_d, origin=recovery_origin)

    # --- Recovery room's 3 solid outer walls ---
    _wall_segment("Clinic_RecoveryRoom_Wall_East", rec_w, rec_d / 2.0, rec_d, is_x_aligned=False, origin=recovery_origin)
    _wall_segment("Clinic_RecoveryRoom_Wall_North", rec_w / 2.0, rec_d, rec_w, is_x_aligned=True, origin=recovery_origin)
    _wall_segment("Clinic_RecoveryRoom_Wall_South", rec_w / 2.0, 0.0, rec_w, is_x_aligned=True, origin=recovery_origin)

    # --- Shared wall between the two rooms, with a doorway ---
    unreal.log("[build_clinic_blockout] Building the shared wall + doorway...")
    shared_wall_y = max(op_d, rec_d) / 2.0
    _wall_with_doorway(
        "Clinic_SharedWall",
        center_x=op_w,
        center_y=shared_wall_y,
        length=max(op_d, rec_d),
        is_x_aligned=False,
        door_width=DOORWAY_WIDTH,
        door_height=DOORWAY_HEIGHT,
    )

    unreal.log("[build_clinic_blockout] Done. Spawned operating room + recovery room blockout with a connecting doorway.")
    unreal.log("[build_clinic_blockout] Next: dress with actual medical props/furniture once sourced (see ASSET_SOURCING.md), or re-skin these blockout walls with a proper wall material.")


if __name__ == "__main__":
    build_clinic_blockout()
