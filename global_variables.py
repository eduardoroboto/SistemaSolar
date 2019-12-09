from shapes import MAP
from math import pi


#Estrela
SUN_DIAMETER = 10

#Planetas
EARTH_DIAMETER   = 1
MERCURY_DIAMETER = 0.383
VENUS_DIAMETER   = 0.949
MOON_DIAMETER    = 0.2724
MARS_DIAMETER    = 0.532
JUPITER_DIAMETER = 11.21
SATURN_DIAMETER  = 9.45
URANUS_DIAMETER  = 4.01
NEPTUNE_DIAMETER = 3.88
# PLUTO_DIAMETER   = 0.186

EARTH_DISTANCE    = 1
MERCURY_DISTANCE  = 0.387
VENUS_DISTANCE    = 0.723
MARS_DISTANCE     = 1.52
JUPITER_DISTANCE  = 5.20
SATURN_DISTANCE   = 9.58
URANUS_DISTANCE   = 19.20
NEPTUNE_DISTANCE  = 30.05
# PLUTO_DISTANCE  = 39.48


semimajor_axis_Mercury = 0.3871
semimajor_axis_Venus = 0.7233
semimajor_axis_Earth = 1.0000
semimajor_axis_Mars = 1.5237
semimajor_axis_Jupiter = 5.2029
semimajor_axis_Saturn = 9.5370
semimajor_axis_Neptune = 19.1890
semimajor_axis_Uranus = 30.0699
# semimajor_axis_Pluto = 39.4821

Mercury_orbital_period = 0.48
Mercury_eccentricity = 0.21
Venus_orbital_period = 0.62
Venus_eccentricity = 0.01
Mars_orbital_period = 1.88
Mars_eccentricity = 0.09
Jupiter_orbital_period = 11.86
Jupiter_eccentricity = 0.05
Saturn_orbital_period = 29.46
Saturn_eccentricity = 0.05
Uranus_orbital_period = 84.02
Uranus_eccentricity = 0.05
Neptune_orbital_period = 164.8
Neptune_eccentricity = 0.01
Pluto_orbital_period = 248.0
# Pluto_eccentricity = 0.25



MERCURY_VELOCITY = 0.241
VENUS_VELOCITY   = 0.615
EARTH_VELOCITY   = 1
MARS_VELOCITY    = 1.88
JUPITER_VELOCITY = 11.9
SATURN_VELOCITY  = 29.4
URANUS_VELOCITY  = 83.7
NEPTUNE_VELOCITY = 163.7
# PLUTO_VELOCITY=247.9


# Satelites DIAMETER
#terra
MOON_DIAMETER      = 0.383
#marte
FOBOS_DIAMETER     = 0.000883
DEIMOS_DIAMETER    = 0.001768
# jupiter
EUROPA_DIAMETER    = 0.244985
GANIMEDES_DIAMETER = 0.413452
IO_DIAMETER        = 0.285921
CALISTO_DIAMETER   = 0.378324
# saturn
REIA_DIAMETER      = 0.119887
TITA_DIAMETER      = 0.404136
JAPETO_DIAMETER    = 0.115288
# uranus
UMBRIEL_DIAMETER   = 0.091775
TITANIA_DIAMETER   = 0.123748
OBERON_DIAMMercury_orbital_periodETER    = 0.119510
# neptune
TRITAO_DIAMETER    = 0.212431
PROTEU_DIAMETER    = 0.032962
NEREIDA_DIAMETER   = 0.026683


# Satelites DISTANCE
#terra
MOON_DISTANCE     = 0.00257
#marte
FOBOS_DISTANCE = 0.000063
DEIMOS_DISTANCE = 0.000156
# jupiter
EUROPA_DISTANCE = 0.004473
GANIMEDES_DISTANCE = 0.007136
IO_DISTANCE = 0.002819
CALISTO_DISTANCE = 0.012551
# saturn
REIA_DISTANCE = 0.003514
TITA_DISTANCE = 0.008146
JAPETO_DISTANCE = 0.023739
# uranus
UMBRIEL_DISTANCE = 0.001773
TITANIA_DISTANCE = 0.002906
OBERON_DISTANCE = 0.003890
# neptune
TRITAO_DISTANCE = 0.002365
PROTEU_DISTANCE = 0.000784
NEREIDA_DISTANCE = 0.03685


# Satelites
#terra
MOON_VELOCITY=   0.0748

def RADIUS_MAP(DIAMETER):
    """ Convert DIAMETER TO RADIUS"""
    return (DIAMETER/2)

def DISTANCE_MAP(distance):
    """ Scale distance AU to a number"""
    return distance*12

def VELOCITY_MAP(velocity):
    """Scale VELOCITY to a round number """
    return round(MAP(round(velocity*100*pi),0,1000,1,360*5))
