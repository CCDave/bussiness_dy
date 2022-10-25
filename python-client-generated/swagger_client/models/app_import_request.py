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

class AppImportRequest(object):
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
        'content': 'str',
        'ima_file_path': 'str',
        'group_id': 'str',
        'unique_src_id': 'bool'
    }

    attribute_map = {
        'content': 'content',
        'ima_file_path': 'imaFilePath',
        'group_id': 'groupId',
        'unique_src_id': 'uniqueSrcId'
    }

    def __init__(self, content=None, ima_file_path=None, group_id=None, unique_src_id=None):  # noqa: E501
        """AppImportRequest - a model defined in Swagger"""  # noqa: E501
        self._content = None
        self._ima_file_path = None
        self._group_id = None
        self._unique_src_id = None
        self.discriminator = None
        if content is not None:
            self.content = content
        if ima_file_path is not None:
            self.ima_file_path = ima_file_path
        if group_id is not None:
            self.group_id = group_id
        if unique_src_id is not None:
            self.unique_src_id = unique_src_id

    @property
    def content(self):
        """Gets the content of this AppImportRequest.  # noqa: E501

        应用数据  # noqa: E501

        :return: The content of this AppImportRequest.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this AppImportRequest.

        应用数据  # noqa: E501

        :param content: The content of this AppImportRequest.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def ima_file_path(self):
        """Gets the ima_file_path of this AppImportRequest.  # noqa: E501

        ima文件路径  # noqa: E501

        :return: The ima_file_path of this AppImportRequest.  # noqa: E501
        :rtype: str
        """
        return self._ima_file_path

    @ima_file_path.setter
    def ima_file_path(self, ima_file_path):
        """Sets the ima_file_path of this AppImportRequest.

        ima文件路径  # noqa: E501

        :param ima_file_path: The ima_file_path of this AppImportRequest.  # noqa: E501
        :type: str
        """

        self._ima_file_path = ima_file_path

    @property
    def group_id(self):
        """Gets the group_id of this AppImportRequest.  # noqa: E501

        分组ID  # noqa: E501

        :return: The group_id of this AppImportRequest.  # noqa: E501
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this AppImportRequest.

        分组ID  # noqa: E501

        :param group_id: The group_id of this AppImportRequest.  # noqa: E501
        :type: str
        """

        self._group_id = group_id

    @property
    def unique_src_id(self):
        """Gets the unique_src_id of this AppImportRequest.  # noqa: E501

        源应用ID不能重复  # noqa: E501

        :return: The unique_src_id of this AppImportRequest.  # noqa: E501
        :rtype: bool
        """
        return self._unique_src_id

    @unique_src_id.setter
    def unique_src_id(self, unique_src_id):
        """Sets the unique_src_id of this AppImportRequest.

        源应用ID不能重复  # noqa: E501

        :param unique_src_id: The unique_src_id of this AppImportRequest.  # noqa: E501
        :type: bool
        """

        self._unique_src_id = unique_src_id

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
        if issubclass(AppImportRequest, dict):
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
        if not isinstance(other, AppImportRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other