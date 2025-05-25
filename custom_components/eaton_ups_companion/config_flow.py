"""Config flow for Eaton UPS Companion integration."""

from __future__ import annotations

import voluptuous as vol
from voluptuous.schema_builder import Schema

from homeassistant import config_entries
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import callback
from homeassistant.data_entry_flow import FlowResult
from homeassistant.exceptions import HomeAssistantError
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.typing import ConfigType

from .const import (
    ATTR_HOST,
    ATTR_NAME,
    ATTR_PORT,
    DOMAIN,
    HTTP_PORT_DEFAULT
)

def get_host_schema_config(data: ConfigType) -> Schema:
    """Return the host schema for config flow."""

    return vol.Schema({
        vol.Required(ATTR_NAME, default=data.get(ATTR_NAME)): cv.string,
        vol.Required(ATTR_HOST, default=data.get(ATTR_HOST)): cv.string,
        vol.Required(ATTR_PORT, default=data.get(ATTR_PORT, HTTP_PORT_DEFAULT)): cv.port
    })

def get_host_schema_options(data: ConfigType) -> Schema:
    """Return the host schema for options flow."""

    return vol.Schema({
        vol.Required(ATTR_HOST, default=data.get(ATTR_HOST)): cv.string,
        vol.Required(ATTR_PORT, default=data.get(ATTR_PORT, HTTP_PORT_DEFAULT)): cv.port
    })

class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Eaton UPS Companion."""

    VERSION = 1

    def __init__(self) -> None:
        """Init the ConfigFlow."""
        self.data: ConfigType = {}

    async def async_step_user(self, user_input: ConfigType | None = None) -> FlowResult:
        """Handle the initial step."""
        return await self.async_step_host(host_input=user_input)

    async def async_step_host(self, host_input: ConfigType | None = None) -> FlowResult:
        """Handle the host step."""
        if host_input is not None:
            self.data = host_input
            return self.async_create_entry(title=self.data[ATTR_NAME], data=self.data)

        return self.async_show_form(step_id="host", data_schema=get_host_schema_config(data=self.data))

    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry):
        """Options callback for Eaton UPS Companion."""
        return OptionsFlow(config_entry)

class OptionsFlow(config_entries.OptionsFlow):
    """Handle a options flow for Eaton UPS Companion."""

    def __init__(self, entry: ConfigEntry) -> None:
        """Initialize Eaton UPS options flow."""
        self.data = dict(entry.data)

    async def async_step_init(self, user_input: ConfigType | None = None) -> FlowResult:
        """Manage the options."""
        return await self.async_step_host(host_input=user_input)

    async def async_step_host(self, host_input: ConfigType | None = None) -> FlowResult:
        """Handle the host step."""
        if host_input is not None:
            self.data.update(host_input)
            self.hass.config_entries.async_update_entry(self.config_entry, data=self.data)
            return self.async_create_entry(title="", data={})

        return self.async_show_form(step_id="host", data_schema=get_host_schema_options(data=self.data))

class CannotConnect(HomeAssistantError):
    """Error to indicate we cannot connect."""
