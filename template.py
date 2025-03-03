# # This is an integer (int type)
# print(3, "is a", type(3))

# # This is a real number (float type)
# print(3.0, "is a", type(3.0))

# print(6.02e23, "is Avogadro's number")
# print(6.62607e-34, "is Planck's constant in Joule-seconds")

# # Convert int to float (generally no change to numerical value)
# print( "float(3) creates",float(3) )

# # Truncate float to int
# print( "int(3.14) creates", int(3.14) )

# print(0.2 - 0.1 == 0.1)    # as expected
# print(3.1 - 3.0 == 0.1)    # uh-oh

# import numpy as np # type: ignore
# print( np.isclose(3.1 - 3.0, 0.1) )

# import numpy as np
# print( "(np.inf + 5) is", np.inf + 5 )
# print( "(np.inf + np.inf) is", np.inf + np.inf )
# print( "(5 - np.inf) is", 5 - np.inf )

import numpy as np
np.datetime64("2020-01-17")    # YYYY-MM-DD 
np.datetime64("1969-07-20T20:17")    # YYYY-MM-DDThh:mm