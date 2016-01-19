from r2.controllers import add_controller
from r2.controllers.reddit_base import RedditController


@add_controller
class {{ cookiecutter.plugin_name }}Controller(RedditController):
    # TODO: your action methods go here!
    pass
