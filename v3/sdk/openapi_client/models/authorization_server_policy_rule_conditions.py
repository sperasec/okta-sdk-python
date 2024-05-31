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
from openapi_client.models.app_instance_policy_rule_condition import AppInstancePolicyRuleCondition
from openapi_client.models.before_scheduled_action_policy_rule_condition import BeforeScheduledActionPolicyRuleCondition
from openapi_client.models.client_policy_condition import ClientPolicyCondition
from openapi_client.models.context_policy_rule_condition import ContextPolicyRuleCondition
from openapi_client.models.device_policy_rule_condition import DevicePolicyRuleCondition
from openapi_client.models.grant_type_policy_rule_condition import GrantTypePolicyRuleCondition
from openapi_client.models.group_policy_rule_condition import GroupPolicyRuleCondition
from openapi_client.models.identity_provider_policy_rule_condition import IdentityProviderPolicyRuleCondition
from openapi_client.models.mdm_enrollment_policy_rule_condition import MDMEnrollmentPolicyRuleCondition
from openapi_client.models.o_auth2_scopes_mediation_policy_rule_condition import OAuth2ScopesMediationPolicyRuleCondition
from openapi_client.models.password_policy_authentication_provider_condition import PasswordPolicyAuthenticationProviderCondition
from openapi_client.models.platform_policy_rule_condition import PlatformPolicyRuleCondition
from openapi_client.models.policy_network_condition import PolicyNetworkCondition
from openapi_client.models.policy_people_condition import PolicyPeopleCondition
from openapi_client.models.policy_rule_auth_context_condition import PolicyRuleAuthContextCondition
from openapi_client.models.risk_policy_rule_condition import RiskPolicyRuleCondition
from openapi_client.models.risk_score_policy_rule_condition import RiskScorePolicyRuleCondition
from openapi_client.models.user_identifier_policy_rule_condition import UserIdentifierPolicyRuleCondition
from openapi_client.models.user_policy_rule_condition import UserPolicyRuleCondition
from openapi_client.models.user_status_policy_rule_condition import UserStatusPolicyRuleCondition
from typing import Optional, Set
from typing_extensions import Self

