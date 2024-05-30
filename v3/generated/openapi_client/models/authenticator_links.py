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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.href_object import HrefObject
from openapi_client.models.href_object_activate_link import HrefObjectActivateLink
from openapi_client.models.href_object_deactivate_link import HrefObjectDeactivateLink
from openapi_client.models.href_object_self_link import HrefObjectSelfLink
from typing import Optional, Set
from typing_extensions import Self

class AuthenticatorLinks(BaseModel):
    """
    AuthenticatorLinks
    """ # noqa: E501
    var_self: Optional[HrefObjectSelfLink] = Field(default=None, alias="self")
    activate: Optional[HrefObjectActivateLink] = None
    deactivate: Optional[HrefObjectDeactivateLink] = None
    methods: Optional[HrefObject] = Field(default=None, description="Link to Authenticator methods")
    __properties: ClassVar[List[str]] = ["self", "activate", "deactivate", "methods"]

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
        """Create an instance of AuthenticatorLinks from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of var_self
        if self.var_self:
            _dict['self'] = self.var_self.to_dict()
        # override the default output from pydantic by calling `to_dict()` of activate
        if self.activate:
            _dict['activate'] = self.activate.to_dict()
        # override the default output from pydantic by calling `to_dict()` of deactivate
        if self.deactivate:
            _dict['deactivate'] = self.deactivate.to_dict()
        # override the default output from pydantic by calling `to_dict()` of methods
        if self.methods:
            _dict['methods'] = self.methods.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AuthenticatorLinks from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "self": HrefObjectSelfLink.from_dict(obj["self"]) if obj.get("self") is not None else None,
            "activate": HrefObjectActivateLink.from_dict(obj["activate"]) if obj.get("activate") is not None else None,
            "deactivate": HrefObjectDeactivateLink.from_dict(obj["deactivate"]) if obj.get("deactivate") is not None else None,
            "methods": HrefObject.from_dict(obj["methods"]) if obj.get("methods") is not None else None
        })
        return _obj


