# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import octoprint.plugin

class wledPlugin(octoprint.plugin.StartupPlugin,
                       octoprint.plugin.TemplatePlugin,
                       octoprint.plugin.SettingsPlugin,
                       octoprint.plugin.AssetPlugin):
    def on_after_startup(self):
        self._logger.info("WLed plugin started")

    def get_settings_defaults(self):
        return dict(url="http://wled-octo.home.intra")

    def get_template_configs(self):
        return [
            dict(type="navbar", custom_bindings=False),
            dict(type="settings", custom_bindings=False)
        ]

    def get_assets(self):
        return dict(
            js=["js/wled.js"]
        )

__plugin_name__ = "Wled"
__plugin_pythoncompat__ = ">=2.7,<4"
__plugin_implementation__ = wledPlugin()
