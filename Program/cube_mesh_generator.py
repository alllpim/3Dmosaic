from copy import copy
from os import path

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from stl import Mesh

CUBE_VERTICES = np.array((
    (0, 0, 0),
    (1, 0, 0),
    (1, 1, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 0, 1),
    (1, 1, 1),
    (0, 1, 1)
))

CUBE_FACES = (
    (0, 3, 1),
    (1, 3, 2),
    (0, 4, 7),
    (0, 7, 3),
    (4, 5, 6),
    (4, 6, 7),
    (5, 1, 2),
    (5, 2, 6),
    (2, 3, 6),
    (3, 7, 6),
    (0, 1, 5),
    (0, 5, 4)
)


def create_cube_mesh(mutliplier: int | tuple[int, int, int] = 1,
                     offset: int | tuple[int, int, int] = 0) -> Mesh:
    if isinstance(mutliplier, int):
        mutliplier = (mutliplier, mutliplier, mutliplier)
    elif isinstance(mutliplier, tuple) and len(mutliplier) == 3:
        pass
    else:
        raise ValueError("Argument 'mutliplier' must be int or tuple[int, int, int]")

    if isinstance(offset, int):
        offset = (offset, offset, offset)
    elif isinstance(offset, tuple) and len(offset) == 3:
        pass
    else:
        raise ValueError("Argument 'offset' must be int or tuple[int, int, int]")

    cube_mesh = Mesh(np.zeros(len(CUBE_FACES), dtype=Mesh.dtype))
    for i, face in enumerate(CUBE_FACES):
        for j in range(3):
            vertex = copy(CUBE_VERTICES[face[j], :])

            for k in range(3):
                vertex[k] *= mutliplier[k]
                vertex[k] += offset[k]

            cube_mesh.vectors[i][j] = vertex

    return cube_mesh


def create_cube_array(multiplier: int | tuple[int, int, int] = 1, offset: int | tuple[int, int, int] = 0,
                      count_by_axis: tuple[int, int, int] = (1, 1, 1), max_count: int | None = None) -> Mesh:
    if isinstance(offset, int):
        offset = (offset, offset, offset)
    elif isinstance(offset, tuple) and len(offset) == 3:
        pass
    else:
        raise ValueError("Argument 'offset' must be int or tuple[int, int, int]")

    if not isinstance(count_by_axis, tuple) or len(count_by_axis) != 3:
        raise ValueError("Argument 'count_by_axis' must be tuple[int, int, int]")

    cube_meshes = []
    count = 0
    for x in range(count_by_axis[0]):
        for y in range(count_by_axis[1]):
            for z in range(count_by_axis[2]):
                cube_meshes.append(create_cube_mesh(multiplier, (offset[0] * x, offset[1] * y, offset[2] * z)).data)
                count += 1
                if count == max_count:
                    break
            if count == max_count:
                break
        if count == max_count:
            break

    return Mesh(np.concatenate(cube_meshes))


def create_many_cube_arrays(counts: list[int], multiplier: int | tuple[int, int, int] = 1,
                            offset: int | tuple[int, int, int] = 0,
                            count_by_axis: tuple[int, int, int] = (1, 1, 1)) -> list[list[Mesh]]:
    count_of_all = count_by_axis[0] * count_by_axis[1] * count_by_axis[2]
    meshes = []
    for count in counts:
        single_count_meshes = []
        single_count = count
        while single_count > 0:
            single_count_meshes.append(create_cube_array(multiplier, offset, count_by_axis, single_count))
            single_count -= count_of_all
        meshes.append(single_count_meshes)
    return meshes


def save_meshes(meshes: list[list[Mesh]], filenames: list[str], folder: str = "meshes") -> None:
    if len(meshes) != len(filenames):
        raise ValueError("Arguments 'meshes' and 'filenames' must be the same length")

    for list_of_meshes, filename in zip(meshes, filenames):
        if len(list_of_meshes) == 1:
            list_of_meshes[0].save(path.join(folder, filename + ".stl"))
        else:
            for index, mesh in enumerate(list_of_meshes):
                mesh.save(path.join(folder, filename + "_" + str(index + 1) + ".stl"))


def show_mesh(mesh: Mesh) -> None:
    figure = plt.figure()
    ax = figure.add_subplot(projection="3D")
    ax.add_collection3d(Poly3DCollection(mesh.vectors))
    scale = mesh.points.flatten()
    ax.auto_scale_xyz(scale, scale, scale)
    plt.show()


if __name__ == "__main__":
    pass

    # mesh = create_cube_mesh(5)
    # mesh.save("cube.stl")
    # combined = create_cube_array((10, 10, 5), offset=15, count_by_axis=(1, 2, 4), max_count=5)
    # combined.save("cube.stl")
    # show_mesh(Mesh.from_file("cube"))
    #
    # meshes = create_many_cube_arrays([43, 56, 12, 88, 66], multiplier=5, offset=6, count_by_axis=(8, 8, 1))
    # save_meshes(meshes, ["43", "56", "12", "88", "66"])
    #
    # show_mesh(Mesh.from_file("meshes_output/66_2.stl"))
