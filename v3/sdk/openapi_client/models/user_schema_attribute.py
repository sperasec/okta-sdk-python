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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.user_schema_attribute_enum import UserSchemaAttributeEnum
from openapi_client.models.user_schema_attribute_items import UserSchemaAttributeItems
from openapi_client.models.user_schema_attribute_master import UserSchemaAttributeMaster
from openapi_client.models.user_schema_attribute_permission import UserSchemaAttributePermission
from openapi_client.models.user_schema_attribute_scope import UserSchemaAttributeScope
from openapi_client.models.user_schema_attribute_type import UserSchemaAttributeType
from openapi_client.models.user_schema_attribute_union import UserSchemaAttributeUnion
from typing import Optional, Set
from typing_extensions import Self

class UserSchemaAttribute(BaseModel):
    """
    UserSchemaAttribute
    """ # noqa: E501
    description: Optional[StrictStr] = None
    enum: Optional[List[StrictStr]] = None
    external_name: Optional[StrictStr] = Field(default=None, alias="externalName")
    external_namespace: Optional[StrictStr] = Field(default=None, alias="externalNamespace")
    items: Optional[UserSchemaAttributeItems] = None
    master: Optional[UserSchemaAttributeMaster] = None
    max_length: Optional[StrictInt] = Field(default=None, alias="maxLength")
    min_length: Optional[StrictInt] = Field(default=None, alias="minLength")
    mutability: Optional[StrictStr] = None
    one_of: Optional[List[UserSchemaAttributeEnum]] = Field(default=None, alias="oneOf")
    pattern: Optional[StrictStr] = None
    permissions: Optional[List[UserSchemaAttributePermission]] = None
    required: Optional[StrictBool] = None
    scope: Optional[UserSchemaAttributeScope] = None
    title: Optional[StrictStr] = None
    type: Optional[UserSchemaAttributeType] = None
    union: Optional[UserSchemaAttributeUnion] = None
    unique: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["description", "enum", "externalName", "externalNamespace", "items", "master", "maxLength", "minLength", "mutability", "oneOf", "pattern", "permissions", "required", "scope", "title", "type", "union", "unique"]

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
        """Create an instance of UserSchemaAttribute from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of items
        if self.items:
            _dict['items'] = self.items.to_dict()
        # override the default output from pydantic by calling `to_dict()` of master
        if self.master:
            _dict['master'] = self.master.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in one_of (list)
        _items = []
        if self.one_of:
            for _item in self.one_of:
                if _item:
                    _items.append(_item.to_dict())
            _dict['oneOf'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in permissions (list)
        _items = []
        if self.permissions:
            for _item in self.permissions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['permissions'] = _items
        # set to None if max_length (nullable) is None
        # and model_fields_set contains the field
        if self.max_length is None and "max_length" in self.model_fields_set:
            _dict['maxLength'] = None

        # set to None if min_length (nullable) is None
        # and model_fields_set contains the field
        if self.min_length is None and "min_length" in self.model_fields_set:
            _dict['minLength'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserSchemaAttribute from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "description": obj.get("description"),
            "enum": obj.get("enum"),
            "externalName": obj.get("externalName"),
            "externalNamespace": obj.get("externalNamespace"),
            "items": UserSchemaAttributeItems.from_dict(obj["items"]) if obj.get("items") is not None else None,
            "master": UserSchemaAttributeMaster.from_dict(obj["master"]) if obj.get("master") is not None else None,
            "maxLength": obj.get("maxLength"),
            "minLength": obj.get("minLength"),
            "mutability": obj.get("mutability"),
            "oneOf": [UserSchemaAttributeEnum.from_dict(_item) for _item in obj["oneOf"]] if obj.get("oneOf") is not None else None,
            "pattern": obj.get("pattern"),
            "permissions": [UserSchemaAttributePermission.from_dict(_item) for _item in obj["permissions"]] if obj.get("permissions") is not None else None,
            "required": obj.get("required"),
            "scope": obj.get("scope"),
            "title": obj.get("title"),
            "type": obj.get("type"),
            "union": obj.get("union"),
            "unique": obj.get("unique")
        })
        return _obj

