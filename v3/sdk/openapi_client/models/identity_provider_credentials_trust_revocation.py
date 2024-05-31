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


class IdentityProviderCredentialsTrustRevocation(str, Enum):
    """
    IdentityProviderCredentialsTrustRevocation
    """

    """
    allowed enum values
    """
    CRL = 'CRL'
    DELTA_CRL = 'DELTA_CRL'
    OCSP = 'OCSP'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of IdentityProviderCredentialsTrustRevocation from a JSON string"""
        return cls(json.loads(json_str))

