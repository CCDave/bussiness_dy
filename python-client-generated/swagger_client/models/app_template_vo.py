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

class AppTemplateVO(object):
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
        'app_id': 'str',
        'version': 'int',
        'name': 'str',
        'category_list': 'list[object]',
        'cover_id': 'str',
        'remark': 'str',
        'detail': 'str',
        'row_number': 'float',
        'is_free': 'bool',
        'is_default': 'bool',
        'is_hidden': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'app_id': 'appId',
        'version': 'version',
        'name': 'name',
        'category_list': 'categoryList',
        'cover_id': 'coverId',
        'remark': 'remark',
        'detail': 'detail',
        'row_number': 'rowNumber',
        'is_free': 'isFree',
        'is_default': 'isDefault',
        'is_hidden': 'isHidden'
    }

    def __init__(self, id=None, app_id=None, version=None, name=None, category_list=None, cover_id=None, remark=None, detail=None, row_number=None, is_free=None, is_default=None, is_hidden=None):  # noqa: E501
        """AppTemplateVO - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._app_id = None
        self._version = None
        self._name = None
        self._category_list = None
        self._cover_id = None
        self._remark = None
        self._detail = None
        self._row_number = None
        self._is_free = None
        self._is_default = None
        self._is_hidden = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if app_id is not None:
            self.app_id = app_id
        if version is not None:
            self.version = version
        if name is not None:
            self.name = name
        if category_list is not None:
            self.category_list = category_list
        if cover_id is not None:
            self.cover_id = cover_id
        if remark is not None:
            self.remark = remark
        if detail is not None:
            self.detail = detail
        if row_number is not None:
            self.row_number = row_number
        if is_free is not None:
            self.is_free = is_free
        if is_default is not None:
            self.is_default = is_default
        if is_hidden is not None:
            self.is_hidden = is_hidden

    @property
    def id(self):
        """Gets the id of this AppTemplateVO.  # noqa: E501

        ID  # noqa: E501

        :return: The id of this AppTemplateVO.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AppTemplateVO.

        ID  # noqa: E501

        :param id: The id of this AppTemplateVO.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def app_id(self):
        """Gets the app_id of this AppTemplateVO.  # noqa: E501

        应用ID  # noqa: E501

        :return: The app_id of this AppTemplateVO.  # noqa: E501
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this AppTemplateVO.

        应用ID  # noqa: E501

        :param app_id: The app_id of this AppTemplateVO.  # noqa: E501
        :type: str
        """

        self._app_id = app_id

    @property
    def version(self):
        """Gets the version of this AppTemplateVO.  # noqa: E501

        版本号  # noqa: E501

        :return: The version of this AppTemplateVO.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this AppTemplateVO.

        版本号  # noqa: E501

        :param version: The version of this AppTemplateVO.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def name(self):
        """Gets the name of this AppTemplateVO.  # noqa: E501

        名称  # noqa: E501

        :return: The name of this AppTemplateVO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AppTemplateVO.

        名称  # noqa: E501

        :param name: The name of this AppTemplateVO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def category_list(self):
        """Gets the category_list of this AppTemplateVO.  # noqa: E501

        分类  # noqa: E501

        :return: The category_list of this AppTemplateVO.  # noqa: E501
        :rtype: list[object]
        """
        return self._category_list

    @category_list.setter
    def category_list(self, category_list):
        """Sets the category_list of this AppTemplateVO.

        分类  # noqa: E501

        :param category_list: The category_list of this AppTemplateVO.  # noqa: E501
        :type: list[object]
        """

        self._category_list = category_list

    @property
    def cover_id(self):
        """Gets the cover_id of this AppTemplateVO.  # noqa: E501

        封面  # noqa: E501

        :return: The cover_id of this AppTemplateVO.  # noqa: E501
        :rtype: str
        """
        return self._cover_id

    @cover_id.setter
    def cover_id(self, cover_id):
        """Sets the cover_id of this AppTemplateVO.

        封面  # noqa: E501

        :param cover_id: The cover_id of this AppTemplateVO.  # noqa: E501
        :type: str
        """

        self._cover_id = cover_id

    @property
    def remark(self):
        """Gets the remark of this AppTemplateVO.  # noqa: E501

        备注  # noqa: E501

        :return: The remark of this AppTemplateVO.  # noqa: E501
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this AppTemplateVO.

        备注  # noqa: E501

        :param remark: The remark of this AppTemplateVO.  # noqa: E501
        :type: str
        """

        self._remark = remark

    @property
    def detail(self):
        """Gets the detail of this AppTemplateVO.  # noqa: E501

        富文本  # noqa: E501

        :return: The detail of this AppTemplateVO.  # noqa: E501
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this AppTemplateVO.

        富文本  # noqa: E501

        :param detail: The detail of this AppTemplateVO.  # noqa: E501
        :type: str
        """

        self._detail = detail

    @property
    def row_number(self):
        """Gets the row_number of this AppTemplateVO.  # noqa: E501

        排序  # noqa: E501

        :return: The row_number of this AppTemplateVO.  # noqa: E501
        :rtype: float
        """
        return self._row_number

    @row_number.setter
    def row_number(self, row_number):
        """Sets the row_number of this AppTemplateVO.

        排序  # noqa: E501

        :param row_number: The row_number of this AppTemplateVO.  # noqa: E501
        :type: float
        """

        self._row_number = row_number

    @property
    def is_free(self):
        """Gets the is_free of this AppTemplateVO.  # noqa: E501

        是否免费  # noqa: E501

        :return: The is_free of this AppTemplateVO.  # noqa: E501
        :rtype: bool
        """
        return self._is_free

    @is_free.setter
    def is_free(self, is_free):
        """Sets the is_free of this AppTemplateVO.

        是否免费  # noqa: E501

        :param is_free: The is_free of this AppTemplateVO.  # noqa: E501
        :type: bool
        """

        self._is_free = is_free

    @property
    def is_default(self):
        """Gets the is_default of this AppTemplateVO.  # noqa: E501

        是否默认安装  # noqa: E501

        :return: The is_default of this AppTemplateVO.  # noqa: E501
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this AppTemplateVO.

        是否默认安装  # noqa: E501

        :param is_default: The is_default of this AppTemplateVO.  # noqa: E501
        :type: bool
        """

        self._is_default = is_default

    @property
    def is_hidden(self):
        """Gets the is_hidden of this AppTemplateVO.  # noqa: E501

        是否隐藏  # noqa: E501

        :return: The is_hidden of this AppTemplateVO.  # noqa: E501
        :rtype: bool
        """
        return self._is_hidden

    @is_hidden.setter
    def is_hidden(self, is_hidden):
        """Sets the is_hidden of this AppTemplateVO.

        是否隐藏  # noqa: E501

        :param is_hidden: The is_hidden of this AppTemplateVO.  # noqa: E501
        :type: bool
        """

        self._is_hidden = is_hidden

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
        if issubclass(AppTemplateVO, dict):
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
        if not isinstance(other, AppTemplateVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other