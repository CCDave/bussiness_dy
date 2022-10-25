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

class AdminAccountUpdateRequest(object):
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
        'name': 'str',
        'avatar': 'str',
        'mobile_no': 'str',
        'email': 'str',
        'oid': 'str',
        'remark': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'avatar': 'avatar',
        'mobile_no': 'mobileNo',
        'email': 'email',
        'oid': 'oid',
        'remark': 'remark'
    }

    def __init__(self, id=None, name=None, avatar=None, mobile_no=None, email=None, oid=None, remark=None):  # noqa: E501
        """AdminAccountUpdateRequest - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._avatar = None
        self._mobile_no = None
        self._email = None
        self._oid = None
        self._remark = None
        self.discriminator = None
        self.id = id
        if name is not None:
            self.name = name
        if avatar is not None:
            self.avatar = avatar
        if mobile_no is not None:
            self.mobile_no = mobile_no
        if email is not None:
            self.email = email
        if oid is not None:
            self.oid = oid
        if remark is not None:
            self.remark = remark

    @property
    def id(self):
        """Gets the id of this AdminAccountUpdateRequest.  # noqa: E501

        id  # noqa: E501

        :return: The id of this AdminAccountUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AdminAccountUpdateRequest.

        id  # noqa: E501

        :param id: The id of this AdminAccountUpdateRequest.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this AdminAccountUpdateRequest.  # noqa: E501

        姓名  # noqa: E501

        :return: The name of this AdminAccountUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AdminAccountUpdateRequest.

        姓名  # noqa: E501

        :param name: The name of this AdminAccountUpdateRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def avatar(self):
        """Gets the avatar of this AdminAccountUpdateRequest.  # noqa: E501

        头像  # noqa: E501

        :return: The avatar of this AdminAccountUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._avatar

    @avatar.setter
    def avatar(self, avatar):
        """Sets the avatar of this AdminAccountUpdateRequest.

        头像  # noqa: E501

        :param avatar: The avatar of this AdminAccountUpdateRequest.  # noqa: E501
        :type: str
        """

        self._avatar = avatar

    @property
    def mobile_no(self):
        """Gets the mobile_no of this AdminAccountUpdateRequest.  # noqa: E501

        手机号  # noqa: E501

        :return: The mobile_no of this AdminAccountUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._mobile_no

    @mobile_no.setter
    def mobile_no(self, mobile_no):
        """Sets the mobile_no of this AdminAccountUpdateRequest.

        手机号  # noqa: E501

        :param mobile_no: The mobile_no of this AdminAccountUpdateRequest.  # noqa: E501
        :type: str
        """

        self._mobile_no = mobile_no

    @property
    def email(self):
        """Gets the email of this AdminAccountUpdateRequest.  # noqa: E501

        邮箱  # noqa: E501

        :return: The email of this AdminAccountUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this AdminAccountUpdateRequest.

        邮箱  # noqa: E501

        :param email: The email of this AdminAccountUpdateRequest.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def oid(self):
        """Gets the oid of this AdminAccountUpdateRequest.  # noqa: E501

        oid  # noqa: E501

        :return: The oid of this AdminAccountUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._oid

    @oid.setter
    def oid(self, oid):
        """Sets the oid of this AdminAccountUpdateRequest.

        oid  # noqa: E501

        :param oid: The oid of this AdminAccountUpdateRequest.  # noqa: E501
        :type: str
        """

        self._oid = oid

    @property
    def remark(self):
        """Gets the remark of this AdminAccountUpdateRequest.  # noqa: E501

        备注  # noqa: E501

        :return: The remark of this AdminAccountUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this AdminAccountUpdateRequest.

        备注  # noqa: E501

        :param remark: The remark of this AdminAccountUpdateRequest.  # noqa: E501
        :type: str
        """

        self._remark = remark

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
        if issubclass(AdminAccountUpdateRequest, dict):
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
        if not isinstance(other, AdminAccountUpdateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other