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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.authenticator_identity import AuthenticatorIdentity
from typing import Optional, Set
from typing_extensions import Self

class AuthenticatorMethodConstraint(BaseModel):
    """
    Limits the authenticators that can be used for a given method. Currently, only the `otp` method supports constraints, and Google authenticator (key : 'google_otp') is the only allowed authenticator.
    """ # noqa: E501
    method: Optional[StrictStr] = None
    allowed_authenticators: Optional[List[AuthenticatorIdentity]] = Field(default=None, alias="allowedAuthenticators")
    __properties: ClassVar[List[str]] = ["method", "allowedAuthenticators"]

    @field_validator('method')
    def method_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['otp']):
            raise ValueError("must be one of enum values ('otp')")
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
        """Create an instance of AuthenticatorMethodConstraint from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in allowed_authenticators (list)
        _items = []
        if self.allowed_authenticators:
            for _item in self.allowed_authenticators:
                if _item:
                    _items.append(_item.to_dict())
            _dict['allowedAuthenticators'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AuthenticatorMethodConstraint from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "method": obj.get("method"),
            "allowedAuthenticators": [AuthenticatorIdentity.from_dict(_item) for _item in obj["allowedAuthenticators"]] if obj.get("allowedAuthenticators") is not None else None
        })
        return _obj

