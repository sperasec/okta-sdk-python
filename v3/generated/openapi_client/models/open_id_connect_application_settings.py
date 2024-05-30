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
from openapi_client.models.application_settings_notes import ApplicationSettingsNotes
from openapi_client.models.application_settings_notifications import ApplicationSettingsNotifications
from openapi_client.models.open_id_connect_application_settings_client import OpenIdConnectApplicationSettingsClient
from typing import Optional, Set
from typing_extensions import Self

class OpenIdConnectApplicationSettings(BaseModel):
    """
    OpenIdConnectApplicationSettings
    """ # noqa: E501
    identity_store_id: Optional[StrictStr] = Field(default=None, alias="identityStoreId")
    implicit_assignment: Optional[StrictBool] = Field(default=None, alias="implicitAssignment")
    inline_hook_id: Optional[StrictStr] = Field(default=None, alias="inlineHookId")
    notes: Optional[ApplicationSettingsNotes] = None
    notifications: Optional[ApplicationSettingsNotifications] = None
    oauth_client: Optional[OpenIdConnectApplicationSettingsClient] = Field(default=None, alias="oauthClient")
    __properties: ClassVar[List[str]] = ["identityStoreId", "implicitAssignment", "inlineHookId", "notes", "notifications", "oauthClient"]

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
        """Create an instance of OpenIdConnectApplicationSettings from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of notes
        if self.notes:
            _dict['notes'] = self.notes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of notifications
        if self.notifications:
            _dict['notifications'] = self.notifications.to_dict()
        # override the default output from pydantic by calling `to_dict()` of oauth_client
        if self.oauth_client:
            _dict['oauthClient'] = self.oauth_client.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OpenIdConnectApplicationSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "identityStoreId": obj.get("identityStoreId"),
            "implicitAssignment": obj.get("implicitAssignment"),
            "inlineHookId": obj.get("inlineHookId"),
            "notes": ApplicationSettingsNotes.from_dict(obj["notes"]) if obj.get("notes") is not None else None,
            "notifications": ApplicationSettingsNotifications.from_dict(obj["notifications"]) if obj.get("notifications") is not None else None,
            "oauthClient": OpenIdConnectApplicationSettingsClient.from_dict(obj["oauthClient"]) if obj.get("oauthClient") is not None else None
        })
        return _obj


