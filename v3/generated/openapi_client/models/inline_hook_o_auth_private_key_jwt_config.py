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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.inline_hook_channel_config_auth_scheme import InlineHookChannelConfigAuthScheme
from openapi_client.models.inline_hook_channel_config_headers import InlineHookChannelConfigHeaders
from typing import Optional, Set
from typing_extensions import Self

class InlineHookOAuthPrivateKeyJwtConfig(BaseModel):
    """
    InlineHookOAuthPrivateKeyJwtConfig
    """ # noqa: E501
    hook_key_id: Optional[StrictStr] = Field(default=None, alias="hookKeyId")
    auth_type: Optional[StrictStr] = Field(default=None, alias="authType")
    client_id: Optional[StrictStr] = Field(default=None, alias="clientId")
    scope: Optional[StrictStr] = None
    token_url: Optional[StrictStr] = Field(default=None, alias="tokenUrl")
    auth_scheme: Optional[InlineHookChannelConfigAuthScheme] = Field(default=None, alias="authScheme")
    headers: Optional[List[InlineHookChannelConfigHeaders]] = None
    method: Optional[StrictStr] = None
    uri: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["authType", "clientId", "scope", "tokenUrl", "authScheme", "headers", "method", "uri"]

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
        """Create an instance of InlineHookOAuthPrivateKeyJwtConfig from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of auth_scheme
        if self.auth_scheme:
            _dict['authScheme'] = self.auth_scheme.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in headers (list)
        _items = []
        if self.headers:
            for _item in self.headers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['headers'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InlineHookOAuthPrivateKeyJwtConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "authType": obj.get("authType"),
            "clientId": obj.get("clientId"),
            "scope": obj.get("scope"),
            "tokenUrl": obj.get("tokenUrl"),
            "authScheme": InlineHookChannelConfigAuthScheme.from_dict(obj["authScheme"]) if obj.get("authScheme") is not None else None,
            "headers": [InlineHookChannelConfigHeaders.from_dict(_item) for _item in obj["headers"]] if obj.get("headers") is not None else None,
            "method": obj.get("method"),
            "uri": obj.get("uri")
        })
        return _obj


