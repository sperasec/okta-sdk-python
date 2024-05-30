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
from openapi_client.models.application_credentials_signing_use import ApplicationCredentialsSigningUse
from typing import Optional, Set
from typing_extensions import Self

class ApplicationCredentialsSigning(BaseModel):
    """
    ApplicationCredentialsSigning
    """ # noqa: E501
    kid: Optional[StrictStr] = None
    last_rotated: Optional[datetime] = Field(default=None, alias="lastRotated")
    next_rotation: Optional[datetime] = Field(default=None, alias="nextRotation")
    rotation_mode: Optional[StrictStr] = Field(default=None, alias="rotationMode")
    use: Optional[ApplicationCredentialsSigningUse] = None
    __properties: ClassVar[List[str]] = ["kid", "lastRotated", "nextRotation", "rotationMode", "use"]

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
        """Create an instance of ApplicationCredentialsSigning from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "last_rotated",
            "next_rotation",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApplicationCredentialsSigning from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "kid": obj.get("kid"),
            "lastRotated": obj.get("lastRotated"),
            "nextRotation": obj.get("nextRotation"),
            "rotationMode": obj.get("rotationMode"),
            "use": obj.get("use")
        })
        return _obj


