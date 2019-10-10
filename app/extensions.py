from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from playhouse.flask_utils import FlaskDB
from micawber.cache import Cache as OEmbedCache
from micawber import bootstrap_basic

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()

# FlaskDB is a wrapper for a peewee database that sets up pre/post-request
# hooks for managing database connections.
flask_db = FlaskDB()

# The `database` is the actual peewee database, as opposed to flask_db which is
# the wrapper.

# Configure micawber with the default OEmbed providers (YouTube, Flickr, etc).
# We'll use a simple in-memory cache so that multiple requests for the same
# video don't require multiple network requests.
oembed_providers = bootstrap_basic(OEmbedCache())
