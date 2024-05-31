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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.okta_sign_on_policy_factor_prompt_mode import OktaSignOnPolicyFactorPromptMode
from openapi_client.models.okta_sign_on_policy_rule_signon_session_actions import OktaSignOnPolicyRuleSignonSessionActions
from openapi_client.models.policy_access import PolicyAccess
from typing import Optional, Set
from typing_extensions import Self

class OktaSignOnPolicyRuleSignonActions(BaseModel):
    """
    OktaSignOnPolicyRuleSignonActions
    """ # noqa: E501
    access: Optional[PolicyAccess] = None
    factor_lifetime: Optional[StrictInt] = Field(default=None, alias="factorLifetime")
    factor_prompt_mode: Optional[OktaSignOnPolicyFactorPromptMode] = Field(default=None, alias="factorPromptMode")
    remember_device_by_default: Optional[StrictBool] = Field(default=False, alias="rememberDeviceByDefault")
    require_factor: Optional[StrictBool] = Field(default=False, alias="requireFactor")
    session: Optional[OktaSignOnPolicyRuleSignonSessionActions] = None
    __properties: ClassVar[List[str]] = ["access", "factorLifetime", "factorPromptMode", "rememberDeviceByDefault", "requireFactor", "session"]

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
        """Create an instance of OktaSignOnPolicyRuleSignonActions from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of session
        if self.session:
            _dict['session'] = self.session.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OktaSignOnPolicyRuleSignonActions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "access": obj.get("access"),
            "factorLifetime": obj.get("factorLifetime"),
            "factorPromptMode": obj.get("factorPromptMode"),
            "rememberDeviceByDefault": obj.get("rememberDeviceByDefault") if obj.get("rememberDeviceByDefault") is not None else False,
            "requireFactor": obj.get("requireFactor") if obj.get("requireFactor") is not None else False,
            "session": OktaSignOnPolicyRuleSignonSessionActions.from_dict(obj["session"]) if obj.get("session") is not None else None
        })
        return _obj

