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


class InlineResponse20015Data(object):
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
        'did_group_id': 'int',
        'area_code': 'str',
        'city_name': 'str'
    }

    attribute_map = {
        'did_group_id': 'did_group_id',
        'area_code': 'area_code',
        'city_name': 'city_name'
    }

    def __init__(self, did_group_id=None, area_code=None, city_name=None):  # noqa: E501
        """InlineResponse20015Data - a model defined in Swagger"""  # noqa: E501

        self._did_group_id = None
        self._area_code = None
        self._city_name = None
        self.discriminator = None

        if did_group_id is not None:
            self.did_group_id = did_group_id
        if area_code is not None:
            self.area_code = area_code
        if city_name is not None:
            self.city_name = city_name

    @property
    def did_group_id(self):
        """Gets the did_group_id of this InlineResponse20015Data.  # noqa: E501


        :return: The did_group_id of this InlineResponse20015Data.  # noqa: E501
        :rtype: int
        """
        return self._did_group_id

    @did_group_id.setter
    def did_group_id(self, did_group_id):
        """Sets the did_group_id of this InlineResponse20015Data.


        :param did_group_id: The did_group_id of this InlineResponse20015Data.  # noqa: E501
        :type: int
        """

        self._did_group_id = did_group_id

    @property
    def area_code(self):
        """Gets the area_code of this InlineResponse20015Data.  # noqa: E501


        :return: The area_code of this InlineResponse20015Data.  # noqa: E501
        :rtype: str
        """
        return self._area_code

    @area_code.setter
    def area_code(self, area_code):
        """Sets the area_code of this InlineResponse20015Data.


        :param area_code: The area_code of this InlineResponse20015Data.  # noqa: E501
        :type: str
        """

        self._area_code = area_code

    @property
    def city_name(self):
        """Gets the city_name of this InlineResponse20015Data.  # noqa: E501


        :return: The city_name of this InlineResponse20015Data.  # noqa: E501
        :rtype: str
        """
        return self._city_name

    @city_name.setter
    def city_name(self, city_name):
        """Sets the city_name of this InlineResponse20015Data.


        :param city_name: The city_name of this InlineResponse20015Data.  # noqa: E501
        :type: str
        """

        self._city_name = city_name

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
        if not isinstance(other, InlineResponse20015Data):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other