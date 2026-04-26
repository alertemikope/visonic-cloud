"""Constants for the Visonic Cloud integration."""

from datetime import timedelta

DOMAIN = "visonic_cloud"

DEFAULT_BASE_URL = "https://visonic.tycomonitor.com"
DEFAULT_API_VERSION = "14.0"
SUPPORTED_API_VERSIONS = ("14.0", "10.0")


def build_api_base(base_url: str, api_version: str) -> str:
    """Build the REST API base URL."""
    return f"{base_url.rstrip('/')}/rest_api/{api_version}"

CONF_BASE_URL = "base_url"
CONF_PANEL_SERIAL = "panel_serial"
CONF_PANEL_ALIAS = "panel_alias"
CONF_USER_CODE = "user_code"
CONF_APP_ID = "app_id"
CONF_USER_TOKEN = "user_token"
CONF_SESSION_TOKEN = "session_token"

UPDATE_INTERVAL = timedelta(minutes=2)

# Device type mappings
DEVICE_TYPE_ZONE = "ZONE"
DEVICE_TYPE_CONTROL_PANEL = "CONTROL_PANEL"
DEVICE_TYPE_POWER_LINK = "POWER_LINK"
DEVICE_TYPE_PGM = "PGM"
DEVICE_TYPE_WIRELESS_COMMANDER = "WIRELESS_COMMANDER"

# Zone subtypes
SUBTYPE_MC303_VANISH = "MC303_VANISH"
SUBTYPE_FLAT_PIR_SMART = "FLAT_PIR_SMART"
SUBTYPE_CURTAIN = "CURTAIN"
SUBTYPE_PGM_ON_PANEL = "PGM_ON_PANEL"
SUBTYPE_KEYPAD = "KEYPAD"

# Partition states
PARTITION_STATE_DISARM = "DISARM"
PARTITION_STATE_AWAY = "AWAY"
PARTITION_STATE_HOME = "HOME"
PARTITION_STATE_EXIT = "EXIT"

PLATFORMS = ["alarm_control_panel", "binary_sensor", "sensor"]
