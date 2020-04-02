class Ball:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Can't be negative, get {}".format(radius))
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    # @radius.setter
    # def radius(self, radius):
    #     self._radius = radius


    def __call__(self, x):
        return x *3.14

ball = Ball(1)
ball.radius
ball.radius = 2

z = Layer(init)(x)
z = Layer(init)(z)
z = Layer(init)(z)
