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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.o_auth2_scope_consent_type import OAuth2ScopeConsentType
from openapi_client.models.o_auth2_scope_metadata_publish import OAuth2ScopeMetadataPublish
from typing import Optional, Set
from typing_extensions import Self

class OAuth2Scope(BaseModel):
    """
    OAuth2Scope
    """ # noqa: E501
    consent: Optional[OAuth2ScopeConsentType] = None
    default: Optional[StrictBool] = None
    description: Optional[StrictStr] = None
    display_name: Optional[StrictStr] = Field(default=None, alias="displayName")
    id: Optional[StrictStr] = None
    metadata_publish: Optional[OAuth2ScopeMetadataPublish] = Field(default=None, alias="metadataPublish")
    name: Optional[StrictStr] = None
    system: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["consent", "default", "description", "displayName", "id", "metadataPublish", "name", "system"]

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
        """Create an instance of OAuth2Scope from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OAuth2Scope from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "consent": obj.get("consent"),
            "default": obj.get("default"),
            "description": obj.get("description"),
            "displayName": obj.get("displayName"),
            "id": obj.get("id"),
            "metadataPublish": obj.get("metadataPublish"),
            "name": obj.get("name"),
            "system": obj.get("system")
        })
        return _obj


