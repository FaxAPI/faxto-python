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

from swagger_client.models.inline_response2003_created import InlineResponse2003Created  # noqa: F401,E501


class InlineResponse2003History(object):
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
        'created': 'InlineResponse2003Created',
        'document_id': 'int',
        'document': 'str',
        'recipient': 'str',
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'created': 'created',
        'document_id': 'document_id',
        'document': 'document',
        'recipient': 'recipient',
        'status': 'status'
    }

    def __init__(self, id=None, created=None, document_id=None, document=None, recipient=None, status=None):  # noqa: E501
        """InlineResponse2003History - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._created = None
        self._document_id = None
        self._document = None
        self._recipient = None
        self._status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if created is not None:
            self.created = created
        if document_id is not None:
            self.document_id = document_id
        if document is not None:
            self.document = document
        if recipient is not None:
            self.recipient = recipient
        if status is not None:
            self.status = status

    @property
    def id(self):
        """Gets the id of this InlineResponse2003History.  # noqa: E501


        :return: The id of this InlineResponse2003History.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse2003History.


        :param id: The id of this InlineResponse2003History.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def created(self):
        """Gets the created of this InlineResponse2003History.  # noqa: E501


        :return: The created of this InlineResponse2003History.  # noqa: E501
        :rtype: InlineResponse2003Created
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this InlineResponse2003History.


        :param created: The created of this InlineResponse2003History.  # noqa: E501
        :type: InlineResponse2003Created
        """

        self._created = created

    @property
    def document_id(self):
        """Gets the document_id of this InlineResponse2003History.  # noqa: E501


        :return: The document_id of this InlineResponse2003History.  # noqa: E501
        :rtype: int
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this InlineResponse2003History.


        :param document_id: The document_id of this InlineResponse2003History.  # noqa: E501
        :type: int
        """

        self._document_id = document_id

    @property
    def document(self):
        """Gets the document of this InlineResponse2003History.  # noqa: E501


        :return: The document of this InlineResponse2003History.  # noqa: E501
        :rtype: str
        """
        return self._document

    @document.setter
    def document(self, document):
        """Sets the document of this InlineResponse2003History.


        :param document: The document of this InlineResponse2003History.  # noqa: E501
        :type: str
        """

        self._document = document

    @property
    def recipient(self):
        """Gets the recipient of this InlineResponse2003History.  # noqa: E501


        :return: The recipient of this InlineResponse2003History.  # noqa: E501
        :rtype: str
        """
        return self._recipient

    @recipient.setter
    def recipient(self, recipient):
        """Sets the recipient of this InlineResponse2003History.


        :param recipient: The recipient of this InlineResponse2003History.  # noqa: E501
        :type: str
        """

        self._recipient = recipient

    @property
    def status(self):
        """Gets the status of this InlineResponse2003History.  # noqa: E501

        The status of the fax job  # noqa: E501

        :return: The status of this InlineResponse2003History.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponse2003History.

        The status of the fax job  # noqa: E501

        :param status: The status of this InlineResponse2003History.  # noqa: E501
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
        if not isinstance(other, InlineResponse2003History):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
