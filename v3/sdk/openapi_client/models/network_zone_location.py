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
from typing import Optional, Set
from typing_extensions import Self

class NetworkZoneLocation(BaseModel):
    """
    NetworkZoneLocation
    """ # noqa: E501
    country: Optional[StrictStr] = Field(default=None, description="Format of the country value: length 2 [ISO-3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code. Do not use continent codes as they are treated as generic codes for undesignated countries.")
    region: Optional[StrictStr] = Field(default=None, description="Format of the region value (optional): region code [ISO-3166-2](https://en.wikipedia.org/wiki/ISO_3166-2) appended to country code (`countryCode-regionCode`), or `null` if empty. Do not use continent codes as they are treated as generic codes for undesignated regions.")
    __properties: ClassVar[List[str]] = ["country", "region"]

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
        """Create an instance of NetworkZoneLocation from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NetworkZoneLocation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "country": obj.get("country"),
            "region": obj.get("region")
        })
        return _obj

