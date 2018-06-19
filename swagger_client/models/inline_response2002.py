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


class InlineResponse2002(object):
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
        'message': 'str',
        'user_cash_balance': 'float'
    }

    attribute_map = {
        'status': 'status',
        'message': 'message',
        'user_cash_balance': 'user_cash_balance'
    }

    def __init__(self, status=None, message=None, user_cash_balance=None):  # noqa: E501
        """InlineResponse2002 - a model defined in Swagger"""  # noqa: E501

        self._status = None
        self._message = None
        self._user_cash_balance = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if message is not None:
            self.message = message
        if user_cash_balance is not None:
            self.user_cash_balance = user_cash_balance

    @property
    def status(self):
        """Gets the status of this InlineResponse2002.  # noqa: E501

        The status of the API request  # noqa: E501

        :return: The status of this InlineResponse2002.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponse2002.

        The status of the API request  # noqa: E501

        :param status: The status of this InlineResponse2002.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def message(self):
        """Gets the message of this InlineResponse2002.  # noqa: E501

        Display message  # noqa: E501

        :return: The message of this InlineResponse2002.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this InlineResponse2002.

        Display message  # noqa: E501

        :param message: The message of this InlineResponse2002.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def user_cash_balance(self):
        """Gets the user_cash_balance of this InlineResponse2002.  # noqa: E501

        Remaining cash balance  # noqa: E501

        :return: The user_cash_balance of this InlineResponse2002.  # noqa: E501
        :rtype: float
        """
        return self._user_cash_balance

    @user_cash_balance.setter
    def user_cash_balance(self, user_cash_balance):
        """Sets the user_cash_balance of this InlineResponse2002.

        Remaining cash balance  # noqa: E501

        :param user_cash_balance: The user_cash_balance of this InlineResponse2002.  # noqa: E501
        :type: float
        """

        self._user_cash_balance = user_cash_balance

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
        if not isinstance(other, InlineResponse2002):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other