# Eaton UPS Companion integration for Home Assistant

[![Version](https://img.shields.io/github/v/release/routmoute/home-assistant-eaton-ups-companion?label=version)](https://github.com/routmoute/home-assistant-eaton-ups-companion/releases/latest)
[![Validate for HACS](https://github.com/routmoute/home-assistant-eaton-ups-companion/workflows/Validate%20for%20HACS/badge.svg)](https://github.com/routmoute/home-assistant-eaton-ups-companion/actions/workflows/hacs.yaml)
[![Validate% with hassfest](https://github.com/routmoute/home-assistant-eaton-up-companion/workflows/Validate%20with%20hassfest/badge.svg)](https://github.com/routmoute/home-assistant-eaton-ups-companion/actions/workflows/hassfest.yaml)

Custom Home Assistant integration to get datas from windows Eaton UPS Companion

## Port Configuration
If you want access to UPS Companion from another machine than localhost, you need to open port 4679 in your windows firewall

## Install
### HACS
The easiest way to install this component is by clicking the badge below, which adds this repo as a custom repo in your HASS instance.

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?category=Integration&owner=routmoute&repository=home-assistant-eaton-ups-companion)

You can also add the integration manually by copying `custom_components/eaton_ups_companion` into `<HASS config directory>/custom_components`
