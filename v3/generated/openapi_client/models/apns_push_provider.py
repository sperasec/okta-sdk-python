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

from pydantic import ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.apns_configuration import APNSConfiguration
from openapi_client.models.links_self import LinksSelf
from openapi_client.models.provider_type import ProviderType
from openapi_client.models.push_provider import PushProvider
from typing import Optional, Set
from typing_extensions import Self

class APNSPushProvider(PushProvider):
    """
    APNSPushProvider
    """ # noqa: E501
    configuration: Optional[APNSConfiguration] = None
    __properties: ClassVar[List[str]] = ["id", "lastUpdatedDate", "name", "providerType", "_links", "configuration"]

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
        """Create an instance of APNSPushProvider from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        # override the default output from pydantic by calling `to_dict()` of configuration
        if self.configuration:
            _dict['configuration'] = self.configuration.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of APNSPushProvider from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "lastUpdatedDate": obj.get("lastUpdatedDate"),
            "name": obj.get("name"),
            "providerType": obj.get("providerType"),
            "_links": LinksSelf.from_dict(obj["_links"]) if obj.get("_links") is not None else None,
            "configuration": APNSConfiguration.from_dict(obj["configuration"]) if obj.get("configuration") is not None else None
        })
        return _obj


