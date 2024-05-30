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


class KeyTrustLevelOSMode(str, Enum):
    """
    Represents the attestation strength used by the Chrome Verified Access API
    """

    """
    allowed enum values
    """
    CHROME_OS_DEVELOPER_MODE = 'CHROME_OS_DEVELOPER_MODE'
    CHROME_OS_VERIFIED_MODE = 'CHROME_OS_VERIFIED_MODE'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of KeyTrustLevelOSMode from a JSON string"""
        return cls(json.loads(json_str))


