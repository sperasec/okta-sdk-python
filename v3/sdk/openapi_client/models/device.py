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
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.device_display_name import DeviceDisplayName
from openapi_client.models.device_profile import DeviceProfile
from openapi_client.models.device_status import DeviceStatus
from openapi_client.models.links_self_and_full_users_lifecycle import LinksSelfAndFullUsersLifecycle
from typing import Optional, Set
from typing_extensions import Self

class Device(BaseModel):
    """
    Device
    """ # noqa: E501
    created: Optional[datetime] = Field(default=None, description="Timestamp when the device was created")
    id: Optional[StrictStr] = Field(default=None, description="Unique key for the device")
    last_updated: Optional[datetime] = Field(default=None, description="Timestamp when the device record was last updated. Updates occur when Okta collects and saves device signals during authentication, and when the lifecycle state of the device changes.", alias="lastUpdated")
    profile: Optional[DeviceProfile] = None
    resource_alternate_id: Optional[StrictStr] = Field(default=None, alias="resourceAlternateId")
    resource_display_name: Optional[DeviceDisplayName] = Field(default=None, alias="resourceDisplayName")
    resource_id: Optional[StrictStr] = Field(default=None, description="Alternate key for the `id`", alias="resourceId")
    resource_type: Optional[StrictStr] = Field(default='UDDevice', alias="resourceType")
    status: Optional[DeviceStatus] = None
    links: Optional[LinksSelfAndFullUsersLifecycle] = Field(default=None, alias="_links")
    __properties: ClassVar[List[str]] = ["created", "id", "lastUpdated", "profile", "resourceAlternateId", "resourceDisplayName", "resourceId", "resourceType", "status", "_links"]

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
        """Create an instance of Device from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "created",
            "id",
            "last_updated",
            "resource_alternate_id",
            "resource_id",
            "resource_type",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of profile
        if self.profile:
            _dict['profile'] = self.profile.to_dict()
        # override the default output from pydantic by calling `to_dict()` of resource_display_name
        if self.resource_display_name:
            _dict['resourceDisplayName'] = self.resource_display_name.to_dict()
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Device from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created": obj.get("created"),
            "id": obj.get("id"),
            "lastUpdated": obj.get("lastUpdated"),
            "profile": DeviceProfile.from_dict(obj["profile"]) if obj.get("profile") is not None else None,
            "resourceAlternateId": obj.get("resourceAlternateId"),
            "resourceDisplayName": DeviceDisplayName.from_dict(obj["resourceDisplayName"]) if obj.get("resourceDisplayName") is not None else None,
            "resourceId": obj.get("resourceId"),
            "resourceType": obj.get("resourceType") if obj.get("resourceType") is not None else 'UDDevice',
            "status": obj.get("status"),
            "_links": LinksSelfAndFullUsersLifecycle.from_dict(obj["_links"]) if obj.get("_links") is not None else None
        })
        return _obj

