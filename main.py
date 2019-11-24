from engine import *
# from planet import *
from celestial_object import *
from global_variables import *

ENGINE = Engine(1000,[900,900])
ENGINE.start_pygame("lines")
arrows = Three_Axys_Arrows()

# sun = CelestialObject(5,0)
# sun.spawnMoons(5)


sun     = Star(0,0,0,RADIUS_MAP(SUN_RADIUS))
mercury = Planet(0,0,0,RADIUS_MAP(MERCURY_RADIUS))
venus   = Planet(0,0,0,RADIUS_MAP(VENUS_RADIUS))
earth   = Planet(0,0,0,RADIUS_MAP(EARTH_RADIUS))
moon    = Planet(0,0,0, RADIUS_MAP(MOON_RADIUS))
mars    = Planet(0,0,0,RADIUS_MAP(MARS_RADIUS))
jupiter = Planet(0,0,0,RADIUS_MAP(JUPITER_RADIUS))
saturn  = Planet(0,0,0,RADIUS_MAP(SATURN_RADIUS ))
uranus  = Planet(0,0,0,RADIUS_MAP(URANUS_RADIUS ))
neptune = Planet(0,0,0,RADIUS_MAP(NEPTUNE_RADIUS))



mercury.sun_revolution(sun.x,sun.y,DISTANCE_MAP(MERCURY_DISTANCE)+sun.radius+mercury.radius,VELOCITY_MAP(MERCURY_VELOCITY))
venus.sun_revolution(sun.x,sun.y,DISTANCE_MAP(VENUS_DISTANCE)+sun.radius+venus.radius,VELOCITY_MAP(VENUS_VELOCITY))
earth.sun_revolution(sun.x,sun.y,DISTANCE_MAP(EARTH_DISTANCE)+sun.radius+earth.radius,VELOCITY_MAP(EARTH_VELOCITY))
moon.moon_revolution(earth.vertices_list,0.2+MOON_DISTANCE+earth.radius+moon.radius,VELOCITY_MAP(MOON_VELOCITY))
mars.sun_revolution(sun.x,sun.y,DISTANCE_MAP(MARS_DISTANCE)+sun.radius+mars.radius,VELOCITY_MAP(MARS_VELOCITY))
jupiter.sun_revolution(sun.x,sun.y,DISTANCE_MAP(JUPITER_DISTANCE)+sun.radius+jupiter.radius,VELOCITY_MAP(JUPITER_VELOCITY))
saturn.sun_revolution(sun.x,sun.y,DISTANCE_MAP(SATURN_DISTANCE)+sun.radius+saturn.radius,VELOCITY_MAP(SATURN_VELOCITY))
uranus.sun_revolution(sun.x,sun.y,DISTANCE_MAP(URANUS_DISTANCE)+sun.radius+uranus.radius,VELOCITY_MAP(URANUS_VELOCITY))
neptune.sun_revolution(sun.x,sun.y,DISTANCE_MAP(NEPTUNE_DISTANCE)+sun.radius+neptune.radius,VELOCITY_MAP(NEPTUNE_VELOCITY))


if __name__ == "__main__":

    while True:
        ENGINE.user_input('zoom')
        ENGINE.clear_buffer()
        arrows.draw()

        arrows.draw()
        sun.draw()
        mercury.revolution_animate()
        venus.revolution_animate()
        earth.revolution_animate()
        moon.revolution_animate()
        mars.revolution_animate()
        jupiter.revolution_animate()
        saturn.revolution_animate()
        uranus.revolution_animate()
        neptune.revolution_animate()

        ENGINE.flip_and_clock(10)

