from engine import *
# from planet import *
from celestial_object import *
from global_variables import *


# Pygame init
ENGINE = Engine(1000,[900,900])
ENGINE.start_pygame("lines")
# arrows = Three_Axys_Arrows()

# Tuple Color of Moon
moon_gray_white = (0.863, 0.863, 0.863)

sun       = Star(RADIUS_MAP(SUN_DIAMETER),(1,1,0))                     #star
mercury   = Planet(RADIUS_MAP(MERCURY_DIAMETER),(0.741, 0.718, 0.420)) #planet
venus     = Planet(RADIUS_MAP(VENUS_DIAMETER),(1.000, 0.843, 0.000))   #planet

earth     = Planet(RADIUS_MAP(EARTH_DIAMETER), (0.000, 0.000, 0.545))  #planet
moon      = Moon(RADIUS_MAP(MOON_DIAMETER), moon_gray_white)           #moon

mars      =  Planet(RADIUS_MAP(MARS_DIAMETER),(1.000, 0.271, 0.000))   #planet
fobos     =  Moon(RADIUS_MAP(FOBOS_DIAMETER),moon_gray_white)          #moon
deimos    =  Moon(RADIUS_MAP(DEIMOS_DIAMETER),(1.000, 0.498, 0.314))   #moon

jupiter   = Planet(RADIUS_MAP(JUPITER_DIAMETER),(1.000, 0.627, 0.478)) #planet
europa    = Moon( RADIUS_MAP(EUROPA_DIAMETER),(0.941, 0.902, 0.549))   #moon
ganimedes = Moon( RADIUS_MAP(GANIMEDES_DIAMETER),moon_gray_white)      #moon
io        = Moon( RADIUS_MAP(IO_DIAMETER),(0.855, 0.647, 0.125))       #moon
calisto   = Moon( RADIUS_MAP(CALISTO_DIAMETER),moon_gray_white)        #moon

saturn  = Planet(RADIUS_MAP(SATURN_DIAMETER ),(1.000, 0.871, 0.678))   #planet
reia    = Moon( RADIUS_MAP(REIA_DIAMETER),moon_gray_white)             #moon
tita    = Moon( RADIUS_MAP(TITA_DIAMETER),(0.941, 0.902, 0.549))       #moon
japeto  = Moon( RADIUS_MAP(JAPETO_DIAMETER),moon_gray_white)           #moon


uranus  = Planet(RADIUS_MAP(URANUS_DIAMETER ),(0.686, 0.933, 0.933))   #planet
umbriel = Moon(RADIUS_MAP(UMBRIEL_DIAMETER),moon_gray_white)           #moon
titania = Moon(RADIUS_MAP(TITA_DIAMETER),moon_gray_white)              #moon
oberon  = Moon(RADIUS_MAP(OBERON_DIAMETER),moon_gray_white)            #moon

neptune = Planet(RADIUS_MAP(NEPTUNE_DIAMETER), (0.255, 0.412, 0.882))  #planet
tritao  = Moon( RADIUS_MAP(TRITAO_DIAMETER),(1.000, 0.871, 0.678))     #moon
proteu  = Moon( RADIUS_MAP(PROTEU_DIAMETER),moon_gray_white)           #moon
nereida = Moon( RADIUS_MAP(NEREIDA_DIAMETER),moon_gray_white)          #moon

# Sedna    = Planet(RADIUS_MAP(MOON_DIAMETER),(0.502, 0.000, 0.000))   #dwarf-planet

