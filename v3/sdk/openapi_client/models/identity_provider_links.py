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
from openapi_client.models.href_object_self_link import HrefObjectSelfLink
from typing import Optional, Set
from typing_extensions import Self

class IdentityProviderLinks(BaseModel):
    """
    IdentityProviderLinks
    """ # noqa: E501
    var_self: Optional[HrefObjectSelfLink] = Field(default=None, alias="self")
    acs: Optional[HrefObject] = Field(default=None, description="SAML 2.0 Assertion Consumer Service URL for the Okta SP")
    authorize: Optional[HrefObject] = Field(default=None, description="OAuth 2.0 authorization endpoint for the IdP OAuth 2.0 Authorization Code flow")
    client_redirect_uri: Optional[HrefObject] = Field(default=None, description="Redirect URI for the OAuth 2.0 Authorization Code flow", alias="clientRedirectUri")
    metadata: Optional[HrefObject] = Field(default=None, description="Federation metadata document for the IdP (for example: SAML 2.0 Metadata)")
    users: Optional[HrefObject] = Field(default=None, description="IdP users")
    deactivate: Optional[HrefObject] = Field(default=None, description="Deactivate IdP")
    activate: Optional[HrefObject] = Field(default=None, description="Activate IdP")
    keys: Optional[HrefObject] = Field(default=None, description="IdP keys")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["self", "acs", "authorize", "clientRedirectUri", "metadata", "users", "deactivate", "activate", "keys"]

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
        """Create an instance of IdentityProviderLinks from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of var_self
        if self.var_self:
            _dict['self'] = self.var_self.to_dict()
        # override the default output from pydantic by calling `to_dict()` of acs
        if self.acs:
            _dict['acs'] = self.acs.to_dict()
        # override the default output from pydantic by calling `to_dict()` of authorize
        if self.authorize:
            _dict['authorize'] = self.authorize.to_dict()
        # override the default output from pydantic by calling `to_dict()` of client_redirect_uri
        if self.client_redirect_uri:
            _dict['clientRedirectUri'] = self.client_redirect_uri.to_dict()
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of users
        if self.users:
            _dict['users'] = self.users.to_dict()
        # override the default output from pydantic by calling `to_dict()` of deactivate
        if self.deactivate:
            _dict['deactivate'] = self.deactivate.to_dict()
        # override the default output from pydantic by calling `to_dict()` of activate
        if self.activate:
            _dict['activate'] = self.activate.to_dict()
        # override the default output from pydantic by calling `to_dict()` of keys
        if self.keys:
            _dict['keys'] = self.keys.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IdentityProviderLinks from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "self": HrefObjectSelfLink.from_dict(obj["self"]) if obj.get("self") is not None else None,
            "acs": HrefObject.from_dict(obj["acs"]) if obj.get("acs") is not None else None,
            "authorize": HrefObject.from_dict(obj["authorize"]) if obj.get("authorize") is not None else None,
            "clientRedirectUri": HrefObject.from_dict(obj["clientRedirectUri"]) if obj.get("clientRedirectUri") is not None else None,
            "metadata": HrefObject.from_dict(obj["metadata"]) if obj.get("metadata") is not None else None,
            "users": HrefObject.from_dict(obj["users"]) if obj.get("users") is not None else None,
            "deactivate": HrefObject.from_dict(obj["deactivate"]) if obj.get("deactivate") is not None else None,
            "activate": HrefObject.from_dict(obj["activate"]) if obj.get("activate") is not None else None,
            "keys": HrefObject.from_dict(obj["keys"]) if obj.get("keys") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

