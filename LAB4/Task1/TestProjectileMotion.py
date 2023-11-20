from ProjectileMotion import ProjectileMotion


free_speed = ProjectileMotion.FreeMovement(50).speed()
limited_speed = ProjectileMotion.LimitedMovement(50, 30).speed()
print("Швидкість каменю без опору повітря:", free_speed, "м/с")
print("Швидкість каменю з опором повітря:", limited_speed, "м/с")
