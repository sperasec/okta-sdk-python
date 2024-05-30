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
from openapi_client.models.api_service_integration_links import APIServiceIntegrationLinks
from typing import Optional, Set
from typing_extensions import Self

class PostAPIServiceIntegrationInstance(BaseModel):
    """
    PostAPIServiceIntegrationInstance
    """ # noqa: E501
    config_guide_url: Optional[StrictStr] = Field(default=None, description="The URL to the API service integration configuration guide", alias="configGuideUrl")
    created_at: Optional[StrictStr] = Field(default=None, description="Timestamp when the API Service Integration instance was created", alias="createdAt")
    created_by: Optional[StrictStr] = Field(default=None, description="The user ID of the API Service Integration instance creator", alias="createdBy")
    granted_scopes: Optional[List[StrictStr]] = Field(default=None, description="The list of Okta management scopes granted to the API Service Integration instance. See [Okta management OAuth 2.0 scopes](/oauth2/#okta-admin-management).", alias="grantedScopes")
    id: Optional[StrictStr] = Field(default=None, description="The ID of the API Service Integration instance")
    name: Optional[StrictStr] = Field(default=None, description="The name of the API service integration that corresponds with the `type` property. This is the full name of the API service integration listed in the Okta Integration Network (OIN) catalog.")
    type: Optional[StrictStr] = Field(default=None, description="The type of the API service integration. This string is an underscore-concatenated, lowercased API service integration name. For example, `my_api_log_integration`.")
    links: Optional[APIServiceIntegrationLinks] = Field(default=None, alias="_links")
    client_secret: Optional[StrictStr] = Field(default=None, description="The client secret for the API Service Integration instance. This property is only returned in a POST response.", alias="clientSecret")
    __properties: ClassVar[List[str]] = ["configGuideUrl", "createdAt", "createdBy", "grantedScopes", "id", "name", "type", "_links", "clientSecret"]

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
        """Create an instance of PostAPIServiceIntegrationInstance from a JSON string"""
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
            "config_guide_url",
            "created_at",
            "created_by",
            "id",
            "name",
            "client_secret",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PostAPIServiceIntegrationInstance from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "configGuideUrl": obj.get("configGuideUrl"),
            "createdAt": obj.get("createdAt"),
            "createdBy": obj.get("createdBy"),
            "grantedScopes": obj.get("grantedScopes"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "type": obj.get("type"),
            "_links": APIServiceIntegrationLinks.from_dict(obj["_links"]) if obj.get("_links") is not None else None,
            "clientSecret": obj.get("clientSecret")
        })
        return _obj


