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
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.links_self import LinksSelf
from typing import Optional, Set
from typing_extensions import Self

class ThreatInsightConfiguration(BaseModel):
    """
    ThreatInsightConfiguration
    """ # noqa: E501
    action: StrictStr = Field(description="Specifies how Okta responds to authentication requests from suspicious IP addresses")
    created: Optional[datetime] = Field(default=None, description="Timestamp when the ThreatInsight Configuration object was created")
    exclude_zones: Optional[List[StrictStr]] = Field(default=None, description="Accepts a list of [Network Zone](/openapi/okta-management/management/tag/NetworkZone/) IDs. IPs in the excluded network zones aren't logged or blocked. This ensures that traffic from known, trusted IPs isn't accidentally logged or blocked.", alias="excludeZones")
    last_updated: Optional[datetime] = Field(default=None, description="Timestamp when the ThreatInsight Configuration object was last updated", alias="lastUpdated")
    links: Optional[LinksSelf] = Field(default=None, alias="_links")
    __properties: ClassVar[List[str]] = ["action", "created", "excludeZones", "lastUpdated", "_links"]

    @field_validator('action')
    def action_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['none', 'audit', 'block']):
            raise ValueError("must be one of enum values ('none', 'audit', 'block')")
        return value

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
        """Create an instance of ThreatInsightConfiguration from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "created",
            "last_updated",
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
        """Create an instance of ThreatInsightConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "action": obj.get("action"),
            "created": obj.get("created"),
            "excludeZones": obj.get("excludeZones"),
            "lastUpdated": obj.get("lastUpdated"),
            "_links": LinksSelf.from_dict(obj["_links"]) if obj.get("_links") is not None else None
        })
        return _obj

