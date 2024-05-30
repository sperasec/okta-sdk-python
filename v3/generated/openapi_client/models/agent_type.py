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


class AgentType(str, Enum):
    """
    Agent types that are being monitored
    """

    """
    allowed enum values
    """
    AD = 'AD'
    IWA = 'IWA'
    LDAP = 'LDAP'
    MFA = 'MFA'
    OPP = 'OPP'
    RUM = 'RUM'
    RADIUS = 'Radius'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AgentType from a JSON string"""
        return cls(json.loads(json_str))


