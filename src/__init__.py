# adding the line below allows main.py to import "gamma"
# directly from ".", without the need to write or know that
# gamma is part of "tony":
from .tony import gamma, beta

# this can bubble up relevant files in deep hierarchies:
from .tony.wanda.natasha.bruce import delta
