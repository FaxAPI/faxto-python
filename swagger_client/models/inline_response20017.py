# coding: utf-8

"""
    Fax.to REST API client for Python

    This is Fax.to REST API client for Python.  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: inquiries@fax.to
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.inline_response20017_numbers import InlineResponse20017Numbers  # noqa: F401,E501
from swagger_client.models.inline_response2004_meta import InlineResponse2004Meta  # noqa: F401,E501


class InlineResponse20017(object):
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
        'status': 'str',
        'numbers': 'list[InlineResponse20017Numbers]',
        'meta': 'InlineResponse2004Meta'
    }

    attribute_map = {
        'status': 'status',
        'numbers': 'numbers',
        'meta': 'meta'
    }

    def __init__(self, status=None, numbers=None, meta=None):  # noqa: E501
        """InlineResponse20017 - a model defined in Swagger"""  # noqa: E501

        self._status = None
        self._numbers = None
        self._meta = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if numbers is not None:
            self.numbers = numbers
        if meta is not None:
            self.meta = meta

    @property
    def status(self):
        """Gets the status of this InlineResponse20017.  # noqa: E501

        The status of the API request  # noqa: E501

        :return: The status of this InlineResponse20017.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponse20017.

        The status of the API request  # noqa: E501

        :param status: The status of this InlineResponse20017.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def numbers(self):
        """Gets the numbers of this InlineResponse20017.  # noqa: E501

        Numbers data  # noqa: E501

        :return: The numbers of this InlineResponse20017.  # noqa: E501
        :rtype: list[InlineResponse20017Numbers]
        """
        return self._numbers

    @numbers.setter
    def numbers(self, numbers):
        """Sets the numbers of this InlineResponse20017.

        Numbers data  # noqa: E501

        :param numbers: The numbers of this InlineResponse20017.  # noqa: E501
        :type: list[InlineResponse20017Numbers]
        """

        self._numbers = numbers

    @property
    def meta(self):
        """Gets the meta of this InlineResponse20017.  # noqa: E501


        :return: The meta of this InlineResponse20017.  # noqa: E501
        :rtype: InlineResponse2004Meta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this InlineResponse20017.


        :param meta: The meta of this InlineResponse20017.  # noqa: E501
        :type: InlineResponse2004Meta
        """

        self._meta = meta

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse20017):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
