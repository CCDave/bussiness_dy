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

class AdminAppTemplateUpdateRequest(object):
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
        'form': 'AppTemplateUpdateForm',
        'update_fields': 'list[object]'
    }

    attribute_map = {
        'form': 'form',
        'update_fields': 'updateFields'
    }

    def __init__(self, form=None, update_fields=None):  # noqa: E501
        """AdminAppTemplateUpdateRequest - a model defined in Swagger"""  # noqa: E501
        self._form = None
        self._update_fields = None
        self.discriminator = None
        self.form = form
        self.update_fields = update_fields

    @property
    def form(self):
        """Gets the form of this AdminAppTemplateUpdateRequest.  # noqa: E501


        :return: The form of this AdminAppTemplateUpdateRequest.  # noqa: E501
        :rtype: AppTemplateUpdateForm
        """
        return self._form

    @form.setter
    def form(self, form):
        """Sets the form of this AdminAppTemplateUpdateRequest.


        :param form: The form of this AdminAppTemplateUpdateRequest.  # noqa: E501
        :type: AppTemplateUpdateForm
        """
        if form is None:
            raise ValueError("Invalid value for `form`, must not be `None`")  # noqa: E501

        self._form = form

    @property
    def update_fields(self):
        """Gets the update_fields of this AdminAppTemplateUpdateRequest.  # noqa: E501

        需要更新的字段列表  # noqa: E501

        :return: The update_fields of this AdminAppTemplateUpdateRequest.  # noqa: E501
        :rtype: list[object]
        """
        return self._update_fields

    @update_fields.setter
    def update_fields(self, update_fields):
        """Sets the update_fields of this AdminAppTemplateUpdateRequest.

        需要更新的字段列表  # noqa: E501

        :param update_fields: The update_fields of this AdminAppTemplateUpdateRequest.  # noqa: E501
        :type: list[object]
        """
        if update_fields is None:
            raise ValueError("Invalid value for `update_fields`, must not be `None`")  # noqa: E501

        self._update_fields = update_fields

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
        if issubclass(AdminAppTemplateUpdateRequest, dict):
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
        if not isinstance(other, AdminAppTemplateUpdateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other