class vector:
    def __init__(self, x, y, z):
        self.x_coord = x
        self.y_coord = y
        self.z_coord = z

    def __add__(self, another_vector):
        new_x = self.x_coord+another_vector.x_coord
        new_y = self.y_coord+another_vector.y_coord
        new_z = self.z_coord+another_vector.z_coord
        return vector(new_x, new_y, new_z)

    def dot_prod(self):
        return self.x_coord**2+self.y_coord**2+self.z_coord**2

    def __str__(self):
        return f"x: {self.x_coord}, y: {self.y_coord}, z: {self.z_coord}"

v1 = vector(1,2,1)
v2 = vector(2,1,4)
print(
    (v1+v2).dot_prod() #  LOOOL
    )
