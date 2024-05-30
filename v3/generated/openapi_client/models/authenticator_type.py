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


class AuthenticatorType(str, Enum):
    """
    AuthenticatorType
    """

    """
    allowed enum values
    """
    APP = 'app'
    EMAIL = 'email'
    FEDERATED = 'federated'
    PASSWORD = 'password'
    PHONE = 'phone'
    SECURITY_KEY = 'security_key'
    SECURITY_QUESTION = 'security_question'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AuthenticatorType from a JSON string"""
        return cls(json.loads(json_str))


