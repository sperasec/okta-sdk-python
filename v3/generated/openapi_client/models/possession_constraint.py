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
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.authentication_method_object import AuthenticationMethodObject
from typing import Optional, Set
from typing_extensions import Self

class PossessionConstraint(BaseModel):
    """
    PossessionConstraint
    """ # noqa: E501
    methods: Optional[List[StrictStr]] = Field(default=None, description="The Authenticator methods that are permitted")
    reauthenticate_in: Optional[StrictStr] = Field(default=None, description="The duration after which the user must re-authenticate regardless of user activity. This re-authentication interval overrides the Verification Method object's `reauthenticateIn` interval. The supported values use ISO 8601 period format for recurring time intervals (for example, `PT1H`).", alias="reauthenticateIn")
    types: Optional[List[StrictStr]] = Field(default=None, description="The Authenticator types that are permitted")
    authentication_methods: Optional[List[AuthenticationMethodObject]] = Field(default=None, description="This property specifies the precise authenticator and method for authentication.", alias="authenticationMethods")
    excluded_authentication_methods: Optional[List[AuthenticationMethodObject]] = Field(default=None, description="This property specifies the precise authenticator and method to exclude from authentication.", alias="excludedAuthenticationMethods")
    required: Optional[StrictBool] = Field(default=None, description="This property indicates whether the knowledge or possession factor is required by the assurance. It's optional in the request, but is always returned in the response. By default, this field is `true`. If the knowledge or possession constraint has values for`excludedAuthenticationMethods` the `required` value is false.")
    device_bound: Optional[StrictStr] = Field(default='OPTIONAL', description="Indicates if device-bound Factors are required. This property is only set for `POSSESSION` constraints.", alias="deviceBound")
    hardware_protection: Optional[StrictStr] = Field(default='OPTIONAL', description="Indicates if any secrets or private keys used during authentication must be hardware protected and not exportable. This property is only set for `POSSESSION` constraints.", alias="hardwareProtection")
    phishing_resistant: Optional[StrictStr] = Field(default='OPTIONAL', description="Indicates if phishing-resistant Factors are required. This property is only set for `POSSESSION` constraints.", alias="phishingResistant")
    user_presence: Optional[StrictStr] = Field(default='REQUIRED', description="Indicates if the user needs to approve an Okta Verify prompt or provide biometrics (meets NIST AAL2 requirements). This property is only set for `POSSESSION` constraints.", alias="userPresence")
    user_verification: Optional[StrictStr] = Field(default='OPTIONAL', description="Indicates the user interaction requirement (PIN or biometrics) to ensure verification of a possession factor", alias="userVerification")
    __properties: ClassVar[List[str]] = ["methods", "reauthenticateIn", "types", "authenticationMethods", "excludedAuthenticationMethods", "required", "deviceBound", "hardwareProtection", "phishingResistant", "userPresence", "userVerification"]

    @field_validator('methods')
    def methods_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['PASSWORD', 'SECURITY_QUESTION', 'SMS', 'VOICE', 'EMAIL', 'PUSH', 'SIGNED_NONCE', 'OTP', 'TOTP', 'WEBAUTHN', 'DUO', 'IDP', 'CERT']):
                raise ValueError("each list item must be one of ('PASSWORD', 'SECURITY_QUESTION', 'SMS', 'VOICE', 'EMAIL', 'PUSH', 'SIGNED_NONCE', 'OTP', 'TOTP', 'WEBAUTHN', 'DUO', 'IDP', 'CERT')")
        return value

    @field_validator('types')
    def types_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['SECURITY_KEY', 'PHONE', 'EMAIL', 'PASSWORD', 'SECURITY_QUESTION', 'APP', 'FEDERATED']):
                raise ValueError("each list item must be one of ('SECURITY_KEY', 'PHONE', 'EMAIL', 'PASSWORD', 'SECURITY_QUESTION', 'APP', 'FEDERATED')")
        return value

    @field_validator('device_bound')
    def device_bound_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['OPTIONAL', 'REQUIRED']):
            raise ValueError("must be one of enum values ('OPTIONAL', 'REQUIRED')")
        return value

    @field_validator('hardware_protection')
    def hardware_protection_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['OPTIONAL', 'REQUIRED']):
            raise ValueError("must be one of enum values ('OPTIONAL', 'REQUIRED')")
        return value

    @field_validator('phishing_resistant')
    def phishing_resistant_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['OPTIONAL', 'REQUIRED']):
            raise ValueError("must be one of enum values ('OPTIONAL', 'REQUIRED')")
        return value

    @field_validator('user_presence')
    def user_presence_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['OPTIONAL', 'REQUIRED']):
            raise ValueError("must be one of enum values ('OPTIONAL', 'REQUIRED')")
        return value

    @field_validator('user_verification')
    def user_verification_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['OPTIONAL', 'REQUIRED']):
            raise ValueError("must be one of enum values ('OPTIONAL', 'REQUIRED')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of PossessionConstraint from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in authentication_methods (list)
        _items = []
        if self.authentication_methods:
            for _item in self.authentication_methods:
                if _item:
                    _items.append(_item.to_dict())
            _dict['authenticationMethods'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in excluded_authentication_methods (list)
        _items = []
        if self.excluded_authentication_methods:
            for _item in self.excluded_authentication_methods:
                if _item:
                    _items.append(_item.to_dict())
            _dict['excludedAuthenticationMethods'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PossessionConstraint from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "methods": obj.get("methods"),
            "reauthenticateIn": obj.get("reauthenticateIn"),
            "types": obj.get("types"),
            "authenticationMethods": [AuthenticationMethodObject.from_dict(_item) for _item in obj["authenticationMethods"]] if obj.get("authenticationMethods") is not None else None,
            "excludedAuthenticationMethods": [AuthenticationMethodObject.from_dict(_item) for _item in obj["excludedAuthenticationMethods"]] if obj.get("excludedAuthenticationMethods") is not None else None,
            "required": obj.get("required"),
            "deviceBound": obj.get("deviceBound") if obj.get("deviceBound") is not None else 'OPTIONAL',
            "hardwareProtection": obj.get("hardwareProtection") if obj.get("hardwareProtection") is not None else 'OPTIONAL',
            "phishingResistant": obj.get("phishingResistant") if obj.get("phishingResistant") is not None else 'OPTIONAL',
            "userPresence": obj.get("userPresence") if obj.get("userPresence") is not None else 'REQUIRED',
            "userVerification": obj.get("userVerification") if obj.get("userVerification") is not None else 'OPTIONAL'
        })
        return _obj


