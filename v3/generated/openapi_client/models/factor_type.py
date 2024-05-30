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


class FactorType(str, Enum):
    """
    FactorType
    """

    """
    allowed enum values
    """
    CALL = 'call'
    EMAIL = 'email'
    PUSH = 'push'
    QUESTION = 'question'
    SIGNED_NONCE = 'signed_nonce'
    SMS = 'sms'
    TOKEN = 'token'
    TOKEN_COLON_HARDWARE = 'token:hardware'
    TOKEN_COLON_HOTP = 'token:hotp'
    TOKEN_COLON_SOFTWARE_COLON_TOTP = 'token:software:totp'
    U2F = 'u2f'
    WEB = 'web'
    WEBAUTHN = 'webauthn'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of FactorType from a JSON string"""
        return cls(json.loads(json_str))


