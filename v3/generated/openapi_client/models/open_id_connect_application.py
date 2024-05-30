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

from pydantic import ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.application import Application
from openapi_client.models.application_accessibility import ApplicationAccessibility
from openapi_client.models.application_licensing import ApplicationLicensing
from openapi_client.models.application_lifecycle_status import ApplicationLifecycleStatus
from openapi_client.models.application_links import ApplicationLinks
from openapi_client.models.application_sign_on_mode import ApplicationSignOnMode
from openapi_client.models.application_visibility import ApplicationVisibility
from openapi_client.models.o_auth_application_credentials import OAuthApplicationCredentials
from openapi_client.models.open_id_connect_application_settings import OpenIdConnectApplicationSettings
from typing import Optional, Set
from typing_extensions import Self

class OpenIdConnectApplication(Application):
    """
    OpenIdConnectApplication
    """ # noqa: E501
    credentials: Optional[OAuthApplicationCredentials] = None
    name: Optional[StrictStr] = 'oidc_client'
    settings: Optional[OpenIdConnectApplicationSettings] = None
    __properties: ClassVar[List[str]] = ["accessibility", "created", "features", "id", "label", "lastUpdated", "licensing", "profile", "signOnMode", "status", "visibility", "_embedded", "_links", "credentials", "name", "settings"]

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
        """Create an instance of OpenIdConnectApplication from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of accessibility
        if self.accessibility:
            _dict['accessibility'] = self.accessibility.to_dict()
        # override the default output from pydantic by calling `to_dict()` of licensing
        if self.licensing:
            _dict['licensing'] = self.licensing.to_dict()
        # override the default output from pydantic by calling `to_dict()` of visibility
        if self.visibility:
            _dict['visibility'] = self.visibility.to_dict()
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        # override the default output from pydantic by calling `to_dict()` of credentials
        if self.credentials:
            _dict['credentials'] = self.credentials.to_dict()
        # override the default output from pydantic by calling `to_dict()` of settings
        if self.settings:
            _dict['settings'] = self.settings.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OpenIdConnectApplication from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accessibility": ApplicationAccessibility.from_dict(obj["accessibility"]) if obj.get("accessibility") is not None else None,
            "created": obj.get("created"),
            "features": obj.get("features"),
            "id": obj.get("id"),
            "label": obj.get("label"),
            "lastUpdated": obj.get("lastUpdated"),
            "licensing": ApplicationLicensing.from_dict(obj["licensing"]) if obj.get("licensing") is not None else None,
            "profile": obj.get("profile"),
            "signOnMode": obj.get("signOnMode"),
            "status": obj.get("status"),
            "visibility": ApplicationVisibility.from_dict(obj["visibility"]) if obj.get("visibility") is not None else None,
            "_embedded": obj.get("_embedded"),
            "_links": ApplicationLinks.from_dict(obj["_links"]) if obj.get("_links") is not None else None,
            "credentials": OAuthApplicationCredentials.from_dict(obj["credentials"]) if obj.get("credentials") is not None else None,
            "name": obj.get("name") if obj.get("name") is not None else 'oidc_client',
            "settings": OpenIdConnectApplicationSettings.from_dict(obj["settings"]) if obj.get("settings") is not None else None
        })
        return _obj


