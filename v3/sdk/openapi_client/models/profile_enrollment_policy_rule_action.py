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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.pre_registration_inline_hook import PreRegistrationInlineHook
from openapi_client.models.profile_enrollment_policy_rule_activation_requirement import ProfileEnrollmentPolicyRuleActivationRequirement
from openapi_client.models.profile_enrollment_policy_rule_profile_attribute import ProfileEnrollmentPolicyRuleProfileAttribute
from typing import Optional, Set
from typing_extensions import Self

class ProfileEnrollmentPolicyRuleAction(BaseModel):
    """
    ProfileEnrollmentPolicyRuleAction
    """ # noqa: E501
    access: Optional[StrictStr] = None
    activation_requirements: Optional[ProfileEnrollmentPolicyRuleActivationRequirement] = Field(default=None, alias="activationRequirements")
    pre_registration_inline_hooks: Optional[List[PreRegistrationInlineHook]] = Field(default=None, alias="preRegistrationInlineHooks")
    profile_attributes: Optional[List[ProfileEnrollmentPolicyRuleProfileAttribute]] = Field(default=None, alias="profileAttributes")
    target_group_ids: Optional[List[StrictStr]] = Field(default=None, alias="targetGroupIds")
    unknown_user_action: Optional[StrictStr] = Field(default=None, alias="unknownUserAction")
    progressive_profiling_action: Optional[StrictStr] = Field(default=None, alias="progressiveProfilingAction")
    __properties: ClassVar[List[str]] = ["access", "activationRequirements", "preRegistrationInlineHooks", "profileAttributes", "targetGroupIds", "unknownUserAction", "progressiveProfilingAction"]

    @field_validator('unknown_user_action')
    def unknown_user_action_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['DENY', 'REGISTER']):
            raise ValueError("must be one of enum values ('DENY', 'REGISTER')")
        return value

    @field_validator('progressive_profiling_action')
    def progressive_profiling_action_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['ENABLED', 'DISABLED']):
            raise ValueError("must be one of enum values ('ENABLED', 'DISABLED')")
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
        """Create an instance of ProfileEnrollmentPolicyRuleAction from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of activation_requirements
        if self.activation_requirements:
            _dict['activationRequirements'] = self.activation_requirements.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in pre_registration_inline_hooks (list)
        _items = []
        if self.pre_registration_inline_hooks:
            for _item in self.pre_registration_inline_hooks:
                if _item:
                    _items.append(_item.to_dict())
            _dict['preRegistrationInlineHooks'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in profile_attributes (list)
        _items = []
        if self.profile_attributes:
            for _item in self.profile_attributes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['profileAttributes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProfileEnrollmentPolicyRuleAction from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "access": obj.get("access"),
            "activationRequirements": ProfileEnrollmentPolicyRuleActivationRequirement.from_dict(obj["activationRequirements"]) if obj.get("activationRequirements") is not None else None,
            "preRegistrationInlineHooks": [PreRegistrationInlineHook.from_dict(_item) for _item in obj["preRegistrationInlineHooks"]] if obj.get("preRegistrationInlineHooks") is not None else None,
            "profileAttributes": [ProfileEnrollmentPolicyRuleProfileAttribute.from_dict(_item) for _item in obj["profileAttributes"]] if obj.get("profileAttributes") is not None else None,
            "targetGroupIds": obj.get("targetGroupIds"),
            "unknownUserAction": obj.get("unknownUserAction"),
            "progressiveProfilingAction": obj.get("progressiveProfilingAction")
        })
        return _obj

