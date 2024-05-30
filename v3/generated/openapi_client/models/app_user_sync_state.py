# coding: utf-8

"""
    Okta Admin Management

    Allows customers to easily access the Okta Management APIs

    The version of the OpenAPI document: 5.1.0
    Contact: devex-public@okta.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class AppUserSyncState(str, Enum):
    """
    The synchronization state for the App User. The App User's `syncState` depends on whether the `PROFILE_MASTERING` feature is enabled for the app.  > **Note:** User provisioning currently must be configured through the Admin Console.
    """

    """
    allowed enum values
    """
    DISABLED = 'DISABLED'
    ERROR = 'ERROR'
    OUT_OF_SYNC = 'OUT_OF_SYNC'
    SYNCHRONIZED = 'SYNCHRONIZED'
    SYNCING = 'SYNCING'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AppUserSyncState from a JSON string"""
        return cls(json.loads(json_str))


