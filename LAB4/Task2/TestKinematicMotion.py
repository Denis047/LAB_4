from KinematicMotion import KinematicMotion

v0 = 20
k2 = 0.2

motion = KinematicMotion(v0, k2)
time_without_drag = motion.time_of_flight_without_drag()
time_with_drag = motion.time_of_flight_with_drag()

print(f"Час польоту без гальмівної сили: {time_without_drag} с")
print(f"Час польоту з гальмівною силою: {time_with_drag} с")

motion.plot_motion()
