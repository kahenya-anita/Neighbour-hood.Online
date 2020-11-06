# (Step : 1) ==== import models === #
from NBHapp.models import *


# (Step : 2) ==== Returns all neighbourhoods from neighbourhood table === #
>>> neighbourhoods = Neighbourhood.objects.all()
>>> print(neighbourhoods)
<QuerySet [<Neighbourhood: Gathongi Estate>, <Neighbourhood: Ramai Estate>, <Neighbourhood: Ridge Estate>]>

# (Step : 3) ==== Get the first neighbourhood === #
firstNeighbourhood = Neighbourhood.object.first()
>>> print(neighbourhoods.first())
# Name of Neighbourhood

# (Step : 4) ==== Get the last neighbourhood === #
lastNeighbourhood = Neighbourhood.object.last()
>>> print(neighbourhoods.last())
# Name of Neighbourhood

# (Step : 5) ==== Return Single Neighbourhoods by name === #
>>> neighbourhood1 = Neighbourhood.objects.get(name="Gathongi Estate")
>>> print(neighbourhood1)
# Name of Neighbourhood

# (Step : 6) ==== Access each attribute === #
print(neighbourhood1.location)
# Location
print(neighbourhood1.id)
# ID
print(neighbourhood1.population)
# Population