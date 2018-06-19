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


class InlineResponse20017Numbers(object):
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
        'id': 'int',
        'order_reference': 'str',
        'country_code': 'str',
        'country': 'str',
        'city_name': 'str',
        'area_code': 'str',
        'did_group_id': 'int',
        'did_number': 'str',
        'expiration_date': 'date',
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'order_reference': 'order_reference',
        'country_code': 'country_code',
        'country': 'country',
        'city_name': 'city_name',
        'area_code': 'area_code',
        'did_group_id': 'did_group_id',
        'did_number': 'did_number',
        'expiration_date': 'expiration_date',
        'status': 'status'
    }

    def __init__(self, id=None, order_reference=None, country_code=None, country=None, city_name=None, area_code=None, did_group_id=None, did_number=None, expiration_date=None, status=None):  # noqa: E501
        """InlineResponse20017Numbers - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._order_reference = None
        self._country_code = None
        self._country = None
        self._city_name = None
        self._area_code = None
        self._did_group_id = None
        self._did_number = None
        self._expiration_date = None
        self._status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if order_reference is not None:
            self.order_reference = order_reference
        if country_code is not None:
            self.country_code = country_code
        if country is not None:
            self.country = country
        if city_name is not None:
            self.city_name = city_name
        if area_code is not None:
            self.area_code = area_code
        if did_group_id is not None:
            self.did_group_id = did_group_id
        if did_number is not None:
            self.did_number = did_number
        if expiration_date is not None:
            self.expiration_date = expiration_date
        if status is not None:
            self.status = status

    @property
    def id(self):
        """Gets the id of this InlineResponse20017Numbers.  # noqa: E501


        :return: The id of this InlineResponse20017Numbers.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20017Numbers.


        :param id: The id of this InlineResponse20017Numbers.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def order_reference(self):
        """Gets the order_reference of this InlineResponse20017Numbers.  # noqa: E501


        :return: The order_reference of this InlineResponse20017Numbers.  # noqa: E501
        :rtype: str
        """
        return self._order_reference

    @order_reference.setter
    def order_reference(self, order_reference):
        """Sets the order_reference of this InlineResponse20017Numbers.


        :param order_reference: The order_reference of this InlineResponse20017Numbers.  # noqa: E501
        :type: str
        """

        self._order_reference = order_reference

    @property
    def country_code(self):
        """Gets the country_code of this InlineResponse20017Numbers.  # noqa: E501


        :return: The country_code of this InlineResponse20017Numbers.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this InlineResponse20017Numbers.


        :param country_code: The country_code of this InlineResponse20017Numbers.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    @property
    def country(self):
        """Gets the country of this InlineResponse20017Numbers.  # noqa: E501


        :return: The country of this InlineResponse20017Numbers.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this InlineResponse20017Numbers.


        :param country: The country of this InlineResponse20017Numbers.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def city_name(self):
        """Gets the city_name of this InlineResponse20017Numbers.  # noqa: E501


        :return: The city_name of this InlineResponse20017Numbers.  # noqa: E501
        :rtype: str
        """
        return self._city_name

    @city_name.setter
    def city_name(self, city_name):
        """Sets the city_name of this InlineResponse20017Numbers.


        :param city_name: The city_name of this InlineResponse20017Numbers.  # noqa: E501
        :type: str
        """

        self._city_name = city_name

    @property
    def area_code(self):
        """Gets the area_code of this InlineResponse20017Numbers.  # noqa: E501


        :return: The area_code of this InlineResponse20017Numbers.  # noqa: E501
        :rtype: str
        """
        return self._area_code

    @area_code.setter
    def area_code(self, area_code):
        """Sets the area_code of this InlineResponse20017Numbers.


        :param area_code: The area_code of this InlineResponse20017Numbers.  # noqa: E501
        :type: str
        """

        self._area_code = area_code

    @property
    def did_group_id(self):
        """Gets the did_group_id of this InlineResponse20017Numbers.  # noqa: E501


        :return: The did_group_id of this InlineResponse20017Numbers.  # noqa: E501
        :rtype: int
        """
        return self._did_group_id

    @did_group_id.setter
    def did_group_id(self, did_group_id):
        """Sets the did_group_id of this InlineResponse20017Numbers.


        :param did_group_id: The did_group_id of this InlineResponse20017Numbers.  # noqa: E501
        :type: int
        """

        self._did_group_id = did_group_id

    @property
    def did_number(self):
        """Gets the did_number of this InlineResponse20017Numbers.  # noqa: E501


        :return: The did_number of this InlineResponse20017Numbers.  # noqa: E501
        :rtype: str
        """
        return self._did_number

    @did_number.setter
    def did_number(self, did_number):
        """Sets the did_number of this InlineResponse20017Numbers.


        :param did_number: The did_number of this InlineResponse20017Numbers.  # noqa: E501
        :type: str
        """

        self._did_number = did_number

    @property
    def expiration_date(self):
        """Gets the expiration_date of this InlineResponse20017Numbers.  # noqa: E501


        :return: The expiration_date of this InlineResponse20017Numbers.  # noqa: E501
        :rtype: date
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        """Sets the expiration_date of this InlineResponse20017Numbers.


        :param expiration_date: The expiration_date of this InlineResponse20017Numbers.  # noqa: E501
        :type: date
        """

        self._expiration_date = expiration_date

    @property
    def status(self):
        """Gets the status of this InlineResponse20017Numbers.  # noqa: E501


        :return: The status of this InlineResponse20017Numbers.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponse20017Numbers.


        :param status: The status of this InlineResponse20017Numbers.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if not isinstance(other, InlineResponse20017Numbers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other