sun_earth_distance   = sun.radius + earth.radius   + DISTANCE_MAP(EARTH_DISTANCE)
sun_mercury_distance = sun.radius + mercury.radius + DISTANCE_MAP(MERCURY_DISTANCE)
sun_venus_distance   = sun.radius + venus.radius   + DISTANCE_MAP(VENUS_DISTANCE)
sun_mars_distance    = sun.radius + mars.radius    + DISTANCE_MAP(MARS_DISTANCE)
sun_jupiter_distance = sun.radius + jupiter.radius + DISTANCE_MAP(JUPITER_DISTANCE)
sun_saturn_distance  = sun.radius + saturn.radius  + DISTANCE_MAP(SATURN_DISTANCE)
sun_uranus_distance  = sun.radius + uranus.radius  + DISTANCE_MAP(URANUS_DISTANCE)
sun_neptune_distance = sun.radius + neptune.radius + DISTANCE_MAP(NEPTUNE_DISTANCE)


#terra
earth_moon_distance  =  earth.radius+moon.radius+MOON_DISTANCE+0.2

#marte
marte_fobos_distance  = earth.radius+fobos.radius+FOBOS_DISTANCE
marte_deimos_distance = mars.radius+deimos.radius+DEIMOS_DIAMETER+0.5

# jupiter
jupiter_europa_distance    = jupiter.radius+europa.radius+EUROPA_DIAMETER
jupiter_ganimedes_distance = jupiter.radius+ganimedes.radius+GANIMEDES_DISTANCE+0.5
jupiter_io_distance        = jupiter.radius+io.radius+IO_DISTANCE+1.0
jupiter_calisto_distance   = jupiter.radius+calisto.radius+CALISTO_DIAMETER+1.5

# saturn
saturn_reia_distance   = saturn.radius+reia.radius+REIA_DISTANCE
saturn_tita_distance   = saturn.radius+tita.radius+TITA_DISTANCE+0.5
saturn_japeto_distance = saturn.radius+japeto.radius+JAPETO_DISTANCE+1.0

# uranus
uranus_umbriel_distance  = uranus.radius+umbriel.radius+UMBRIEL_DISTANCE
uranus_titania_distance  = uranus.radius+titania.radius+TITANIA_DISTANCE+0.5
uranus_oberon_distance   = uranus.radius+oberon.radius+OBERON_DISTANCE+1.0

# neptune
netune_tritao_distance   = neptune.radius+tritao.radius+TRITAO_DISTANCE
neptune_proteu_distance  = neptune.radius+proteu.radius+PROTEU_DISTANCE+0.5
neptune_nereida_distance = neptune.radius+nereida.radius+NEREIDA_DISTANCE+1.0



mercury.sun_revolution(sun_mercury_distance,Mercury_orbital_period,Mercury_eccentricity,VELOCITY_MAP(MERCURY_DISTANCE))
venus.sun_revolution(sun_venus_distance,Venus_orbital_period,Venus_eccentricity,VELOCITY_MAP(VENUS_DISTANCE))
mercury.sun_revolution(sun_mercury_distance,Mercury_orbital_period,Mercury_eccentricity,VELOCITY_MAP(MERCURY_DISTANCE))
venus.sun_revolution(sun_venus_distance,Venus_orbital_period,Venus_eccentricity,VELOCITY_MAP(VENUS_DISTANCE))
earth.sun_revolution(sun_earth_distance,1.0,0.02,VELOCITY_MAP(EARTH_DISTANCE))
mars.sun_revolution(sun_mars_distance,Mars_orbital_period,Mars_eccentricity,VELOCITY_MAP(MARS_DISTANCE))
jupiter.sun_revolution(sun_jupiter_distance,Jupiter_orbital_period,Jupiter_eccentricity,VELOCITY_MAP(JUPITER_DISTANCE))
saturn.sun_revolution(sun_saturn_distance,Saturn_orbital_period,Saturn_eccentricity,VELOCITY_MAP(SATURN_DISTANCE))
uranus.sun_revolution(sun_uranus_distance,Uranus_orbital_period,Uranus_eccentricity,VELOCITY_MAP(URANUS_DISTANCE))
neptune.sun_revolution(sun_neptune_distance,Neptune_orbital_period,Neptune_eccentricity,VELOCITY_MAP(NEPTUNE_DISTANCE))

# Sedna.sun_revolution(0,10505,0.84123,500)

