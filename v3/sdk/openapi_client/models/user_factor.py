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

from datetime import datetime
from importlib import import_module
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from openapi_client.models.factor_provider import FactorProvider
from openapi_client.models.factor_status import FactorStatus
from openapi_client.models.factor_type import FactorType
from openapi_client.models.links_self import LinksSelf
from openapi_client.models.verify_factor_request import VerifyFactorRequest
from typing import Optional, Set
from typing_extensions import Self

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from openapi_client.models.call_user_factor import CallUserFactor
    from openapi_client.models.email_user_factor import EmailUserFactor
    from openapi_client.models.custom_hotp_user_factor import CustomHotpUserFactor
    from openapi_client.models.push_user_factor import PushUserFactor
    from openapi_client.models.security_question_user_factor import SecurityQuestionUserFactor
    from openapi_client.models.sms_user_factor import SmsUserFactor
    from openapi_client.models.token_user_factor import TokenUserFactor
    from openapi_client.models.hardware_user_factor import HardwareUserFactor
    from openapi_client.models.custom_hotp_user_factor import CustomHotpUserFactor
    from openapi_client.models.totp_user_factor import TotpUserFactor
    from openapi_client.models.u2f_user_factor import U2fUserFactor
    from openapi_client.models.web_user_factor import WebUserFactor
    from openapi_client.models.web_authn_user_factor import WebAuthnUserFactor

class UserFactor(BaseModel):
    """
    UserFactor
    """ # noqa: E501
    created: Optional[datetime] = None
    factor_type: Optional[FactorType] = Field(default=None, alias="factorType")
    id: Optional[StrictStr] = None
    last_updated: Optional[datetime] = Field(default=None, alias="lastUpdated")
    profile: Optional[Dict[str, Any]] = Field(default=None, description="Factor-specific attributes")
    provider: Optional[FactorProvider] = None
    status: Optional[FactorStatus] = None
    verify: Optional[VerifyFactorRequest] = None
    embedded: Optional[Dict[str, Dict[str, Any]]] = Field(default=None, alias="_embedded")
    links: Optional[LinksSelf] = Field(default=None, alias="_links")
    __properties: ClassVar[List[str]] = ["created", "factorType", "id", "lastUpdated", "profile", "provider", "status", "verify", "_embedded", "_links"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    # JSON field name that stores the object type
    __discriminator_property_name: ClassVar[str] = 'factorType'

    # discriminator mappings
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'call': 'CallUserFactor','email': 'EmailUserFactor','hotp': 'CustomHotpUserFactor','push': 'PushUserFactor','question': 'SecurityQuestionUserFactor','sms': 'SmsUserFactor','token': 'TokenUserFactor','token:hardware': 'HardwareUserFactor','token:hotp': 'CustomHotpUserFactor','token:software:totp': 'TotpUserFactor','u2f': 'U2fUserFactor','web': 'WebUserFactor','webauthn': 'WebAuthnUserFactor'
    }

    @classmethod
    def get_discriminator_value(cls, obj: Dict[str, Any]) -> Optional[str]:
        """Returns the discriminator value (object type) of the data"""
        discriminator_value = obj[cls.__discriminator_property_name]
        if discriminator_value:
            return cls.__discriminator_value_class_map.get(discriminator_value)
        else:
            return None

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Union[CallUserFactor, EmailUserFactor, CustomHotpUserFactor, PushUserFactor, SecurityQuestionUserFactor, SmsUserFactor, TokenUserFactor, HardwareUserFactor, CustomHotpUserFactor, TotpUserFactor, U2fUserFactor, WebUserFactor, WebAuthnUserFactor]]:
        """Create an instance of UserFactor from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "created",
            "id",
            "last_updated",
            "embedded",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of verify
        if self.verify:
            _dict['verify'] = self.verify.to_dict()
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Optional[Union[CallUserFactor, EmailUserFactor, CustomHotpUserFactor, PushUserFactor, SecurityQuestionUserFactor, SmsUserFactor, TokenUserFactor, HardwareUserFactor, CustomHotpUserFactor, TotpUserFactor, U2fUserFactor, WebUserFactor, WebAuthnUserFactor]]:
        """Create an instance of UserFactor from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type ==  'call':
            return import_module("openapi_client.models.call_user_factor").CallUserFactor.from_dict(obj)
        if object_type ==  'email':
            return import_module("openapi_client.models.email_user_factor").EmailUserFactor.from_dict(obj)
        if object_type ==  'hotp':
            return import_module("openapi_client.models.custom_hotp_user_factor").CustomHotpUserFactor.from_dict(obj)
        if object_type ==  'push':
            return import_module("openapi_client.models.push_user_factor").PushUserFactor.from_dict(obj)
        if object_type ==  'question':
            return import_module("openapi_client.models.security_question_user_factor").SecurityQuestionUserFactor.from_dict(obj)
        if object_type ==  'sms':
            return import_module("openapi_client.models.sms_user_factor").SmsUserFactor.from_dict(obj)
        if object_type ==  'token':
            return import_module("openapi_client.models.token_user_factor").TokenUserFactor.from_dict(obj)
        if object_type ==  'token:hardware':
            return import_module("openapi_client.models.hardware_user_factor").HardwareUserFactor.from_dict(obj)
        if object_type ==  'token:hotp':
            return import_module("openapi_client.models.custom_hotp_user_factor").CustomHotpUserFactor.from_dict(obj)
        if object_type ==  'token:software:totp':
            return import_module("openapi_client.models.totp_user_factor").TotpUserFactor.from_dict(obj)
        if object_type ==  'u2f':
            return import_module("openapi_client.models.u2f_user_factor").U2fUserFactor.from_dict(obj)
        if object_type ==  'web':
            return import_module("openapi_client.models.web_user_factor").WebUserFactor.from_dict(obj)
        if object_type ==  'webauthn':
            return import_module("openapi_client.models.web_authn_user_factor").WebAuthnUserFactor.from_dict(obj)

        raise ValueError("UserFactor failed to lookup discriminator value from " +
                            json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                            ", mapping: " + json.dumps(cls.__discriminator_value_class_map))

