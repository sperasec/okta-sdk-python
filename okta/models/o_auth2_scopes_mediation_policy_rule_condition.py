# coding: utf-8

"""
    Okta API

    Allows customers to easily access the Okta API  # noqa: E501

    OpenAPI spec version: 2.9.2
    Contact: devex-public@okta.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

import okta.models as models  # noqa
from okta.helpers import to_snake_case

class OAuth2ScopesMediationPolicyRuleCondition(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {}
    swagger_types['include'] = 'list[str]'

    attribute_map = {
        'include': 'include'
    }

    def __init__(self, config=None):
        if config is not None:
            config = {to_snake_case(key): value for key, value in config.items()}
        else:
            config = {}
        self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, include=None, **kwargs):  # noqa: E501
        """OAuth2ScopesMediationPolicyRuleCondition - a model defined in Swagger"""  # noqa: E501
        self._include = None
        self.discriminator = None
        if include is not None:
            if hasattr(models, self.swagger_types['include']):
                nested_class = getattr(models, self.swagger_types['include'])
                if isinstance(include, nested_class):
                    self.include = include
                elif isinstance(include, dict):
                    self.include = nested_class.from_kwargs(**include)
                else:
                    self.include = include
            else:
                self.include = include

    @property
    def include(self):
        """Gets the include of this OAuth2ScopesMediationPolicyRuleCondition.  # noqa: E501


        :return: The include of this OAuth2ScopesMediationPolicyRuleCondition.  # noqa: E501
        :rtype: list[str]
        """
        return self._include

    @include.setter
    def include(self, include):
        """Sets the include of this OAuth2ScopesMediationPolicyRuleCondition.


        :param include: The include of this OAuth2ScopesMediationPolicyRuleCondition.  # noqa: E501
        :type: list[str]
        """

        self._include = include

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(OAuth2ScopesMediationPolicyRuleCondition, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OAuth2ScopesMediationPolicyRuleCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other