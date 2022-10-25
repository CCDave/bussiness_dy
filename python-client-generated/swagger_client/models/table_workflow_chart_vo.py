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

class TableWorkflowChartVO(object):
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
        'workflow_id': 'str',
        'version': 'int',
        'graph': 'Graph',
        'nodes': 'list[Node]',
        'links': 'list[Link]',
        'id': 'str',
        'company_id': 'str',
        'application_id': 'str',
        'create_time': 'float',
        'update_time': 'float',
        'create_account_id': 'str',
        'create_account_name': 'str',
        'update_account_id': 'str',
        'update_account_name': 'str',
        'app_name': 'str',
        'app_color': 'str',
        'app_icon': 'str',
        'is_delete': 'bool'
    }

    attribute_map = {
        'table_id': 'tableId',
        'workflow_id': 'workflowId',
        'version': 'version',
        'graph': 'graph',
        'nodes': 'nodes',
        'links': 'links',
        'id': 'id',
        'company_id': 'companyId',
        'application_id': 'applicationId',
        'create_time': 'createTime',
        'update_time': 'updateTime',
        'create_account_id': 'createAccountId',
        'create_account_name': 'createAccountName',
        'update_account_id': 'updateAccountId',
        'update_account_name': 'updateAccountName',
        'app_name': 'appName',
        'app_color': 'appColor',
        'app_icon': 'appIcon',
        'is_delete': 'isDelete'
    }

    def __init__(self, table_id=None, workflow_id=None, version=None, graph=None, nodes=None, links=None, id=None, company_id=None, application_id=None, create_time=None, update_time=None, create_account_id=None, create_account_name=None, update_account_id=None, update_account_name=None, app_name=None, app_color=None, app_icon=None, is_delete=None):  # noqa: E501
        """TableWorkflowChartVO - a model defined in Swagger"""  # noqa: E501
        self._table_id = None
        self._workflow_id = None
        self._version = None
        self._graph = None
        self._nodes = None
        self._links = None
        self._id = None
        self._company_id = None
        self._application_id = None
        self._create_time = None
        self._update_time = None
        self._create_account_id = None
        self._create_account_name = None
        self._update_account_id = None
        self._update_account_name = None
        self._app_name = None
        self._app_color = None
        self._app_icon = None
        self._is_delete = None
        self.discriminator = None
        if table_id is not None:
            self.table_id = table_id
        if workflow_id is not None:
            self.workflow_id = workflow_id
        if version is not None:
            self.version = version
        if graph is not None:
            self.graph = graph
        if nodes is not None:
            self.nodes = nodes
        if links is not None:
            self.links = links
        if id is not None:
            self.id = id
        if company_id is not None:
            self.company_id = company_id
        if application_id is not None:
            self.application_id = application_id
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if create_account_id is not None:
            self.create_account_id = create_account_id
        if create_account_name is not None:
            self.create_account_name = create_account_name
        if update_account_id is not None:
            self.update_account_id = update_account_id
        if update_account_name is not None:
            self.update_account_name = update_account_name
        if app_name is not None:
            self.app_name = app_name
        if app_color is not None:
            self.app_color = app_color
        if app_icon is not None:
            self.app_icon = app_icon
        if is_delete is not None:
            self.is_delete = is_delete

    @property
    def table_id(self):
        """Gets the table_id of this TableWorkflowChartVO.  # noqa: E501

        数据表ID  # noqa: E501

        :return: The table_id of this TableWorkflowChartVO.  # noqa: E501
        :rtype: str
        """
        return self._table_id

    @table_id.setter
    def table_id(self, table_id):
        """Sets the table_id of this TableWorkflowChartVO.

        数据表ID  # noqa: E501

        :param table_id: The table_id of this TableWorkflowChartVO.  # noqa: E501
        :type: str
        """

        self._table_id = table_id

    @property
    def workflow_id(self):
        """Gets the workflow_id of this TableWorkflowChartVO.  # noqa: E501

        流程ID  # noqa: E501

        :return: The workflow_id of this TableWorkflowChartVO.  # noqa: E501
        :rtype: str
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        """Sets the workflow_id of this TableWorkflowChartVO.

        流程ID  # noqa: E501

        :param workflow_id: The workflow_id of this TableWorkflowChartVO.  # noqa: E501
        :type: str
        """

        self._workflow_id = workflow_id

    @property
    def version(self):
        """Gets the version of this TableWorkflowChartVO.  # noqa: E501

        版本号  # noqa: E501

        :return: The version of this TableWorkflowChartVO.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this TableWorkflowChartVO.

        版本号  # noqa: E501

        :param version: The version of this TableWorkflowChartVO.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def graph(self):
        """Gets the graph of this TableWorkflowChartVO.  # noqa: E501


        :return: The graph of this TableWorkflowChartVO.  # noqa: E501
        :rtype: Graph
        """
        return self._graph

    @graph.setter
    def graph(self, graph):
        """Sets the graph of this TableWorkflowChartVO.


        :param graph: The graph of this TableWorkflowChartVO.  # noqa: E501
        :type: Graph
        """

        self._graph = graph

    @property
    def nodes(self):
        """Gets the nodes of this TableWorkflowChartVO.  # noqa: E501

        节点列表  # noqa: E501

        :return: The nodes of this TableWorkflowChartVO.  # noqa: E501
        :rtype: list[Node]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this TableWorkflowChartVO.

        节点列表  # noqa: E501

        :param nodes: The nodes of this TableWorkflowChartVO.  # noqa: E501
        :type: list[Node]
        """

        self._nodes = nodes

    @property
    def links(self):
        """Gets the links of this TableWorkflowChartVO.  # noqa: E501

        节点连线列表  # noqa: E501

        :return: The links of this TableWorkflowChartVO.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this TableWorkflowChartVO.

        节点连线列表  # noqa: E501

        :param links: The links of this TableWorkflowChartVO.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def id(self):
        """Gets the id of this TableWorkflowChartVO.  # noqa: E501

        ID  # noqa: E501

        :return: The id of this TableWorkflowChartVO.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TableWorkflowChartVO.

        ID  # noqa: E501

        :param id: The id of this TableWorkflowChartVO.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def company_id(self):
        """Gets the company_id of this TableWorkflowChartVO.  # noqa: E501

        团队ID  # noqa: E501

        :return: The company_id of this TableWorkflowChartVO.  # noqa: E501
        :rtype: str
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        """Sets the company_id of this TableWorkflowChartVO.

        团队ID  # noqa: E501

        :param company_id: The company_id of this TableWorkflowChartVO.  # noqa: E501
        :type: str
        """

        self._company_id = company_id

    @property
    def application_id(self):
        """Gets the application_id of this TableWorkflowChartVO.  # noqa: E501

        应用ID  # noqa: E501

        :return: The application_id of this TableWorkflowChartVO.  # noqa: E501
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this TableWorkflowChartVO.

        应用ID  # noqa: E501

        :param application_id: The application_id of this TableWorkflowChartVO.  # noqa: E501
        :type: str
        """

        self._application_id = application_id

    @property
    def create_time(self):
        """Gets the create_time of this TableWorkflowChartVO.  # noqa: E501

        创建时间  # noqa: E501

        :return: The create_time of this TableWorkflowChartVO.  # noqa: E501
        :rtype: float
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this TableWorkflowChartVO.

        创建时间  # noqa: E501

        :param create_time: The create_time of this TableWorkflowChartVO.  # noqa: E501
        :type: float
        """

        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this TableWorkflowChartVO.  # noqa: E501

        最后更新时间  # noqa: E501

        :return: The update_time of this TableWorkflowChartVO.  # noqa: E501
        :rtype: float
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this TableWorkflowChartVO.

        最后更新时间  # noqa: E501

        :param update_time: The update_time of this TableWorkflowChartVO.  # noqa: E501
        :type: float
        """

        self._update_time = update_time

    @property
    def create_account_id(self):
        """Gets the create_account_id of this TableWorkflowChartVO.  # noqa: E501

        创建人ID  # noqa: E501

        :return: The create_account_id of this TableWorkflowChartVO.  # noqa: E501
        :rtype: str
        """
        return self._create_account_id

    @create_account_id.setter
    def create_account_id(self, create_account_id):
        """Sets the create_account_id of this TableWorkflowChartVO.

        创建人ID  # noqa: E501

        :param create_account_id: The create_account_id of this TableWorkflowChartVO.  # noqa: E501
        :type: str
        """

        self._create_account_id = create_account_id

    @property
    def create_account_name(self):
        """Gets the create_account_name of this TableWorkflowChartVO.  # noqa: E501

        创建人名称  # noqa: E501

        :return: The create_account_name of this TableWorkflowChartVO.  # noqa: E501
        :rtype: str
        """
        return self._create_account_name

    @create_account_name.setter
    def create_account_name(self, create_account_name):
        """Sets the create_account_name of this TableWorkflowChartVO.

        创建人名称  # noqa: E501

        :param create_account_name: The create_account_name of this TableWorkflowChartVO.  # noqa: E501
        :type: str
        """

        self._create_account_name = create_account_name

    @property
    def update_account_id(self):
        """Gets the update_account_id of this TableWorkflowChartVO.  # noqa: E501

        最后更新人ID  # noqa: E501

        :return: The update_account_id of this TableWorkflowChartVO.  # noqa: E501
        :rtype: str
        """
        return self._update_account_id

    @update_account_id.setter
    def update_account_id(self, update_account_id):
        """Sets the update_account_id of this TableWorkflowChartVO.

        最后更新人ID  # noqa: E501

        :param update_account_id: The update_account_id of this TableWorkflowChartVO.  # noqa: E501
        :type: str
        """

        self._update_account_id = update_account_id

    @property
    def update_account_name(self):
        """Gets the update_account_name of this TableWorkflowChartVO.  # noqa: E501

        最后更新人名称  # noqa: E501

        :return: The update_account_name of this TableWorkflowChartVO.  # noqa: E501
        :rtype: str
        """
        return self._update_account_name

    @update_account_name.setter
    def update_account_name(self, update_account_name):
        """Sets the update_account_name of this TableWorkflowChartVO.

        最后更新人名称  # noqa: E501

        :param update_account_name: The update_account_name of this TableWorkflowChartVO.  # noqa: E501
        :type: str
        """

        self._update_account_name = update_account_name

    @property
    def app_name(self):
        """Gets the app_name of this TableWorkflowChartVO.  # noqa: E501

        应用名称  # noqa: E501

        :return: The app_name of this TableWorkflowChartVO.  # noqa: E501
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this TableWorkflowChartVO.

        应用名称  # noqa: E501

        :param app_name: The app_name of this TableWorkflowChartVO.  # noqa: E501
        :type: str
        """

        self._app_name = app_name

    @property
    def app_color(self):
        """Gets the app_color of this TableWorkflowChartVO.  # noqa: E501

        应用颜色  # noqa: E501

        :return: The app_color of this TableWorkflowChartVO.  # noqa: E501
        :rtype: str
        """
        return self._app_color

    @app_color.setter
    def app_color(self, app_color):
        """Sets the app_color of this TableWorkflowChartVO.

        应用颜色  # noqa: E501

        :param app_color: The app_color of this TableWorkflowChartVO.  # noqa: E501
        :type: str
        """

        self._app_color = app_color

    @property
    def app_icon(self):
        """Gets the app_icon of this TableWorkflowChartVO.  # noqa: E501

        应用图标  # noqa: E501

        :return: The app_icon of this TableWorkflowChartVO.  # noqa: E501
        :rtype: str
        """
        return self._app_icon

    @app_icon.setter
    def app_icon(self, app_icon):
        """Sets the app_icon of this TableWorkflowChartVO.

        应用图标  # noqa: E501

        :param app_icon: The app_icon of this TableWorkflowChartVO.  # noqa: E501
        :type: str
        """

        self._app_icon = app_icon

    @property
    def is_delete(self):
        """Gets the is_delete of this TableWorkflowChartVO.  # noqa: E501

        是否已删除  # noqa: E501

        :return: The is_delete of this TableWorkflowChartVO.  # noqa: E501
        :rtype: bool
        """
        return self._is_delete

    @is_delete.setter
    def is_delete(self, is_delete):
        """Sets the is_delete of this TableWorkflowChartVO.

        是否已删除  # noqa: E501

        :param is_delete: The is_delete of this TableWorkflowChartVO.  # noqa: E501
        :type: bool
        """

        self._is_delete = is_delete

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
        if issubclass(TableWorkflowChartVO, dict):
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
        if not isinstance(other, TableWorkflowChartVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other