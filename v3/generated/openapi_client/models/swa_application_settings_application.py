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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class SwaApplicationSettingsApplication(BaseModel):
    """
    SwaApplicationSettingsApplication
    """ # noqa: E501
    button_field: Optional[StrictStr] = Field(default=None, alias="buttonField")
    button_selector: Optional[StrictStr] = Field(default=None, alias="buttonSelector")
    checkbox: Optional[StrictStr] = None
    extra_field_selector: Optional[StrictStr] = Field(default=None, alias="extraFieldSelector")
    extra_field_value: Optional[StrictStr] = Field(default=None, alias="extraFieldValue")
    login_url_regex: Optional[StrictStr] = Field(default=None, alias="loginUrlRegex")
    password_field: Optional[StrictStr] = Field(default=None, alias="passwordField")
    password_selector: Optional[StrictStr] = Field(default=None, alias="passwordSelector")
    redirect_url: Optional[StrictStr] = Field(default=None, alias="redirectUrl")
    target_url: Optional[StrictStr] = Field(default=None, alias="targetURL")
    url: Optional[StrictStr] = None
    username_field: Optional[StrictStr] = Field(default=None, alias="usernameField")
    user_name_selector: Optional[StrictStr] = Field(default=None, alias="userNameSelector")
    __properties: ClassVar[List[str]] = ["buttonField", "buttonSelector", "checkbox", "extraFieldSelector", "extraFieldValue", "loginUrlRegex", "passwordField", "passwordSelector", "redirectUrl", "targetURL", "url", "usernameField", "userNameSelector"]

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
        """Create an instance of SwaApplicationSettingsApplication from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SwaApplicationSettingsApplication from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "buttonField": obj.get("buttonField"),
            "buttonSelector": obj.get("buttonSelector"),
            "checkbox": obj.get("checkbox"),
            "extraFieldSelector": obj.get("extraFieldSelector"),
            "extraFieldValue": obj.get("extraFieldValue"),
            "loginUrlRegex": obj.get("loginUrlRegex"),
            "passwordField": obj.get("passwordField"),
            "passwordSelector": obj.get("passwordSelector"),
            "redirectUrl": obj.get("redirectUrl"),
            "targetURL": obj.get("targetURL"),
            "url": obj.get("url"),
            "usernameField": obj.get("usernameField"),
            "userNameSelector": obj.get("userNameSelector")
        })
        return _obj


