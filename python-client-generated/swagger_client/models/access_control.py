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

class AccessControl(object):
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
        'members': 'list[object]',
        'roles': 'list[object]',
        'groups': 'list[object]',
        'departments': 'list[object]',
        'fields': 'list[object]'
    }

    attribute_map = {
        'members': 'members',
        'roles': 'roles',
        'groups': 'groups',
        'departments': 'departments',
        'fields': 'fields'
    }

    def __init__(self, members=None, roles=None, groups=None, departments=None, fields=None):  # noqa: E501
        """AccessControl - a model defined in Swagger"""  # noqa: E501
        self._members = None
        self._roles = None
        self._groups = None
        self._departments = None
        self._fields = None
        self.discriminator = None
        if members is not None:
            self.members = members
        if roles is not None:
            self.roles = roles
        if groups is not None:
            self.groups = groups
        if departments is not None:
            self.departments = departments
        if fields is not None:
            self.fields = fields

    @property
    def members(self):
        """Gets the members of this AccessControl.  # noqa: E501

        成员列表  # noqa: E501

        :return: The members of this AccessControl.  # noqa: E501
        :rtype: list[object]
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this AccessControl.

        成员列表  # noqa: E501

        :param members: The members of this AccessControl.  # noqa: E501
        :type: list[object]
        """

        self._members = members

    @property
    def roles(self):
        """Gets the roles of this AccessControl.  # noqa: E501

        角色列表  # noqa: E501

        :return: The roles of this AccessControl.  # noqa: E501
        :rtype: list[object]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this AccessControl.

        角色列表  # noqa: E501

        :param roles: The roles of this AccessControl.  # noqa: E501
        :type: list[object]
        """

        self._roles = roles

    @property
    def groups(self):
        """Gets the groups of this AccessControl.  # noqa: E501

        分组列表  # noqa: E501

        :return: The groups of this AccessControl.  # noqa: E501
        :rtype: list[object]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this AccessControl.

        分组列表  # noqa: E501

        :param groups: The groups of this AccessControl.  # noqa: E501
        :type: list[object]
        """

        self._groups = groups

    @property
    def departments(self):
        """Gets the departments of this AccessControl.  # noqa: E501

        部门列表  # noqa: E501

        :return: The departments of this AccessControl.  # noqa: E501
        :rtype: list[object]
        """
        return self._departments

    @departments.setter
    def departments(self, departments):
        """Sets the departments of this AccessControl.

        部门列表  # noqa: E501

        :param departments: The departments of this AccessControl.  # noqa: E501
        :type: list[object]
        """

        self._departments = departments

    @property
    def fields(self):
        """Gets the fields of this AccessControl.  # noqa: E501

        字段列表  # noqa: E501

        :return: The fields of this AccessControl.  # noqa: E501
        :rtype: list[object]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this AccessControl.

        字段列表  # noqa: E501

        :param fields: The fields of this AccessControl.  # noqa: E501
        :type: list[object]
        """

        self._fields = fields

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
        if issubclass(AccessControl, dict):
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
        if not isinstance(other, AccessControl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other