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
from openapi_client.models.lifecycle_status import LifecycleStatus
from openapi_client.models.links_self import LinksSelf
from openapi_client.models.o_auth2_claim_conditions import OAuth2ClaimConditions
from openapi_client.models.o_auth2_claim_group_filter_type import OAuth2ClaimGroupFilterType
from openapi_client.models.o_auth2_claim_type import OAuth2ClaimType
from openapi_client.models.o_auth2_claim_value_type import OAuth2ClaimValueType
from typing import Optional, Set
from typing_extensions import Self

class OAuth2Claim(BaseModel):
    """
    OAuth2Claim
    """ # noqa: E501
    always_include_in_token: Optional[StrictBool] = Field(default=None, alias="alwaysIncludeInToken")
    claim_type: Optional[OAuth2ClaimType] = Field(default=None, alias="claimType")
    conditions: Optional[OAuth2ClaimConditions] = None
    group_filter_type: Optional[OAuth2ClaimGroupFilterType] = None
    id: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    status: Optional[LifecycleStatus] = None
    system: Optional[StrictBool] = None
    value: Optional[StrictStr] = None
    value_type: Optional[OAuth2ClaimValueType] = Field(default=None, alias="valueType")
    links: Optional[LinksSelf] = Field(default=None, alias="_links")
    __properties: ClassVar[List[str]] = ["alwaysIncludeInToken", "claimType", "conditions", "group_filter_type", "id", "name", "status", "system", "value", "valueType", "_links"]

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
        """Create an instance of OAuth2Claim from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of conditions
        if self.conditions:
            _dict['conditions'] = self.conditions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OAuth2Claim from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "alwaysIncludeInToken": obj.get("alwaysIncludeInToken"),
            "claimType": obj.get("claimType"),
            "conditions": OAuth2ClaimConditions.from_dict(obj["conditions"]) if obj.get("conditions") is not None else None,
            "group_filter_type": obj.get("group_filter_type"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "status": obj.get("status"),
            "system": obj.get("system"),
            "value": obj.get("value"),
            "valueType": obj.get("valueType"),
            "_links": LinksSelf.from_dict(obj["_links"]) if obj.get("_links") is not None else None
        })
        return _obj

