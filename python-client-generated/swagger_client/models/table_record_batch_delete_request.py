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

class TableRecordBatchDeleteRequest(object):
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
        'table_id': 'str',
        'id_list': 'list[object]'
    }

    attribute_map = {
        'table_id': 'tableId',
        'id_list': 'idList'
    }

    def __init__(self, table_id=None, id_list=None):  # noqa: E501
        """TableRecordBatchDeleteRequest - a model defined in Swagger"""  # noqa: E501
        self._table_id = None
        self._id_list = None
        self.discriminator = None
        self.table_id = table_id
        self.id_list = id_list

    @property
    def table_id(self):
        """Gets the table_id of this TableRecordBatchDeleteRequest.  # noqa: E501

        数据表ID  # noqa: E501

        :return: The table_id of this TableRecordBatchDeleteRequest.  # noqa: E501
        :rtype: str
        """
        return self._table_id

    @table_id.setter
    def table_id(self, table_id):
        """Sets the table_id of this TableRecordBatchDeleteRequest.

        数据表ID  # noqa: E501

        :param table_id: The table_id of this TableRecordBatchDeleteRequest.  # noqa: E501
        :type: str
        """
        if table_id is None:
            raise ValueError("Invalid value for `table_id`, must not be `None`")  # noqa: E501

        self._table_id = table_id

    @property
    def id_list(self):
        """Gets the id_list of this TableRecordBatchDeleteRequest.  # noqa: E501

        记录ID列表  # noqa: E501

        :return: The id_list of this TableRecordBatchDeleteRequest.  # noqa: E501
        :rtype: list[object]
        """
        return self._id_list

    @id_list.setter
    def id_list(self, id_list):
        """Sets the id_list of this TableRecordBatchDeleteRequest.

        记录ID列表  # noqa: E501

        :param id_list: The id_list of this TableRecordBatchDeleteRequest.  # noqa: E501
        :type: list[object]
        """
        if id_list is None:
            raise ValueError("Invalid value for `id_list`, must not be `None`")  # noqa: E501

        self._id_list = id_list

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
        if issubclass(TableRecordBatchDeleteRequest, dict):
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
        if not isinstance(other, TableRecordBatchDeleteRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other