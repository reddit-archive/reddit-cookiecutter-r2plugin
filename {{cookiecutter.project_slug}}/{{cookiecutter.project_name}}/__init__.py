from pylons.i18n import N_

from r2.lib.configparse import ConfigValue
{%- if cookiecutter.has_static_assets == "yes" %}
from r2.lib.js import LocalizedModule
{%- endif %}
from r2.lib.plugin import Plugin


class {{ cookiecutter.plugin_name }}(Plugin):
    {% if cookiecutter.has_static_assets == "yes" -%}
    needs_static_build = True

    js = {
        "{{ cookiecutter.project_slug }}": LocalizedModule("{{ cookiecutter.project_slug }}.js",
            # TODO: your javascript files go here, e.g.:
            # "{{ cookiecutter.project_slug }}/something.js",
        ),
    }
    {%- else -%}
    needs_static_build = False
    {%- endif %}

    config = {
        # TODO: your static configuratation options go here, e.g.:
        # ConfigValue.int: [
        #     "{{ cookiecutter.project_slug }}_blargs",
        # ],
    }

    live_config = {
        # TODO: your live configuratation options go here, e.g.:
        # ConfigValue.int: [
        #     "{{ cookiecutter.project_slug }}_realtime_blargs",
        # ],
    }

    errors = {
        # TODO: your API errors go here, e.g.:
        # "{{ cookiecutter.project_slug | upper }}_NOT_COOL": N_("not cool"),
    }

    def add_routes(self, mc):
        # TODO: register your routes here, e.g.:
        #
        # mc("/myplugin", controller="{{ cookiecutter.project_slug }}", action="something")
        pass

    def load_controllers(self):
        # TODO: import any other controllers you define here
        from {{ cookiecutter.project_name }}.controllers import (
            {{ cookiecutter.plugin_name }}Controller,
        )

        # TODO: register any hooks you define in your modules here, e.g.:
        #
        # from {{ cookiecutter.project_name }} import some_module
        # some_module.hooks.register_all()

    def declare_queues(self, queues):
        # TODO: add any queues / bindings you need here, e.g.:
        #
        # queues.some_queue_defined_elsewhere << "routing_key"
        #
        # or
        #
        # from r2.config.queues import MessageQueue
        # queues.declare({
        #     "some_q": MessageQueue(),
        # })
        pass
