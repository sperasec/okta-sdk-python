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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.chrome_browser_version import ChromeBrowserVersion
from openapi_client.models.key_trust_level_browser_key import KeyTrustLevelBrowserKey
from openapi_client.models.os_version import OSVersion
from openapi_client.models.password_protection_warning_trigger import PasswordProtectionWarningTrigger
from openapi_client.models.safe_browsing_protection_level import SafeBrowsingProtectionLevel
from typing import Optional, Set
from typing_extensions import Self

class DTCWindows(BaseModel):
    """
    Google Chrome Device Trust Connector provider
    """ # noqa: E501
    browser_version: Optional[ChromeBrowserVersion] = Field(default=None, alias="browserVersion")
    built_in_dns_client_enabled: Optional[StrictBool] = Field(default=None, description="Indicates if a software stack is used to communicate with the DNS server", alias="builtInDnsClientEnabled")
    chrome_remote_desktop_app_blocked: Optional[StrictBool] = Field(default=None, description="Indicates whether access to the Chrome Remote Desktop application is blocked through a policy", alias="chromeRemoteDesktopAppBlocked")
    crowd_strike_agent_id: Optional[StrictStr] = Field(default=None, description="Agent ID of an installed CrowdStrike agent", alias="crowdStrikeAgentId")
    crowd_strike_customer_id: Optional[StrictStr] = Field(default=None, description="Customer ID of an installed CrowdStrike agent", alias="crowdStrikeCustomerId")
    device_enrollment_domain: Optional[StrictStr] = Field(default=None, description="Enrollment domain of the customer that is currently managing the device", alias="deviceEnrollmentDomain")
    disk_enrypted: Optional[StrictBool] = Field(default=None, description="Indicates whether the main disk is encrypted", alias="diskEnrypted")
    key_trust_level: Optional[KeyTrustLevelBrowserKey] = Field(default=None, alias="keyTrustLevel")
    os_firewall: Optional[StrictBool] = Field(default=None, description="Indicates whether a firewall is enabled at the OS-level on the device", alias="osFirewall")
    os_version: Optional[OSVersion] = Field(default=None, alias="osVersion")
    password_protection_warning_trigger: Optional[PasswordProtectionWarningTrigger] = Field(default=None, alias="passwordProtectionWarningTrigger")
    realtime_url_check_mode: Optional[StrictBool] = Field(default=None, description="Indicates whether enterprise-grade (custom) unsafe URL scanning is enabled", alias="realtimeUrlCheckMode")
    safe_browsing_protection_level: Optional[SafeBrowsingProtectionLevel] = Field(default=None, alias="safeBrowsingProtectionLevel")
    screen_lock_secured: Optional[StrictBool] = Field(default=None, description="Indicates whether the device is password-protected", alias="screenLockSecured")
    secure_boot_enabled: Optional[StrictBool] = Field(default=None, description="Indicates whether the device's startup software has its Secure Boot feature enabled", alias="secureBootEnabled")
    site_isolation_enabled: Optional[StrictBool] = Field(default=None, description="Indicates whether the Site Isolation (also known as **Site Per Process**) setting is enabled", alias="siteIsolationEnabled")
    third_party_blocking_enabled: Optional[StrictBool] = Field(default=None, description="Indicates whether Chrome is blocking third-party software injection", alias="thirdPartyBlockingEnabled")
    windows_machine_domain: Optional[StrictStr] = Field(default=None, description="Windows domain that the current machine has joined", alias="windowsMachineDomain")
    windows_user_domain: Optional[StrictStr] = Field(default=None, description="Windows domain for the current OS user", alias="windowsUserDomain")
    __properties: ClassVar[List[str]] = ["browserVersion", "builtInDnsClientEnabled", "chromeRemoteDesktopAppBlocked", "crowdStrikeAgentId", "crowdStrikeCustomerId", "deviceEnrollmentDomain", "diskEnrypted", "keyTrustLevel", "osFirewall", "osVersion", "passwordProtectionWarningTrigger", "realtimeUrlCheckMode", "safeBrowsingProtectionLevel", "screenLockSecured", "secureBootEnabled", "siteIsolationEnabled", "thirdPartyBlockingEnabled", "windowsMachineDomain", "windowsUserDomain"]

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
        """Create an instance of DTCWindows from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of browser_version
        if self.browser_version:
            _dict['browserVersion'] = self.browser_version.to_dict()
        # override the default output from pydantic by calling `to_dict()` of os_version
        if self.os_version:
            _dict['osVersion'] = self.os_version.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DTCWindows from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "browserVersion": ChromeBrowserVersion.from_dict(obj["browserVersion"]) if obj.get("browserVersion") is not None else None,
            "builtInDnsClientEnabled": obj.get("builtInDnsClientEnabled"),
            "chromeRemoteDesktopAppBlocked": obj.get("chromeRemoteDesktopAppBlocked"),
            "crowdStrikeAgentId": obj.get("crowdStrikeAgentId"),
            "crowdStrikeCustomerId": obj.get("crowdStrikeCustomerId"),
            "deviceEnrollmentDomain": obj.get("deviceEnrollmentDomain"),
            "diskEnrypted": obj.get("diskEnrypted"),
            "keyTrustLevel": obj.get("keyTrustLevel"),
            "osFirewall": obj.get("osFirewall"),
            "osVersion": OSVersion.from_dict(obj["osVersion"]) if obj.get("osVersion") is not None else None,
            "passwordProtectionWarningTrigger": obj.get("passwordProtectionWarningTrigger"),
            "realtimeUrlCheckMode": obj.get("realtimeUrlCheckMode"),
            "safeBrowsingProtectionLevel": obj.get("safeBrowsingProtectionLevel"),
            "screenLockSecured": obj.get("screenLockSecured"),
            "secureBootEnabled": obj.get("secureBootEnabled"),
            "siteIsolationEnabled": obj.get("siteIsolationEnabled"),
            "thirdPartyBlockingEnabled": obj.get("thirdPartyBlockingEnabled"),
            "windowsMachineDomain": obj.get("windowsMachineDomain"),
            "windowsUserDomain": obj.get("windowsUserDomain")
        })
        return _obj


