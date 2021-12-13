# coding: utf-8

"""
    Okta API

    Allows customers to easily access the Okta API  # noqa: E501

    OpenAPI spec version: 2.7.0
    Contact: devex-public@okta.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ProfileMappingProperty(object):
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
    swagger_types = {
        'expression': 'str',
        'push_status': 'ProfileMappingPropertyPushStatus'
    }

    attribute_map = {
        'expression': 'expression',
        'push_status': 'pushStatus'
    }

    def __init__(self, config=None):
        if config is not None:
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, expression=None, push_status=None):  # noqa: E501
        """ProfileMappingProperty - a model defined in Swagger"""  # noqa: E501
        self._expression = None
        self._push_status = None
        self.discriminator = None
        if expression is not None:
            self.expression = expression
        if push_status is not None:
            self.push_status = push_status

    @property
    def expression(self):
        """Gets the expression of this ProfileMappingProperty.  # noqa: E501


        :return: The expression of this ProfileMappingProperty.  # noqa: E501
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """Sets the expression of this ProfileMappingProperty.


        :param expression: The expression of this ProfileMappingProperty.  # noqa: E501
        :type: str
        """

        self._expression = expression

    @property
    def push_status(self):
        """Gets the push_status of this ProfileMappingProperty.  # noqa: E501


        :return: The push_status of this ProfileMappingProperty.  # noqa: E501
        :rtype: ProfileMappingPropertyPushStatus
        """
        return self._push_status

    @push_status.setter
    def push_status(self, push_status):
        """Sets the push_status of this ProfileMappingProperty.


        :param push_status: The push_status of this ProfileMappingProperty.  # noqa: E501
        :type: ProfileMappingPropertyPushStatus
        """

        self._push_status = push_status

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
        if issubclass(ProfileMappingProperty, dict):
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
        if not isinstance(other, ProfileMappingProperty):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other