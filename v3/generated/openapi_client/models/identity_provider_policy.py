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
from openapi_client.models.policy_account_link import PolicyAccountLink
from openapi_client.models.policy_subject import PolicySubject
from openapi_client.models.provisioning import Provisioning
from typing import Optional, Set
from typing_extensions import Self

class IdentityProviderPolicy(BaseModel):
    """
    IdentityProviderPolicy
    """ # noqa: E501
    account_link: Optional[PolicyAccountLink] = Field(default=None, alias="accountLink")
    map_amr_claims: Optional[StrictBool] = Field(default=False, description="Enable mapping AMR from IdP to Okta to downstream apps", alias="mapAMRClaims")
    max_clock_skew: Optional[StrictInt] = Field(default=None, alias="maxClockSkew")
    provisioning: Optional[Provisioning] = None
    subject: Optional[PolicySubject] = None
    __properties: ClassVar[List[str]] = ["accountLink", "mapAMRClaims", "maxClockSkew", "provisioning", "subject"]

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
        """Create an instance of IdentityProviderPolicy from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of account_link
        if self.account_link:
            _dict['accountLink'] = self.account_link.to_dict()
        # override the default output from pydantic by calling `to_dict()` of provisioning
        if self.provisioning:
            _dict['provisioning'] = self.provisioning.to_dict()
        # override the default output from pydantic by calling `to_dict()` of subject
        if self.subject:
            _dict['subject'] = self.subject.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IdentityProviderPolicy from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accountLink": PolicyAccountLink.from_dict(obj["accountLink"]) if obj.get("accountLink") is not None else None,
            "mapAMRClaims": obj.get("mapAMRClaims") if obj.get("mapAMRClaims") is not None else False,
            "maxClockSkew": obj.get("maxClockSkew"),
            "provisioning": Provisioning.from_dict(obj["provisioning"]) if obj.get("provisioning") is not None else None,
            "subject": PolicySubject.from_dict(obj["subject"]) if obj.get("subject") is not None else None
        })
        return _obj