moon.moon_revolution(earth.orbit_list,earth_moon_distance,VELOCITY_MAP(MOON_VELOCITY))
fobos.moon_revolution(mars.orbit_list,marte_fobos_distance,  VELOCITY_MAP(MOON_VELOCITY))
deimos.moon_revolution(mars.orbit_list,marte_deimos_distance,VELOCITY_MAP(MOON_VELOCITY)+20)
europa.moon_revolution(jupiter.orbit_list,jupiter_europa_distance,VELOCITY_MAP(MOON_VELOCITY))
ganimedes.moon_revolution(jupiter.orbit_list,jupiter_ganimedes_distance,VELOCITY_MAP(MOON_VELOCITY)+20)
io.moon_revolution(jupiter.orbit_list,jupiter_io_distance,VELOCITY_MAP(MOON_VELOCITY)+25)
calisto.moon_revolution(jupiter.orbit_list,jupiter_calisto_distance,VELOCITY_MAP(MOON_VELOCITY)+30)
reia.moon_revolution(saturn.orbit_list,saturn_reia_distance,VELOCITY_MAP(MOON_VELOCITY))
tita.moon_revolution(saturn.orbit_list,saturn_tita_distance,VELOCITY_MAP(MOON_VELOCITY)+20)
japeto.moon_revolution(saturn.orbit_list,saturn_japeto_distance,VELOCITY_MAP(MOON_VELOCITY)+30)

umbriel.moon_revolution(uranus.orbit_list,uranus_umbriel_distance,VELOCITY_MAP(MOON_VELOCITY))
titania.moon_revolution(uranus.orbit_list,uranus_titania_distance,VELOCITY_MAP(MOON_VELOCITY)+20)
oberon.moon_revolution(uranus.orbit_list,uranus_oberon_distance,VELOCITY_MAP(MOON_VELOCITY)+30)

tritao.moon_revolution(neptune.orbit_list,netune_tritao_distance,VELOCITY_MAP(MOON_VELOCITY))
proteu.moon_revolution(neptune.orbit_list,neptune_proteu_distance,VELOCITY_MAP(MOON_VELOCITY)+20)
nereida.moon_revolution(neptune.orbit_list,neptune_nereida_distance,VELOCITY_MAP(MOON_VELOCITY)+30)


if __name__ == "__main__":

    while True:
        ENGINE.user_input()
        ENGINE.clear_buffer()
        # arrows.draw()


        sun.draw()
        # mercury.draw_ringAll()
        # venus.draw_ringAll()
        # earth.draw_ringAll()
        # mars.draw_ringAll()
        # jupiter.draw_ringAll()
        # saturn.draw_ringAll()
        # uranus.draw_ringAll()
        # neptune.draw_ringAll()

        mercury.revolution_animate()   # planet
        venus.revolution_animate()     # planet
        earth.revolution_animate()     # planet
        moon.revolution_animate()      # moon
        mars.revolution_animate()      # planet
        fobos.revolution_animate()     # moon
        deimos.revolution_animate()    # moon

        jupiter.revolution_animate()   # planet
        europa.revolution_animate()    # moon
        ganimedes.revolution_animate() # moon
        io.revolution_animate()        # moon
        calisto.revolution_animate()   # moon

        saturn.revolution_animate()    # planet
        reia.revolution_animate()      # moon
        tita.revolution_animate()      # moon
        japeto.revolution_animate()    # moon

        uranus.revolution_animate()    # planet
        umbriel.revolution_animate()   # moon
        titania.revolution_animate()   # moon
        oberon.revolution_animate()    # moon

        neptune.revolution_animate()   # planet
        tritao.revolution_animate()    # moon
        proteu.revolution_animate()    # moon
        nereida.revolution_animate()   # moon

        # glTranslate(0.0, 0.0, self.zoom_factor)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    glTranslate(0.0, 0.0, 50)

        ENGINE.flip_and_clock(10)