class AuthorizationServerPolicyRuleConditions(BaseModel):
    """
    AuthorizationServerPolicyRuleConditions
    """ # noqa: E501
    app: Optional[AppAndInstancePolicyRuleCondition] = None
    apps: Optional[AppInstancePolicyRuleCondition] = None
    auth_context: Optional[PolicyRuleAuthContextCondition] = Field(default=None, alias="authContext")
    auth_provider: Optional[PasswordPolicyAuthenticationProviderCondition] = Field(default=None, alias="authProvider")
    before_scheduled_action: Optional[BeforeScheduledActionPolicyRuleCondition] = Field(default=None, alias="beforeScheduledAction")
    clients: Optional[ClientPolicyCondition] = None
    context: Optional[ContextPolicyRuleCondition] = None
    device: Optional[DevicePolicyRuleCondition] = None
    grant_types: Optional[GrantTypePolicyRuleCondition] = Field(default=None, alias="grantTypes")
    groups: Optional[GroupPolicyRuleCondition] = None
    identity_provider: Optional[IdentityProviderPolicyRuleCondition] = Field(default=None, alias="identityProvider")
    mdm_enrollment: Optional[MDMEnrollmentPolicyRuleCondition] = Field(default=None, alias="mdmEnrollment")
    network: Optional[PolicyNetworkCondition] = None
    people: Optional[PolicyPeopleCondition] = None
    platform: Optional[PlatformPolicyRuleCondition] = None
    risk: Optional[RiskPolicyRuleCondition] = None
    risk_score: Optional[RiskScorePolicyRuleCondition] = Field(default=None, alias="riskScore")
    scopes: Optional[OAuth2ScopesMediationPolicyRuleCondition] = None
    user_identifier: Optional[UserIdentifierPolicyRuleCondition] = Field(default=None, alias="userIdentifier")
    users: Optional[UserPolicyRuleCondition] = None
    user_status: Optional[UserStatusPolicyRuleCondition] = Field(default=None, alias="userStatus")
    __properties: ClassVar[List[str]] = ["app", "apps", "authContext", "authProvider", "beforeScheduledAction", "clients", "context", "device", "grantTypes", "groups", "identityProvider", "mdmEnrollment", "network", "people", "platform", "risk", "riskScore", "scopes", "userIdentifier", "users", "userStatus"]

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
        """Create an instance of AuthorizationServerPolicyRuleConditions from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of apps
        if self.apps:
            _dict['apps'] = self.apps.to_dict()
        # override the default output from pydantic by calling `to_dict()` of auth_context
        if self.auth_context:
            _dict['authContext'] = self.auth_context.to_dict()
        # override the default output from pydantic by calling `to_dict()` of auth_provider
        if self.auth_provider:
            _dict['authProvider'] = self.auth_provider.to_dict()
        # override the default output from pydantic by calling `to_dict()` of before_scheduled_action
        if self.before_scheduled_action:
            _dict['beforeScheduledAction'] = self.before_scheduled_action.to_dict()
        # override the default output from pydantic by calling `to_dict()` of clients
        if self.clients:
            _dict['clients'] = self.clients.to_dict()
        # override the default output from pydantic by calling `to_dict()` of context
        if self.context:
            _dict['context'] = self.context.to_dict()
        # override the default output from pydantic by calling `to_dict()` of device
        if self.device:
            _dict['device'] = self.device.to_dict()
        # override the default output from pydantic by calling `to_dict()` of grant_types
        if self.grant_types:
            _dict['grantTypes'] = self.grant_types.to_dict()
        # override the default output from pydantic by calling `to_dict()` of groups
        if self.groups:
            _dict['groups'] = self.groups.to_dict()
        # override the default output from pydantic by calling `to_dict()` of identity_provider
        if self.identity_provider:
            _dict['identityProvider'] = self.identity_provider.to_dict()
        # override the default output from pydantic by calling `to_dict()` of mdm_enrollment
        if self.mdm_enrollment:
            _dict['mdmEnrollment'] = self.mdm_enrollment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of network
        if self.network:
            _dict['network'] = self.network.to_dict()
        # override the default output from pydantic by calling `to_dict()` of people
        if self.people:
            _dict['people'] = self.people.to_dict()
        # override the default output from pydantic by calling `to_dict()` of platform
        if self.platform:
            _dict['platform'] = self.platform.to_dict()
        # override the default output from pydantic by calling `to_dict()` of risk
        if self.risk:
            _dict['risk'] = self.risk.to_dict()
        # override the default output from pydantic by calling `to_dict()` of risk_score
        if self.risk_score:
            _dict['riskScore'] = self.risk_score.to_dict()
        # override the default output from pydantic by calling `to_dict()` of scopes
        if self.scopes:
            _dict['scopes'] = self.scopes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user_identifier
        if self.user_identifier:
            _dict['userIdentifier'] = self.user_identifier.to_dict()
        # override the default output from pydantic by calling `to_dict()` of users
        if self.users:
            _dict['users'] = self.users.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user_status
        if self.user_status:
            _dict['userStatus'] = self.user_status.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AuthorizationServerPolicyRuleConditions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "app": AppAndInstancePolicyRuleCondition.from_dict(obj["app"]) if obj.get("app") is not None else None,
            "apps": AppInstancePolicyRuleCondition.from_dict(obj["apps"]) if obj.get("apps") is not None else None,
            "authContext": PolicyRuleAuthContextCondition.from_dict(obj["authContext"]) if obj.get("authContext") is not None else None,
            "authProvider": PasswordPolicyAuthenticationProviderCondition.from_dict(obj["authProvider"]) if obj.get("authProvider") is not None else None,
            "beforeScheduledAction": BeforeScheduledActionPolicyRuleCondition.from_dict(obj["beforeScheduledAction"]) if obj.get("beforeScheduledAction") is not None else None,
            "clients": ClientPolicyCondition.from_dict(obj["clients"]) if obj.get("clients") is not None else None,
            "context": ContextPolicyRuleCondition.from_dict(obj["context"]) if obj.get("context") is not None else None,
            "device": DevicePolicyRuleCondition.from_dict(obj["device"]) if obj.get("device") is not None else None,
            "grantTypes": GrantTypePolicyRuleCondition.from_dict(obj["grantTypes"]) if obj.get("grantTypes") is not None else None,
            "groups": GroupPolicyRuleCondition.from_dict(obj["groups"]) if obj.get("groups") is not None else None,
            "identityProvider": IdentityProviderPolicyRuleCondition.from_dict(obj["identityProvider"]) if obj.get("identityProvider") is not None else None,
            "mdmEnrollment": MDMEnrollmentPolicyRuleCondition.from_dict(obj["mdmEnrollment"]) if obj.get("mdmEnrollment") is not None else None,
            "network": PolicyNetworkCondition.from_dict(obj["network"]) if obj.get("network") is not None else None,
            "people": PolicyPeopleCondition.from_dict(obj["people"]) if obj.get("people") is not None else None,
            "platform": PlatformPolicyRuleCondition.from_dict(obj["platform"]) if obj.get("platform") is not None else None,
            "risk": RiskPolicyRuleCondition.from_dict(obj["risk"]) if obj.get("risk") is not None else None,
            "riskScore": RiskScorePolicyRuleCondition.from_dict(obj["riskScore"]) if obj.get("riskScore") is not None else None,
            "scopes": OAuth2ScopesMediationPolicyRuleCondition.from_dict(obj["scopes"]) if obj.get("scopes") is not None else None,
            "userIdentifier": UserIdentifierPolicyRuleCondition.from_dict(obj["userIdentifier"]) if obj.get("userIdentifier") is not None else None,
            "users": UserPolicyRuleCondition.from_dict(obj["users"]) if obj.get("users") is not None else None,
            "userStatus": UserStatusPolicyRuleCondition.from_dict(obj["userStatus"]) if obj.get("userStatus") is not None else None
        })
        return _obj

