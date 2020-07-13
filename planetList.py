planet_list = ["Mercury", "Mars"]

planet_list.append("Jupiter")
planet_list.append("Saturn")
planet_list.extend(["Uranus", "Neptune"])
planet_list.insert(2, "Earth")
planet_list.insert(3, "Venus")
planet_list.append("Pluto")
rocky_planets = planet_list[0:4]
planet_list.__delitem__(-1)