"""Constants for the Eaton UPS Companion integration."""

from __future__ import annotations

from homeassistant.const import Platform

DOMAIN = "eaton_ups_companion"

MANUFACTURER = "Eaton"

PLATFORMS: list[Platform] = [
    #Platform.SENSOR
]

ATTR_NAME = "name"
ATTR_HOST = "host"
ATTR_PORT = "port"

HTTP_PORT_DEFAULT = 4679
