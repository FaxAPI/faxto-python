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


class InlineResponse2003Created(object):
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
        '_date': 'datetime',
        'timezone_type': 'int',
        'timezone': 'str'
    }

    attribute_map = {
        '_date': 'date',
        'timezone_type': 'timezone_type',
        'timezone': 'timezone'
    }

    def __init__(self, _date=None, timezone_type=None, timezone=None):  # noqa: E501
        """InlineResponse2003Created - a model defined in Swagger"""  # noqa: E501

        self.__date = None
        self._timezone_type = None
        self._timezone = None
        self.discriminator = None

        if _date is not None:
            self._date = _date
        if timezone_type is not None:
            self.timezone_type = timezone_type
        if timezone is not None:
            self.timezone = timezone

    @property
    def _date(self):
        """Gets the _date of this InlineResponse2003Created.  # noqa: E501


        :return: The _date of this InlineResponse2003Created.  # noqa: E501
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this InlineResponse2003Created.


        :param _date: The _date of this InlineResponse2003Created.  # noqa: E501
        :type: datetime
        """

        self.__date = _date

    @property
    def timezone_type(self):
        """Gets the timezone_type of this InlineResponse2003Created.  # noqa: E501


        :return: The timezone_type of this InlineResponse2003Created.  # noqa: E501
        :rtype: int
        """
        return self._timezone_type

    @timezone_type.setter
    def timezone_type(self, timezone_type):
        """Sets the timezone_type of this InlineResponse2003Created.


        :param timezone_type: The timezone_type of this InlineResponse2003Created.  # noqa: E501
        :type: int
        """

        self._timezone_type = timezone_type

    @property
    def timezone(self):
        """Gets the timezone of this InlineResponse2003Created.  # noqa: E501


        :return: The timezone of this InlineResponse2003Created.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this InlineResponse2003Created.


        :param timezone: The timezone of this InlineResponse2003Created.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

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
        if not isinstance(other, InlineResponse2003Created):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
