#  ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# ##### END GPL LICENSE BLOCK #####

import bpy
from bpy.types import PropertyGroup
from bpy.props import BoolProperty, IntProperty, FloatProperty, StringProperty, EnumProperty, PointerProperty


class RenderFarmServer_Props(PropertyGroup):
    serverRender: BoolProperty(
        name="Render on Server",
        description="Do rendering on server computer?",
        default=True
    )

    outPath: StringProperty(
        name="Output",
        description="Output directory",
        subtype="DIR_PATH"
    )


classes = (
    RenderFarmServer_Props,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.local_render_farm_server = PointerProperty(type=RenderFarmServer_Props)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.local_render_farm_server