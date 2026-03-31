"""Constants for the place integration."""

from enum import IntEnum

DOMAIN = "gentex_place"
OAUTH2_TOKEN_URL = "https://connectedsmoke-sandbox-94e5744a-af6f-443b-bf23-d595e70c0a0c.auth.us-east-2.amazoncognito.com/oauth2/token"


class AlarmStatus(IntEnum):
    """Alarm status values from device shadow."""

    IDLE = 0
    TEST = 1
    PRE_ALARM = 2
    ALARM = 3
    CRITICAL_ALARM = 4
    HUSHED = 5
    NOT_PRESENT = 6
