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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.password_credential import PasswordCredential
from typing import Optional, Set
from typing_extensions import Self

class ChangePasswordRequest(BaseModel):
    """
    ChangePasswordRequest
    """ # noqa: E501
    new_password: Optional[PasswordCredential] = Field(default=None, alias="newPassword")
    old_password: Optional[PasswordCredential] = Field(default=None, alias="oldPassword")
    revoke_sessions: Optional[StrictBool] = Field(default=None, alias="revokeSessions")
    __properties: ClassVar[List[str]] = ["newPassword", "oldPassword", "revokeSessions"]

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
        """Create an instance of ChangePasswordRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of new_password
        if self.new_password:
            _dict['newPassword'] = self.new_password.to_dict()
        # override the default output from pydantic by calling `to_dict()` of old_password
        if self.old_password:
            _dict['oldPassword'] = self.old_password.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ChangePasswordRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "newPassword": PasswordCredential.from_dict(obj["newPassword"]) if obj.get("newPassword") is not None else None,
            "oldPassword": PasswordCredential.from_dict(obj["oldPassword"]) if obj.get("oldPassword") is not None else None,
            "revokeSessions": obj.get("revokeSessions")
        })
        return _obj


