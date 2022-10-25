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

class FieldSetting(object):
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
        'visible': 'bool',
        'editable': 'bool',
        'default_value': 'object',
        'required': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'visible': 'visible',
        'editable': 'editable',
        'default_value': 'defaultValue',
        'required': 'required'
    }

    def __init__(self, id=None, visible=None, editable=None, default_value=None, required=None):  # noqa: E501
        """FieldSetting - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._visible = None
        self._editable = None
        self._default_value = None
        self._required = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if visible is not None:
            self.visible = visible
        if editable is not None:
            self.editable = editable
        if default_value is not None:
            self.default_value = default_value
        if required is not None:
            self.required = required

    @property
    def id(self):
        """Gets the id of this FieldSetting.  # noqa: E501

        字段ID  # noqa: E501

        :return: The id of this FieldSetting.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FieldSetting.

        字段ID  # noqa: E501

        :param id: The id of this FieldSetting.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def visible(self):
        """Gets the visible of this FieldSetting.  # noqa: E501

        是否显示  # noqa: E501

        :return: The visible of this FieldSetting.  # noqa: E501
        :rtype: bool
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        """Sets the visible of this FieldSetting.

        是否显示  # noqa: E501

        :param visible: The visible of this FieldSetting.  # noqa: E501
        :type: bool
        """

        self._visible = visible

    @property
    def editable(self):
        """Gets the editable of this FieldSetting.  # noqa: E501

        是否可编辑  # noqa: E501

        :return: The editable of this FieldSetting.  # noqa: E501
        :rtype: bool
        """
        return self._editable

    @editable.setter
    def editable(self, editable):
        """Sets the editable of this FieldSetting.

        是否可编辑  # noqa: E501

        :param editable: The editable of this FieldSetting.  # noqa: E501
        :type: bool
        """

        self._editable = editable

    @property
    def default_value(self):
        """Gets the default_value of this FieldSetting.  # noqa: E501

        默认值  # noqa: E501

        :return: The default_value of this FieldSetting.  # noqa: E501
        :rtype: object
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this FieldSetting.

        默认值  # noqa: E501

        :param default_value: The default_value of this FieldSetting.  # noqa: E501
        :type: object
        """

        self._default_value = default_value

    @property
    def required(self):
        """Gets the required of this FieldSetting.  # noqa: E501

        是否必填  # noqa: E501

        :return: The required of this FieldSetting.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this FieldSetting.

        是否必填  # noqa: E501

        :param required: The required of this FieldSetting.  # noqa: E501
        :type: bool
        """

        self._required = required

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
        if issubclass(FieldSetting, dict):
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
        if not isinstance(other, FieldSetting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other