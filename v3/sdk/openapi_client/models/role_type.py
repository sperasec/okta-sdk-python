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


class RoleType(str, Enum):
    """
    RoleType
    """

    """
    allowed enum values
    """
    API_ACCESS_MANAGEMENT_ADMIN = 'API_ACCESS_MANAGEMENT_ADMIN'
    API_ADMIN = 'API_ADMIN'
    APP_ADMIN = 'APP_ADMIN'
    CUSTOM = 'CUSTOM'
    GROUP_MEMBERSHIP_ADMIN = 'GROUP_MEMBERSHIP_ADMIN'
    HELP_DESK_ADMIN = 'HELP_DESK_ADMIN'
    MOBILE_ADMIN = 'MOBILE_ADMIN'
    ORG_ADMIN = 'ORG_ADMIN'
    READ_ONLY_ADMIN = 'READ_ONLY_ADMIN'
    REPORT_ADMIN = 'REPORT_ADMIN'
    SUPER_ADMIN = 'SUPER_ADMIN'
    USER_ADMIN = 'USER_ADMIN'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of RoleType from a JSON string"""
        return cls(json.loads(json_str))

