class Physics:
    @staticmethod
    def box_collider2d_circle_collider_intersects(box_collider2d, circle_collider):
        if box_collider2d is None:
            return False
        if circle_collider is None:
            return False

        is_right = (circle_collider.center.x - circle_collider.radius) - (box_collider2d.center.x + box_collider2d.size.x / 2) > 0
        is_left = (circle_collider.center.x + circle_collider.radius) - (box_collider2d.center.x - box_collider2d.size.x / 2) < 0

        if is_left or is_right:
            return False

        is_up = (circle_collider.center.y + circle_collider.radius) - (box_collider2d.center.y - box_collider2d.size.y / 2) < 0
        is_down = (circle_collider.center.y - circle_collider.radius) - (box_collider2d.center.y + box_collider2d.size.y / 2) > 0

        if is_up or is_down:
            return False

        return True


class BoxCollider2D:

     def __init__(self, center, size):
        self.center = center
        self.size = size


class CircleCollider:

    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
