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
from openapi_client.models.lifecycle_status import LifecycleStatus
from openapi_client.models.policy_rule import PolicyRule
from openapi_client.models.policy_rule_conditions import PolicyRuleConditions
from openapi_client.models.policy_rule_type import PolicyRuleType
from openapi_client.models.profile_enrollment_policy_rule_actions import ProfileEnrollmentPolicyRuleActions
from typing import Optional, Set
from typing_extensions import Self

class ProfileEnrollmentPolicyRule(PolicyRule):
    """
    ProfileEnrollmentPolicyRule
    """ # noqa: E501
    actions: Optional[ProfileEnrollmentPolicyRuleActions] = None
    conditions: Optional[PolicyRuleConditions] = None
    __properties: ClassVar[List[str]] = ["created", "id", "lastUpdated", "name", "priority", "status", "system", "type", "actions", "conditions"]

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
        """Create an instance of ProfileEnrollmentPolicyRule from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of actions
        if self.actions:
            _dict['actions'] = self.actions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of conditions
        if self.conditions:
            _dict['conditions'] = self.conditions.to_dict()
        # set to None if created (nullable) is None
        # and model_fields_set contains the field
        if self.created is None and "created" in self.model_fields_set:
            _dict['created'] = None

        # set to None if last_updated (nullable) is None
        # and model_fields_set contains the field
        if self.last_updated is None and "last_updated" in self.model_fields_set:
            _dict['lastUpdated'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProfileEnrollmentPolicyRule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created": obj.get("created"),
            "id": obj.get("id"),
            "lastUpdated": obj.get("lastUpdated"),
            "name": obj.get("name"),
            "priority": obj.get("priority"),
            "status": obj.get("status"),
            "system": obj.get("system") if obj.get("system") is not None else False,
            "type": obj.get("type"),
            "actions": ProfileEnrollmentPolicyRuleActions.from_dict(obj["actions"]) if obj.get("actions") is not None else None,
            "conditions": PolicyRuleConditions.from_dict(obj["conditions"]) if obj.get("conditions") is not None else None
        })
        return _obj

