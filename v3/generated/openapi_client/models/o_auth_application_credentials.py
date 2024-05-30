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
from openapi_client.models.application_credentials_o_auth_client import ApplicationCredentialsOAuthClient
from openapi_client.models.application_credentials_signing import ApplicationCredentialsSigning
from openapi_client.models.application_credentials_username_template import ApplicationCredentialsUsernameTemplate
from typing import Optional, Set
from typing_extensions import Self

class OAuthApplicationCredentials(BaseModel):
    """
    OAuthApplicationCredentials
    """ # noqa: E501
    signing: Optional[ApplicationCredentialsSigning] = None
    user_name_template: Optional[ApplicationCredentialsUsernameTemplate] = Field(default=None, alias="userNameTemplate")
    oauth_client: Optional[ApplicationCredentialsOAuthClient] = Field(default=None, alias="oauthClient")
    __properties: ClassVar[List[str]] = ["signing", "userNameTemplate", "oauthClient"]

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
        """Create an instance of OAuthApplicationCredentials from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of signing
        if self.signing:
            _dict['signing'] = self.signing.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user_name_template
        if self.user_name_template:
            _dict['userNameTemplate'] = self.user_name_template.to_dict()
        # override the default output from pydantic by calling `to_dict()` of oauth_client
        if self.oauth_client:
            _dict['oauthClient'] = self.oauth_client.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OAuthApplicationCredentials from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "signing": ApplicationCredentialsSigning.from_dict(obj["signing"]) if obj.get("signing") is not None else None,
            "userNameTemplate": ApplicationCredentialsUsernameTemplate.from_dict(obj["userNameTemplate"]) if obj.get("userNameTemplate") is not None else None,
            "oauthClient": ApplicationCredentialsOAuthClient.from_dict(obj["oauthClient"]) if obj.get("oauthClient") is not None else None
        })
        return _obj


