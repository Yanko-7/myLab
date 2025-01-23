from math import pi
import pygmsh

pygmsh.occ.Geometry().add_rectangle()
with pygmsh.geo.Geometry() as geom:
    poly = geom.add_polygon(
        [
            [+0.0, +0.5],
            [-0.1, +0.1],
            [-0.5, +0.0],
            [-0.1, -0.1],
            [+0.0, -0.5],
            [+0.1, -0.1],
            [+0.5, +0.0],
            [+0.1, +0.1],
        ],
        mesh_size=0.05,
    )

    geom.twist(
        poly,
        translation_axis=[0, 0, 1],
        rotation_axis=[0, 0, 1],
        point_on_axis=[0, 0, 0],
        angle=pi / 3,
    )

    mesh = geom.generate_mesh()
# 将网格保存为 VTK 格式
mesh.write('mesh.vtk')
