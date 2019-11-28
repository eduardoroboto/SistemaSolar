from shapes import *
from math import *

# Everything is in km
# SUN_DIAMETER     = 109

#Estrela
# SUN_DIAMETER     = 109.17
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
semimajor_axis_Pluto = 39.4821

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
Pluto_eccentricity = 0.25



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
OBERON_DIAMETER    = 0.119510
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

# #marte
# FOBOS_VELOCITY = 0
# DEIMOS_VELOCITY = 0
# # jupiter
# EUROPA_VELOCITY = 0
# GANIMEDES_VELOCITY = 0
# IO_VELOCITY = 0
# CALISTO_VELOCITY = 0
# # saturn
# REIA_VELOCITY = 0
# TITA_VELOCITY = 0
# JAPETO_VELOCITY = 0
# # uranus
# UMBRIEL_VELOCITY = 0
# TITANIA_VELOCITY = 0
# OBERON_VELOCITY = 0
# # neptune
# TRITAO_VELOCITY = 0
# PROTEU_VELOCITY = 0
# NEREIDA_VELOCITY = 0


#terra
#marte
# MERCURY_COLOR=
# VENUS_COLOR=
# EARTH_COLOR=
# MOON_COLOR=
# MARS_COLOR=
# JUPITER_COLOR=
# SATURN_COLOR=
# URANUS_COLOR=
# NEPTUNE_COLOR=


# 0.241 	0.615 	1 	1.88 	11.9 	29.4 	83.7 	163.7 	247.9
#
# 5906376272
# 9999999999
def RADIUS_MAP(DIAMETER):
    return (DIAMETER/2)
    # return MAP(DIAMETER,PLUTO_DIAMETER,JUPITER_DIAMETER,0,5)

def DISTANCE_MAP(distance):
    return distance*12
    # return MAP(distance,0,PLUTO_DISTANCE,0,20)

# 147.1


def VELOCITY_MAP(velocity):
    return round(MAP(round(velocity*100*pi),0,1000,1,360*5))


def keplerIII_period_to_semimajor_axis(orbital_period):
    #########################################################
    # Units: orbital period [yr], separation [au]           #
    #########################################################
    semimajor_axis_cubed = orbital_period ** 2
    semimajor_axis = semimajor_axis_cubed ** (1. / 3.)

    return semimajor_axis


def make_kepler_orbit(eccentricity, orbital_period,nStep):
    ##########################################################
    # Units: orbital period [years]                          #
    # returns: 500 true anomaly values throughout the orbit  #
    ##########################################################
    # nStep = 500
    # tRange = np.linspace(0.0, orbital_period, nStep)
    lower = 0.0
    upper = orbital_period
    length = nStep
    # [lower + x * (upper - lower) / (length - 1) for x in range(length)]
    # [lower + x * (upper - lower) / length for x in range(length)]
    tRange = [lower + x * (upper - lower) / (length - 1) for x in range(length)]


    theta = []
    for time in tRange:
        PsiDiff = 1.0
        M = 2 * pi * time / orbital_period
        PsiOld = M
        theta0old = 180.0
        while PsiDiff > 1e-10:
            PsiNew = M + eccentricity * sin(PsiOld)
            PsiDiff = PsiNew - PsiOld
            PsiOld = PsiNew
        theta0 = 2 * atan(((1 + eccentricity) / (1 - eccentricity)) ** (0.5) * tan(PsiOld / 2.))
        theta.append(theta0)
    return theta

# list1 = make_kepler_orbit(eccentricity,orbital_period)

def orbit(radius,semimajor_axis, eccentricity, true_anomaly_list):
    ##############################################
    # Units: separation [au] #
    ##############################################
    x_orbit = []
    y_orbit = []
    # define the shape equation
    for true_anomaly in true_anomaly_list:
        r_orbit = semimajor_axis * (1 - eccentricity ** 2) / (1 + eccentricity * cos(true_anomaly))
        x_orbit.append(r_orbit * cos(true_anomaly))
        y_orbit.append(r_orbit * sin(true_anomaly))

    return x_orbit, y_orbit