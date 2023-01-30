"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.
 
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.
 
    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time
    
   
def preparation_time_in_minutes(number_of_layers):
    
    """Calculate preparation_time_in_minutes.
 
    :param number_of_layers: int - number_of_layers already elapsed.
    :return: int - total preperation time by multilying number of layers and preperation         time.
 
    Function that takes the number of layers of lasagna as
    an argument and returns total preperation time based on number of layers and preperation time for each layer.
    """
    return number_of_layers * PREPARATION_TIME
    
def elapsed_time_in_minutes(number_of_layers,elapsed_bake_time):
    """Calculate elapsed_time_in_minutes.
 
    :param number_of_layers: int - number_of_layers already elapsed.
    :elapsed_bake_time: int - elapsed_bake_time already elapsed.
    
    :return: int - total elapsed time in minutes
 
    Function that takes the number of layers of lasagna , elapsed_bake_time as
    an argument and returns elapsed_time_in_minutes.
    """
    return number_of_layers * PREPARATION_TIME + elapsed_bake_time