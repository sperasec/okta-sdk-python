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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.links_self import LinksSelf
from openapi_client.models.session_authentication_method import SessionAuthenticationMethod
from openapi_client.models.session_identity_provider import SessionIdentityProvider
from openapi_client.models.session_status import SessionStatus
from typing import Optional, Set
from typing_extensions import Self

class Session(BaseModel):
    """
    Session
    """ # noqa: E501
    amr: Optional[List[SessionAuthenticationMethod]] = Field(default=None, description="Authentication method reference")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    expires_at: Optional[datetime] = Field(default=None, description="A timestamp when the Session expires", alias="expiresAt")
    id: Optional[StrictStr] = Field(default=None, description="A unique key for the Session")
    idp: Optional[SessionIdentityProvider] = None
    last_factor_verification: Optional[datetime] = Field(default=None, description="A timestamp when the user last performed multifactor authentication", alias="lastFactorVerification")
    last_password_verification: Optional[datetime] = Field(default=None, description="A timestamp when the user last performed the primary or step-up authentication with a password", alias="lastPasswordVerification")
    login: Optional[StrictStr] = Field(default=None, description="A unique identifier for the user (username)")
    status: Optional[SessionStatus] = None
    user_id: Optional[StrictStr] = Field(default=None, description="A unique key for the user", alias="userId")
    links: Optional[LinksSelf] = Field(default=None, alias="_links")
    __properties: ClassVar[List[str]] = ["amr", "createdAt", "expiresAt", "id", "idp", "lastFactorVerification", "lastPasswordVerification", "login", "status", "userId", "_links"]

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
        """Create an instance of Session from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "amr",
            "created_at",
            "expires_at",
            "id",
            "last_factor_verification",
            "last_password_verification",
            "login",
            "user_id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of idp
        if self.idp:
            _dict['idp'] = self.idp.to_dict()
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Session from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "amr": obj.get("amr"),
            "createdAt": obj.get("createdAt"),
            "expiresAt": obj.get("expiresAt"),
            "id": obj.get("id"),
            "idp": SessionIdentityProvider.from_dict(obj["idp"]) if obj.get("idp") is not None else None,
            "lastFactorVerification": obj.get("lastFactorVerification"),
            "lastPasswordVerification": obj.get("lastPasswordVerification"),
            "login": obj.get("login"),
            "status": obj.get("status"),
            "userId": obj.get("userId"),
            "_links": LinksSelf.from_dict(obj["_links"]) if obj.get("_links") is not None else None
        })
        return _obj


