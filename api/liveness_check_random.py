import random

def liveness_check_random(selfie):
    '''
    dummy function for liveness check. The result is random (output 90% True, 10% False).
    Will be changed in the future.
    :param dummy variable selfie: the input selfie, type: numpy 2D array, but is not used
    :return: boolean value, indicating if the selfie is from real person or not.
    '''
    random_value = random.rand()
    if random_value < 0.9:
        return True
    else:
        return False