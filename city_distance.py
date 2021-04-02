from math import radians, sin, cos, acos
import numpy as np
import traceback

class City_distance:
    def distance_calc(self):
        """
        input variables
        city1
        location of city 1
        location of city 2

        Purpose of the class:
        To calculate distance between two cities

        """

        city1 = input('City 1:').strip()
        city2 = input('City 2:').strip()
        try:
            lat1,lon1 = city1.split(',')
            lat2,lon2 = city2.split(',')
            lat1 = float(lat1[0:-1])
            lon1 = float(lon1[0:-1])
            lat2 = float(lat2[0:-1])
            lon2 = float(lon2[0:-1])
            r = 6371.01
            phi1 = np.radians(lat1)
            phi2 = np.radians(lat2)
            delta_phi = np.radians(lat2 - lat1)
            delta_lambda = np.radians(lon2 - lon1)
            a = np.sin(delta_phi / 2) ** 2 + np.cos(phi1) * np.cos(phi2) * np.sin(delta_lambda / 2) ** 2
            res = r * (2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a)))
            del lat2,lon1,lon2,r,phi1,phi2,delta_lambda,delta_phi,city2,city1,lat1
            print("City1 and City2 are " +str(np.round(res,2))+ " km apart")
        except Exception as e:
            traceback.print_exc()
            print(e)
distance = City_distance()
distance.distance_calc()
