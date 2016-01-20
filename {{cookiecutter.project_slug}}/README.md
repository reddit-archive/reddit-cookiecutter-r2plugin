# {{ cookiecutter.project_slug }}

{{ cookiecutter.project_description }}

## Installation

Install the plugin itself.

```bash
cd ~/src/{{ cookiecutter.project_slug }}
python setup.py build
sudo python setup.py develop
```

Then add the plugin to your ini file:

```diff
############################################ PLUGINS
# which plugins are enabled (they must be installed via setup.py first)
-plugins = about, liveupdate
+plugins = about, liveupdate, {{ cookiecutter.project_slug }}
```
