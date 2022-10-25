# coding: utf-8

"""
    织信开放API接口

    织信开放API接口  # noqa: E501

    OpenAPI spec version: v2
    Contact: sales@conrerstone365.cn
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AdminAccountGetRequest(object):
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
        'id': 'str',
        'oid': 'str',
        'user_name': 'str',
        'mobile_no': 'str',
        'email': 'str'
    }

    attribute_map = {
        'id': 'id',
        'oid': 'oid',
        'user_name': 'userName',
        'mobile_no': 'mobileNo',
        'email': 'email'
    }

    def __init__(self, id=None, oid=None, user_name=None, mobile_no=None, email=None):  # noqa: E501
        """AdminAccountGetRequest - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._oid = None
        self._user_name = None
        self._mobile_no = None
        self._email = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if oid is not None:
            self.oid = oid
        if user_name is not None:
            self.user_name = user_name
        if mobile_no is not None:
            self.mobile_no = mobile_no
        if email is not None:
            self.email = email

    @property
    def id(self):
        """Gets the id of this AdminAccountGetRequest.  # noqa: E501

        id  # noqa: E501

        :return: The id of this AdminAccountGetRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AdminAccountGetRequest.

        id  # noqa: E501

        :param id: The id of this AdminAccountGetRequest.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def oid(self):
        """Gets the oid of this AdminAccountGetRequest.  # noqa: E501

        oid  # noqa: E501

        :return: The oid of this AdminAccountGetRequest.  # noqa: E501
        :rtype: str
        """
        return self._oid

    @oid.setter
    def oid(self, oid):
        """Sets the oid of this AdminAccountGetRequest.

        oid  # noqa: E501

        :param oid: The oid of this AdminAccountGetRequest.  # noqa: E501
        :type: str
        """

        self._oid = oid

    @property
    def user_name(self):
        """Gets the user_name of this AdminAccountGetRequest.  # noqa: E501

        用户名  # noqa: E501

        :return: The user_name of this AdminAccountGetRequest.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this AdminAccountGetRequest.

        用户名  # noqa: E501

        :param user_name: The user_name of this AdminAccountGetRequest.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def mobile_no(self):
        """Gets the mobile_no of this AdminAccountGetRequest.  # noqa: E501

        手机号  # noqa: E501

        :return: The mobile_no of this AdminAccountGetRequest.  # noqa: E501
        :rtype: str
        """
        return self._mobile_no

    @mobile_no.setter
    def mobile_no(self, mobile_no):
        """Sets the mobile_no of this AdminAccountGetRequest.

        手机号  # noqa: E501

        :param mobile_no: The mobile_no of this AdminAccountGetRequest.  # noqa: E501
        :type: str
        """

        self._mobile_no = mobile_no

    @property
    def email(self):
        """Gets the email of this AdminAccountGetRequest.  # noqa: E501

        手机号  # noqa: E501

        :return: The email of this AdminAccountGetRequest.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this AdminAccountGetRequest.

        手机号  # noqa: E501

        :param email: The email of this AdminAccountGetRequest.  # noqa: E501
        :type: str
        """

        self._email = email

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
        if issubclass(AdminAccountGetRequest, dict):
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
        if not isinstance(other, AdminAccountGetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other