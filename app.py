# we outsourced the factory to the api folder and now we import it here as a package
from api import create_app
app = create_app
