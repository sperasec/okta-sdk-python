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


class ApplicationSignOnMode(str, Enum):
    """
    ApplicationSignOnMode
    """

    """
    allowed enum values
    """
    AUTO_LOGIN = 'AUTO_LOGIN'
    BASIC_AUTH = 'BASIC_AUTH'
    BOOKMARK = 'BOOKMARK'
    BROWSER_PLUGIN = 'BROWSER_PLUGIN'
    OPENID_CONNECT = 'OPENID_CONNECT'
    SAML_1_1 = 'SAML_1_1'
    SAML_2_0 = 'SAML_2_0'
    SECURE_PASSWORD_STORE = 'SECURE_PASSWORD_STORE'
    WS_FEDERATION = 'WS_FEDERATION'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ApplicationSignOnMode from a JSON string"""
        return cls(json.loads(json_str))

