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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.app_and_instance_policy_rule_condition import AppAndInstancePolicyRuleCondition
from openapi_client.models.platform_policy_rule_condition import PlatformPolicyRuleCondition
from openapi_client.models.policy_network_condition import PolicyNetworkCondition
from openapi_client.models.user_identifier_policy_rule_condition import UserIdentifierPolicyRuleCondition
from typing import Optional, Set
from typing_extensions import Self

class IdpDiscoveryPolicyRuleCondition(BaseModel):
    """
    IdpDiscoveryPolicyRuleCondition
    """ # noqa: E501
    app: Optional[AppAndInstancePolicyRuleCondition] = None
    network: Optional[PolicyNetworkCondition] = None
    user_identifier: Optional[UserIdentifierPolicyRuleCondition] = Field(default=None, alias="userIdentifier")
    platform: Optional[PlatformPolicyRuleCondition] = None
    __properties: ClassVar[List[str]] = ["app", "network", "userIdentifier", "platform"]

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
        """Create an instance of IdpDiscoveryPolicyRuleCondition from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of app
        if self.app:
            _dict['app'] = self.app.to_dict()
        # override the default output from pydantic by calling `to_dict()` of network
        if self.network:
            _dict['network'] = self.network.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user_identifier
        if self.user_identifier:
            _dict['userIdentifier'] = self.user_identifier.to_dict()
        # override the default output from pydantic by calling `to_dict()` of platform
        if self.platform:
            _dict['platform'] = self.platform.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IdpDiscoveryPolicyRuleCondition from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "app": AppAndInstancePolicyRuleCondition.from_dict(obj["app"]) if obj.get("app") is not None else None,
            "network": PolicyNetworkCondition.from_dict(obj["network"]) if obj.get("network") is not None else None,
            "userIdentifier": UserIdentifierPolicyRuleCondition.from_dict(obj["userIdentifier"]) if obj.get("userIdentifier") is not None else None,
            "platform": PlatformPolicyRuleCondition.from_dict(obj["platform"]) if obj.get("platform") is not None else None
        })
        return _obj


