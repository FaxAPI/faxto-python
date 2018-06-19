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

from swagger_client.models.inline_response2003_history import InlineResponse2003History  # noqa: F401,E501


class InlineResponse2003(object):
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
        'history': 'list[InlineResponse2003History]'
    }

    attribute_map = {
        'status': 'status',
        'history': 'history'
    }

    def __init__(self, status=None, history=None):  # noqa: E501
        """InlineResponse2003 - a model defined in Swagger"""  # noqa: E501

        self._status = None
        self._history = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if history is not None:
            self.history = history

    @property
    def status(self):
        """Gets the status of this InlineResponse2003.  # noqa: E501

        The status of the API request  # noqa: E501

        :return: The status of this InlineResponse2003.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponse2003.

        The status of the API request  # noqa: E501

        :param status: The status of this InlineResponse2003.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def history(self):
        """Gets the history of this InlineResponse2003.  # noqa: E501

        The fax jobs requested  # noqa: E501

        :return: The history of this InlineResponse2003.  # noqa: E501
        :rtype: list[InlineResponse2003History]
        """
        return self._history

    @history.setter
    def history(self, history):
        """Sets the history of this InlineResponse2003.

        The fax jobs requested  # noqa: E501

        :param history: The history of this InlineResponse2003.  # noqa: E501
        :type: list[InlineResponse2003History]
        """

        self._history = history

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
        if not isinstance(other, InlineResponse2003):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other