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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.agent_type import AgentType
from openapi_client.models.agent_update_instance_status import AgentUpdateInstanceStatus
from openapi_client.models.links_self import LinksSelf
from openapi_client.models.operational_status import OperationalStatus
from typing import Optional, Set
from typing_extensions import Self

class Agent(BaseModel):
    """
    Agent details
    """ # noqa: E501
    id: Optional[StrictStr] = None
    is_hidden: Optional[StrictBool] = Field(default=None, alias="isHidden")
    is_latest_g_aed_version: Optional[StrictBool] = Field(default=None, alias="isLatestGAedVersion")
    last_connection: Optional[datetime] = Field(default=None, alias="lastConnection")
    name: Optional[StrictStr] = None
    operational_status: Optional[OperationalStatus] = Field(default=None, alias="operationalStatus")
    pool_id: Optional[StrictStr] = Field(default=None, alias="poolId")
    type: Optional[AgentType] = None
    update_message: Optional[StrictStr] = Field(default=None, alias="updateMessage")
    update_status: Optional[AgentUpdateInstanceStatus] = Field(default=None, alias="updateStatus")
    version: Optional[StrictStr] = None
    links: Optional[LinksSelf] = Field(default=None, alias="_links")
    __properties: ClassVar[List[str]] = ["id", "isHidden", "isLatestGAedVersion", "lastConnection", "name", "operationalStatus", "poolId", "type", "updateMessage", "updateStatus", "version", "_links"]

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
        """Create an instance of Agent from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Agent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "isHidden": obj.get("isHidden"),
            "isLatestGAedVersion": obj.get("isLatestGAedVersion"),
            "lastConnection": obj.get("lastConnection"),
            "name": obj.get("name"),
            "operationalStatus": obj.get("operationalStatus"),
            "poolId": obj.get("poolId"),
            "type": obj.get("type"),
            "updateMessage": obj.get("updateMessage"),
            "updateStatus": obj.get("updateStatus"),
            "version": obj.get("version"),
            "_links": LinksSelf.from_dict(obj["_links"]) if obj.get("_links") is not None else None
        })
        return _obj

