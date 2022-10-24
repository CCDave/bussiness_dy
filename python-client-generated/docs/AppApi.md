# swagger_client.AppApi

All URIs are relative to *http://uat.informat.cn/webapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_auth**](AppApi.md#app_auth) | **POST** /v2/app/auth | 应用鉴权
[**app_delete**](AppApi.md#app_delete) | **POST** /v2/app/delete | 删除应用
[**app_import**](AppApi.md#app_import) | **POST** /v2/app/import | 通过ima文件安装应用
[**app_install_template**](AppApi.md#app_install_template) | **POST** /v2/app/install_template | 通过应用模板安装应用
[**app_list**](AppApi.md#app_list) | **POST** /v2/app/list | 应用列表
[**app_member_create**](AppApi.md#app_member_create) | **POST** /v2/app_member/create | 创建应用成员
[**app_member_delete**](AppApi.md#app_member_delete) | **POST** /v2/app_member/delete | 从应用移除成员
[**app_member_get**](AppApi.md#app_member_get) | **POST** /v2/app_member/get | 查询应用成员
[**app_member_list**](AppApi.md#app_member_list) | **POST** /v2/app_member/list | 获取成员列表
[**app_member_role_create**](AppApi.md#app_member_role_create) | **POST** /v2/app_member_role/create | 创建应用角色
[**app_member_role_delete**](AppApi.md#app_member_role_delete) | **POST** /v2/app_member_role/delete | 删除应用角色
[**app_member_role_get**](AppApi.md#app_member_role_get) | **POST** /v2/app_member_role/get | 获取应用角色
[**app_member_role_list**](AppApi.md#app_member_role_list) | **POST** /v2/app_member_role/list | 获取应用角色列表
[**app_member_role_update**](AppApi.md#app_member_role_update) | **POST** /v2/app_member_role/update | 更新应用角色
[**app_member_update**](AppApi.md#app_member_update) | **POST** /v2/app_member/update | 更新应用成员
[**app_module_get**](AppApi.md#app_module_get) | **POST** /v2/app_module/get | 应用模块查询
[**app_module_list**](AppApi.md#app_module_list) | **POST** /v2/app_module/list | 应用模块列表
[**app_refresh_token**](AppApi.md#app_refresh_token) | **POST** /v2/app/refresh_token | 刷新应用accessToken
[**app_script_create**](AppApi.md#app_script_create) | **POST** /v2/app_script/create | 创建脚本
[**app_script_delete**](AppApi.md#app_script_delete) | **POST** /v2/app_script/delete | 删除脚本
[**app_script_list**](AppApi.md#app_script_list) | **POST** /v2/app_script/list | 查询脚本列表
[**app_script_load**](AppApi.md#app_script_load) | **POST** /v2/app_script/load | 装载脚本
[**app_script_update**](AppApi.md#app_script_update) | **POST** /v2/app_script/update | 编辑脚本
[**app_token**](AppApi.md#app_token) | **POST** /v2/app/token | 获取应用accessToken
[**app_version**](AppApi.md#app_version) | **POST** /v2/app/version | 系统版本号
[**table_get**](AppApi.md#table_get) | **POST** /v2/table/get | 查询数据表
[**table_list**](AppApi.md#table_list) | **POST** /v2/table/list | 数据表列表
[**table_record_batch_create**](AppApi.md#table_record_batch_create) | **POST** /v2/table_record/batch_create | 批量创建数据表记录
[**table_record_batch_delete**](AppApi.md#table_record_batch_delete) | **POST** /v2/table_record/batch_delete | 批量删除数据表记录
[**table_record_batch_update**](AppApi.md#table_record_batch_update) | **POST** /v2/table_record/batch_update | 批量编辑数据表记录
[**table_record_create**](AppApi.md#table_record_create) | **POST** /v2/table_record/create | 创建数据表记录
[**table_record_delete**](AppApi.md#table_record_delete) | **POST** /v2/table_record/delete | 删除数据表记录
[**table_record_list**](AppApi.md#table_record_list) | **POST** /v2/table_record/list | 查询数据表记录列表
[**table_record_update**](AppApi.md#table_record_update) | **POST** /v2/table_record/update | 编辑数据表记录
[**table_workflow_chart_get**](AppApi.md#table_workflow_chart_get) | **POST** /v2/table_workflow_chart/get | 通过id查询审批流程图详情
[**table_workflow_chart_list**](AppApi.md#table_workflow_chart_list) | **POST** /v2/table_workflow_chart/list | 查询审批流程图列表
[**table_workflow_get**](AppApi.md#table_workflow_get) | **POST** /v2/table_workflow/get | 通过id查询审批流程详情
[**table_workflow_instance_cancel**](AppApi.md#table_workflow_instance_cancel) | **POST** /v2/table_workflow_instance/cancel | 取消审批流程
[**table_workflow_instance_create**](AppApi.md#table_workflow_instance_create) | **POST** /v2/table_workflow_instance/create | 发起审批流程
[**table_workflow_instance_get**](AppApi.md#table_workflow_instance_get) | **POST** /v2/table_workflow_instance/get | 通过ID查询审批流程实例详情
[**table_workflow_instance_list**](AppApi.md#table_workflow_instance_list) | **POST** /v2/table_workflow_instance/list | 查询审批流程实例列表
[**table_workflow_instance_node_get**](AppApi.md#table_workflow_instance_node_get) | **POST** /v2/table_workflow_instance_node/get | 通过ID查询审批流程实例节点详情
[**table_workflow_instance_node_list**](AppApi.md#table_workflow_instance_node_list) | **POST** /v2/table_workflow_instance_node/list | 查询审批流程实例节点列表
[**table_workflow_instance_node_owner_agree**](AppApi.md#table_workflow_instance_node_owner_agree) | **POST** /v2/table_workflow_instance_node_owner/agree | 同意审批流程
[**table_workflow_instance_node_owner_get**](AppApi.md#table_workflow_instance_node_owner_get) | **POST** /v2/table_workflow_instance_node_owner/get | 通过ID查询审批流程实例节点审批人
[**table_workflow_instance_node_owner_list**](AppApi.md#table_workflow_instance_node_owner_list) | **POST** /v2/table_workflow_instance_node_owner/list | 查询审批流程实例节点审批人列表
[**table_workflow_instance_node_owner_refuse**](AppApi.md#table_workflow_instance_node_owner_refuse) | **POST** /v2/table_workflow_instance_node_owner/refuse | 拒绝审批流程
[**table_workflow_instance_node_owner_rollback**](AppApi.md#table_workflow_instance_node_owner_rollback) | **POST** /v2/table_workflow_instance_node_owner/rollback | 回退审批流程
[**table_workflow_instance_node_owner_transfer**](AppApi.md#table_workflow_instance_node_owner_transfer) | **POST** /v2/table_workflow_instance_node_owner/transfer | 转交审批流程
[**table_workflow_instance_set_owner**](AppApi.md#table_workflow_instance_set_owner) | **POST** /v2/table_workflow_instance/set_owner | 设置审批人
[**table_workflow_list**](AppApi.md#table_workflow_list) | **POST** /v2/table_workflow/list | 查询审批流程列表
[**website_material_create**](AppApi.md#website_material_create) | **POST** /v2/website_material/create | 创建网站模块素材
[**website_material_delete**](AppApi.md#website_material_delete) | **POST** /v2/website_material/delete | 删除网站模块素材
[**website_material_list**](AppApi.md#website_material_list) | **POST** /v2/website_material/list | 查询网站模块素材列表
[**website_material_update**](AppApi.md#website_material_update) | **POST** /v2/website_material/update | 更新网站模块素材
[**website_page_create**](AppApi.md#website_page_create) | **POST** /v2/website_page/create | 创建网站模块页面
[**website_page_delete**](AppApi.md#website_page_delete) | **POST** /v2/website_page/delete | 删除网站模块页面
[**website_page_get**](AppApi.md#website_page_get) | **POST** /v2/website_page/get | 通过ID查询网站模板页面
[**website_page_list**](AppApi.md#website_page_list) | **POST** /v2/website_page/list | 查询网站模板页面列表
[**website_page_publish**](AppApi.md#website_page_publish) | **POST** /v2/website_page/publish | 发布网站模块页面
[**website_page_update**](AppApi.md#website_page_update) | **POST** /v2/website_page/update | 编辑网站模块页面

# **app_auth**
> AppAuthResponse app_auth(body, oid=oid, company_id=company_id, app_id=app_id)

应用鉴权

应用鉴权

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.AppAuthRequest() # AppAuthRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 应用鉴权
    api_response = api_instance.app_auth(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->app_auth: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AppAuthRequest**](AppAuthRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**AppAuthResponse**](AppAuthResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_delete**
> AppDeleteResponse app_delete(body, oid=oid, company_id=company_id, app_id=app_id)

删除应用

删除应用

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.AppDeleteRequest() # AppDeleteRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 删除应用
    api_response = api_instance.app_delete(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->app_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AppDeleteRequest**](AppDeleteRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**AppDeleteResponse**](AppDeleteResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_import**
> AppImportResponse app_import(body, oid=oid, company_id=company_id, app_id=app_id)

通过ima文件安装应用

通过ima文件安装应用

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.AppImportRequest() # AppImportRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 通过ima文件安装应用
    api_response = api_instance.app_import(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->app_import: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AppImportRequest**](AppImportRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**AppImportResponse**](AppImportResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_install_template**
> AppInstallTemplateResponse app_install_template(body, oid=oid, company_id=company_id, app_id=app_id)

通过应用模板安装应用

通过应用模板安装应用

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.AppInstallTemplateRequest() # AppInstallTemplateRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 通过应用模板安装应用
    api_response = api_instance.app_install_template(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->app_install_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AppInstallTemplateRequest**](AppInstallTemplateRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**AppInstallTemplateResponse**](AppInstallTemplateResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_list**
> AppListResponse app_list(body, oid=oid, company_id=company_id, app_id=app_id)

应用列表

应用列表

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.AppListRequest() # AppListRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 应用列表
    api_response = api_instance.app_list(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->app_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AppListRequest**](AppListRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**AppListResponse**](AppListResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_member_create**
> AppMemberCreateResponse app_member_create(body, oid=oid, company_id=company_id, app_id=app_id)

创建应用成员

创建应用成员

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.AppMemberCreateRequest() # AppMemberCreateRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 创建应用成员
    api_response = api_instance.app_member_create(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->app_member_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AppMemberCreateRequest**](AppMemberCreateRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**AppMemberCreateResponse**](AppMemberCreateResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_member_delete**
> AppMemberDeleteResponse app_member_delete(body, oid=oid, company_id=company_id, app_id=app_id)

从应用移除成员

从应用移除成员

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.AppMemberDeleteRequest() # AppMemberDeleteRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 从应用移除成员
    api_response = api_instance.app_member_delete(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->app_member_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AppMemberDeleteRequest**](AppMemberDeleteRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**AppMemberDeleteResponse**](AppMemberDeleteResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_member_get**
> AppMemberGetResponse app_member_get(body, oid=oid, company_id=company_id, app_id=app_id)

查询应用成员

查询应用成员

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.AppMemberGetRequest() # AppMemberGetRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 查询应用成员
    api_response = api_instance.app_member_get(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->app_member_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AppMemberGetRequest**](AppMemberGetRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**AppMemberGetResponse**](AppMemberGetResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_member_list**
> AppMemberListResponse app_member_list(body, oid=oid, company_id=company_id, app_id=app_id)

获取成员列表

获取成员列表

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.AppMemberListRequest() # AppMemberListRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 获取成员列表
    api_response = api_instance.app_member_list(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->app_member_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AppMemberListRequest**](AppMemberListRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**AppMemberListResponse**](AppMemberListResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_member_role_create**
> AppMemberRoleCreateResponse app_member_role_create(body, oid=oid, company_id=company_id, app_id=app_id)

创建应用角色

创建应用角色

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.AppMemberRoleCreateRequest() # AppMemberRoleCreateRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 创建应用角色
    api_response = api_instance.app_member_role_create(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->app_member_role_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AppMemberRoleCreateRequest**](AppMemberRoleCreateRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**AppMemberRoleCreateResponse**](AppMemberRoleCreateResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_member_role_delete**
> AppMemberRoleDeleteResponse app_member_role_delete(body, oid=oid, company_id=company_id, app_id=app_id)

删除应用角色

删除应用角色

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.AppMemberRoleDeleteRequest() # AppMemberRoleDeleteRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 删除应用角色
    api_response = api_instance.app_member_role_delete(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->app_member_role_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AppMemberRoleDeleteRequest**](AppMemberRoleDeleteRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**AppMemberRoleDeleteResponse**](AppMemberRoleDeleteResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_member_role_get**
> AppMemberRoleGetResponse app_member_role_get(body, oid=oid, company_id=company_id, app_id=app_id)

获取应用角色

获取应用角色

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.AppMemberRoleGetRequest() # AppMemberRoleGetRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 获取应用角色
    api_response = api_instance.app_member_role_get(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->app_member_role_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AppMemberRoleGetRequest**](AppMemberRoleGetRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**AppMemberRoleGetResponse**](AppMemberRoleGetResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_member_role_list**
> AppMemberRoleListResponse app_member_role_list(body, oid=oid, company_id=company_id, app_id=app_id)

获取应用角色列表

获取应用角色列表

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.AppMemberRoleListRequest() # AppMemberRoleListRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 获取应用角色列表
    api_response = api_instance.app_member_role_list(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->app_member_role_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AppMemberRoleListRequest**](AppMemberRoleListRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**AppMemberRoleListResponse**](AppMemberRoleListResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_member_role_update**
> AppMemberRoleUpdateResponse app_member_role_update(body, oid=oid, company_id=company_id, app_id=app_id)

更新应用角色

更新应用角色

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.AppMemberRoleUpdateRequest() # AppMemberRoleUpdateRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 更新应用角色
    api_response = api_instance.app_member_role_update(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->app_member_role_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AppMemberRoleUpdateRequest**](AppMemberRoleUpdateRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**AppMemberRoleUpdateResponse**](AppMemberRoleUpdateResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_member_update**
> AppMemberUpdateResponse app_member_update(body, oid=oid, company_id=company_id, app_id=app_id)

更新应用成员

更新应用成员

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.AppMemberUpdateRequest() # AppMemberUpdateRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 更新应用成员
    api_response = api_instance.app_member_update(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->app_member_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AppMemberUpdateRequest**](AppMemberUpdateRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**AppMemberUpdateResponse**](AppMemberUpdateResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_module_get**
> AppModuleGetResponse app_module_get(body, oid=oid, company_id=company_id, app_id=app_id)

应用模块查询

应用模块查询

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.AppModuleGetRequest() # AppModuleGetRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 应用模块查询
    api_response = api_instance.app_module_get(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->app_module_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AppModuleGetRequest**](AppModuleGetRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**AppModuleGetResponse**](AppModuleGetResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_module_list**
> AppModuleListResponse app_module_list(body, oid=oid, company_id=company_id, app_id=app_id)

应用模块列表

应用模块列表

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.AppModuleListRequest() # AppModuleListRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 应用模块列表
    api_response = api_instance.app_module_list(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->app_module_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AppModuleListRequest**](AppModuleListRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**AppModuleListResponse**](AppModuleListResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_refresh_token**
> AppRefreshTokenResponse app_refresh_token(body, oid=oid, company_id=company_id, app_id=app_id)

刷新应用accessToken

刷新应用accessToken

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.AppRefreshTokenRequest() # AppRefreshTokenRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 刷新应用accessToken
    api_response = api_instance.app_refresh_token(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->app_refresh_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AppRefreshTokenRequest**](AppRefreshTokenRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**AppRefreshTokenResponse**](AppRefreshTokenResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_script_create**
> AppScriptCreateResponse app_script_create(body, oid=oid, company_id=company_id, app_id=app_id)

创建脚本

创建脚本

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.AppScriptCreateRequest() # AppScriptCreateRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 创建脚本
    api_response = api_instance.app_script_create(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->app_script_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AppScriptCreateRequest**](AppScriptCreateRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**AppScriptCreateResponse**](AppScriptCreateResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_script_delete**
> AppScriptDeleteResponse app_script_delete(body, oid=oid, company_id=company_id, app_id=app_id)

删除脚本

删除脚本

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.AppScriptDeleteRequest() # AppScriptDeleteRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 删除脚本
    api_response = api_instance.app_script_delete(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->app_script_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AppScriptDeleteRequest**](AppScriptDeleteRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**AppScriptDeleteResponse**](AppScriptDeleteResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_script_list**
> AppScriptListResponse app_script_list(body, oid=oid, company_id=company_id, app_id=app_id)

查询脚本列表

查询脚本列表

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.AppScriptListRequest() # AppScriptListRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 查询脚本列表
    api_response = api_instance.app_script_list(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->app_script_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AppScriptListRequest**](AppScriptListRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**AppScriptListResponse**](AppScriptListResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_script_load**
> APIResponse app_script_load(body, oid=oid, company_id=company_id, app_id=app_id)

装载脚本

装载脚本

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.AppScriptLoadRequest() # AppScriptLoadRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 装载脚本
    api_response = api_instance.app_script_load(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->app_script_load: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AppScriptLoadRequest**](AppScriptLoadRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**APIResponse**](APIResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_script_update**
> AppScriptUpdateResponse app_script_update(body, oid=oid, company_id=company_id, app_id=app_id)

编辑脚本

编辑脚本

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.AppScriptUpdateRequest() # AppScriptUpdateRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 编辑脚本
    api_response = api_instance.app_script_update(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->app_script_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AppScriptUpdateRequest**](AppScriptUpdateRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**AppScriptUpdateResponse**](AppScriptUpdateResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_token**
> AppTokenResponse app_token(body)

获取应用accessToken

获取应用accessToken

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AppApi()
body = swagger_client.AppTokenRequest() # AppTokenRequest | 

try:
    # 获取应用accessToken
    api_response = api_instance.app_token(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->app_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AppTokenRequest**](AppTokenRequest.md)|  | 

### Return type

[**AppTokenResponse**](AppTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_version**
> AppVersionResponse app_version(body, oid=oid, company_id=company_id, app_id=app_id)

系统版本号

系统版本号

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.AppVersionRequest() # AppVersionRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 系统版本号
    api_response = api_instance.app_version(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->app_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AppVersionRequest**](AppVersionRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**AppVersionResponse**](AppVersionResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **table_get**
> TableGetResponse table_get(body, oid=oid, company_id=company_id, app_id=app_id)

查询数据表

查询数据表

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.TableGetRequest() # TableGetRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 查询数据表
    api_response = api_instance.table_get(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->table_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TableGetRequest**](TableGetRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**TableGetResponse**](TableGetResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **table_list**
> TableListResponse table_list(body, oid=oid, company_id=company_id, app_id=app_id)

数据表列表

数据表列表

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.TableListRequest() # TableListRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 数据表列表
    api_response = api_instance.table_list(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->table_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TableListRequest**](TableListRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**TableListResponse**](TableListResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **table_record_batch_create**
> TableRecordBatchCreateResponse table_record_batch_create(body, oid=oid, company_id=company_id, app_id=app_id)

批量创建数据表记录

批量创建数据表记录

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.TableRecordBatchCreateRequest() # TableRecordBatchCreateRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 批量创建数据表记录
    api_response = api_instance.table_record_batch_create(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->table_record_batch_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TableRecordBatchCreateRequest**](TableRecordBatchCreateRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**TableRecordBatchCreateResponse**](TableRecordBatchCreateResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **table_record_batch_delete**
> TableRecordBatchDeleteResponse table_record_batch_delete(body, oid=oid, company_id=company_id, app_id=app_id)

批量删除数据表记录

批量删除数据表记录

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.TableRecordBatchDeleteRequest() # TableRecordBatchDeleteRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 批量删除数据表记录
    api_response = api_instance.table_record_batch_delete(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->table_record_batch_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TableRecordBatchDeleteRequest**](TableRecordBatchDeleteRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**TableRecordBatchDeleteResponse**](TableRecordBatchDeleteResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **table_record_batch_update**
> TableRecordBatchUpdateResponse table_record_batch_update(body, oid=oid, company_id=company_id, app_id=app_id)

批量编辑数据表记录

批量编辑数据表记录

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.TableRecordBatchUpdateRequest() # TableRecordBatchUpdateRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 批量编辑数据表记录
    api_response = api_instance.table_record_batch_update(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->table_record_batch_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TableRecordBatchUpdateRequest**](TableRecordBatchUpdateRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**TableRecordBatchUpdateResponse**](TableRecordBatchUpdateResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **table_record_create**
> TableRecordCreateResponse table_record_create(body, oid=oid, company_id=company_id, app_id=app_id)

创建数据表记录

创建数据表记录

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.TableRecordCreateRequest() # TableRecordCreateRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 创建数据表记录
    api_response = api_instance.table_record_create(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->table_record_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TableRecordCreateRequest**](TableRecordCreateRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**TableRecordCreateResponse**](TableRecordCreateResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **table_record_delete**
> TableRecordDeleteResponse table_record_delete(body, oid=oid, company_id=company_id, app_id=app_id)

删除数据表记录

删除数据表记录

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.TableRecordDeleteRequest() # TableRecordDeleteRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 删除数据表记录
    api_response = api_instance.table_record_delete(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->table_record_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TableRecordDeleteRequest**](TableRecordDeleteRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**TableRecordDeleteResponse**](TableRecordDeleteResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **table_record_list**
> TableRecordListResponse table_record_list(body, oid=oid, company_id=company_id, app_id=app_id)

查询数据表记录列表

查询数据表记录列表

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.TableRecordListRequest() # TableRecordListRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 查询数据表记录列表
    api_response = api_instance.table_record_list(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->table_record_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TableRecordListRequest**](TableRecordListRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**TableRecordListResponse**](TableRecordListResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **table_record_update**
> TableRecordUpdateResponse table_record_update(body, oid=oid, company_id=company_id, app_id=app_id)

编辑数据表记录

编辑数据表记录

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.TableRecordUpdateRequest() # TableRecordUpdateRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 编辑数据表记录
    api_response = api_instance.table_record_update(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->table_record_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TableRecordUpdateRequest**](TableRecordUpdateRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**TableRecordUpdateResponse**](TableRecordUpdateResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **table_workflow_chart_get**
> TableWorkflowChartGetResponse table_workflow_chart_get(body, oid=oid, company_id=company_id, app_id=app_id)

通过id查询审批流程图详情

通过id查询审批流程图详情

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.TableWorkflowChartGetRequest() # TableWorkflowChartGetRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 通过id查询审批流程图详情
    api_response = api_instance.table_workflow_chart_get(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->table_workflow_chart_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TableWorkflowChartGetRequest**](TableWorkflowChartGetRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**TableWorkflowChartGetResponse**](TableWorkflowChartGetResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **table_workflow_chart_list**
> TableWorkflowChartListResponse table_workflow_chart_list(body, oid=oid, company_id=company_id, app_id=app_id)

查询审批流程图列表

查询审批流程图列表

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.TableWorkflowChartListRequest() # TableWorkflowChartListRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 查询审批流程图列表
    api_response = api_instance.table_workflow_chart_list(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->table_workflow_chart_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TableWorkflowChartListRequest**](TableWorkflowChartListRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**TableWorkflowChartListResponse**](TableWorkflowChartListResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **table_workflow_get**
> TableWorkflowGetResponse table_workflow_get(body, oid=oid, company_id=company_id, app_id=app_id)

通过id查询审批流程详情

通过id查询审批流程详情

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.TableWorkflowGetRequest() # TableWorkflowGetRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 通过id查询审批流程详情
    api_response = api_instance.table_workflow_get(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->table_workflow_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TableWorkflowGetRequest**](TableWorkflowGetRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**TableWorkflowGetResponse**](TableWorkflowGetResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **table_workflow_instance_cancel**
> TableWorkflowInstanceCancelResponse table_workflow_instance_cancel(body, oid=oid, company_id=company_id, app_id=app_id)

取消审批流程

取消审批流程

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.TableWorkflowInstanceCancelRequest() # TableWorkflowInstanceCancelRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 取消审批流程
    api_response = api_instance.table_workflow_instance_cancel(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->table_workflow_instance_cancel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TableWorkflowInstanceCancelRequest**](TableWorkflowInstanceCancelRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**TableWorkflowInstanceCancelResponse**](TableWorkflowInstanceCancelResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **table_workflow_instance_create**
> TableWorkflowInstanceCreateResponse table_workflow_instance_create(body, oid=oid, company_id=company_id, app_id=app_id)

发起审批流程

发起审批流程

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.TableWorkflowInstanceCreateRequest() # TableWorkflowInstanceCreateRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 发起审批流程
    api_response = api_instance.table_workflow_instance_create(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->table_workflow_instance_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TableWorkflowInstanceCreateRequest**](TableWorkflowInstanceCreateRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**TableWorkflowInstanceCreateResponse**](TableWorkflowInstanceCreateResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **table_workflow_instance_get**
> TableWorkflowInstanceGetResponse table_workflow_instance_get(body, oid=oid, company_id=company_id, app_id=app_id)

通过ID查询审批流程实例详情

通过ID查询审批流程实例详情

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.TableWorkflowInstanceGetRequest() # TableWorkflowInstanceGetRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 通过ID查询审批流程实例详情
    api_response = api_instance.table_workflow_instance_get(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->table_workflow_instance_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TableWorkflowInstanceGetRequest**](TableWorkflowInstanceGetRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**TableWorkflowInstanceGetResponse**](TableWorkflowInstanceGetResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **table_workflow_instance_list**
> TableWorkflowInstanceListResponse table_workflow_instance_list(body, oid=oid, company_id=company_id, app_id=app_id)

查询审批流程实例列表

查询审批流程实例列表

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.TableWorkflowInstanceListRequest() # TableWorkflowInstanceListRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 查询审批流程实例列表
    api_response = api_instance.table_workflow_instance_list(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->table_workflow_instance_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TableWorkflowInstanceListRequest**](TableWorkflowInstanceListRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**TableWorkflowInstanceListResponse**](TableWorkflowInstanceListResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **table_workflow_instance_node_get**
> TableWorkflowInstanceNodeGetResponse table_workflow_instance_node_get(body, oid=oid, company_id=company_id, app_id=app_id)

通过ID查询审批流程实例节点详情

通过ID查询审批流程实例节点详情

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.TableWorkflowInstanceNodeGetRequest() # TableWorkflowInstanceNodeGetRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 通过ID查询审批流程实例节点详情
    api_response = api_instance.table_workflow_instance_node_get(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->table_workflow_instance_node_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TableWorkflowInstanceNodeGetRequest**](TableWorkflowInstanceNodeGetRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**TableWorkflowInstanceNodeGetResponse**](TableWorkflowInstanceNodeGetResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **table_workflow_instance_node_list**
> TableWorkflowInstanceNodeListResponse table_workflow_instance_node_list(body, oid=oid, company_id=company_id, app_id=app_id)

查询审批流程实例节点列表

查询审批流程实例节点列表

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.TableWorkflowInstanceNodeListRequest() # TableWorkflowInstanceNodeListRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 查询审批流程实例节点列表
    api_response = api_instance.table_workflow_instance_node_list(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->table_workflow_instance_node_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TableWorkflowInstanceNodeListRequest**](TableWorkflowInstanceNodeListRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**TableWorkflowInstanceNodeListResponse**](TableWorkflowInstanceNodeListResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **table_workflow_instance_node_owner_agree**
> TableWorkflowInstanceNodeOwnerAgreeResponse table_workflow_instance_node_owner_agree(body, oid=oid, company_id=company_id, app_id=app_id)

同意审批流程

同意审批流程

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.TableWorkflowInstanceNodeOwnerAgreeRequest() # TableWorkflowInstanceNodeOwnerAgreeRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 同意审批流程
    api_response = api_instance.table_workflow_instance_node_owner_agree(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->table_workflow_instance_node_owner_agree: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TableWorkflowInstanceNodeOwnerAgreeRequest**](TableWorkflowInstanceNodeOwnerAgreeRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**TableWorkflowInstanceNodeOwnerAgreeResponse**](TableWorkflowInstanceNodeOwnerAgreeResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **table_workflow_instance_node_owner_get**
> TableWorkflowInstanceNodeOwnerGetResponse table_workflow_instance_node_owner_get(body, oid=oid, company_id=company_id, app_id=app_id)

通过ID查询审批流程实例节点审批人

通过ID查询审批流程实例节点审批人

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.TableWorkflowInstanceNodeOwnerGetRequest() # TableWorkflowInstanceNodeOwnerGetRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 通过ID查询审批流程实例节点审批人
    api_response = api_instance.table_workflow_instance_node_owner_get(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->table_workflow_instance_node_owner_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TableWorkflowInstanceNodeOwnerGetRequest**](TableWorkflowInstanceNodeOwnerGetRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**TableWorkflowInstanceNodeOwnerGetResponse**](TableWorkflowInstanceNodeOwnerGetResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **table_workflow_instance_node_owner_list**
> TableWorkflowInstanceNodeOwnerListResponse table_workflow_instance_node_owner_list(body, oid=oid, company_id=company_id, app_id=app_id)

查询审批流程实例节点审批人列表

查询审批流程实例节点审批人列表

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.TableWorkflowInstanceNodeOwnerListRequest() # TableWorkflowInstanceNodeOwnerListRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 查询审批流程实例节点审批人列表
    api_response = api_instance.table_workflow_instance_node_owner_list(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->table_workflow_instance_node_owner_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TableWorkflowInstanceNodeOwnerListRequest**](TableWorkflowInstanceNodeOwnerListRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**TableWorkflowInstanceNodeOwnerListResponse**](TableWorkflowInstanceNodeOwnerListResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **table_workflow_instance_node_owner_refuse**
> TableWorkflowInstanceNodeOwnerRefuseResponse table_workflow_instance_node_owner_refuse(body, oid=oid, company_id=company_id, app_id=app_id)

拒绝审批流程

拒绝审批流程

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.TableWorkflowInstanceNodeOwnerRefuseRequest() # TableWorkflowInstanceNodeOwnerRefuseRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 拒绝审批流程
    api_response = api_instance.table_workflow_instance_node_owner_refuse(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->table_workflow_instance_node_owner_refuse: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TableWorkflowInstanceNodeOwnerRefuseRequest**](TableWorkflowInstanceNodeOwnerRefuseRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**TableWorkflowInstanceNodeOwnerRefuseResponse**](TableWorkflowInstanceNodeOwnerRefuseResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **table_workflow_instance_node_owner_rollback**
> TableWorkflowInstanceNodeOwnerRollbackResponse table_workflow_instance_node_owner_rollback(body, oid=oid, company_id=company_id, app_id=app_id)

回退审批流程

回退审批流程

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.TableWorkflowInstanceNodeOwnerRollbackRequest() # TableWorkflowInstanceNodeOwnerRollbackRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 回退审批流程
    api_response = api_instance.table_workflow_instance_node_owner_rollback(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->table_workflow_instance_node_owner_rollback: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TableWorkflowInstanceNodeOwnerRollbackRequest**](TableWorkflowInstanceNodeOwnerRollbackRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**TableWorkflowInstanceNodeOwnerRollbackResponse**](TableWorkflowInstanceNodeOwnerRollbackResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **table_workflow_instance_node_owner_transfer**
> TableWorkflowInstanceNodeOwnerTransferResponse table_workflow_instance_node_owner_transfer(body, oid=oid, company_id=company_id, app_id=app_id)

转交审批流程

转交审批流程

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.TableWorkflowInstanceNodeOwnerTransferRequest() # TableWorkflowInstanceNodeOwnerTransferRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 转交审批流程
    api_response = api_instance.table_workflow_instance_node_owner_transfer(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->table_workflow_instance_node_owner_transfer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TableWorkflowInstanceNodeOwnerTransferRequest**](TableWorkflowInstanceNodeOwnerTransferRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**TableWorkflowInstanceNodeOwnerTransferResponse**](TableWorkflowInstanceNodeOwnerTransferResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **table_workflow_instance_set_owner**
> TableWorkflowInstanceSetOwnerResponse table_workflow_instance_set_owner(body, oid=oid, company_id=company_id, app_id=app_id)

设置审批人

设置审批人

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.TableWorkflowInstanceSetOwnerRequest() # TableWorkflowInstanceSetOwnerRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 设置审批人
    api_response = api_instance.table_workflow_instance_set_owner(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->table_workflow_instance_set_owner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TableWorkflowInstanceSetOwnerRequest**](TableWorkflowInstanceSetOwnerRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**TableWorkflowInstanceSetOwnerResponse**](TableWorkflowInstanceSetOwnerResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **table_workflow_list**
> TableWorkflowListResponse table_workflow_list(body, oid=oid, company_id=company_id, app_id=app_id)

查询审批流程列表

查询审批流程列表

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.TableWorkflowListRequest() # TableWorkflowListRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 查询审批流程列表
    api_response = api_instance.table_workflow_list(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->table_workflow_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TableWorkflowListRequest**](TableWorkflowListRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**TableWorkflowListResponse**](TableWorkflowListResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **website_material_create**
> WebsiteMaterialCreateResponse website_material_create(body, oid=oid, company_id=company_id, app_id=app_id)

创建网站模块素材

创建网站模块素材

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.WebsiteMaterialCreateRequest() # WebsiteMaterialCreateRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 创建网站模块素材
    api_response = api_instance.website_material_create(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->website_material_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WebsiteMaterialCreateRequest**](WebsiteMaterialCreateRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**WebsiteMaterialCreateResponse**](WebsiteMaterialCreateResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **website_material_delete**
> WebsiteMaterialDeleteResponse website_material_delete(body, oid=oid, company_id=company_id, app_id=app_id)

删除网站模块素材

删除网站模块素材

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.WebsiteMaterialDeleteRequest() # WebsiteMaterialDeleteRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 删除网站模块素材
    api_response = api_instance.website_material_delete(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->website_material_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WebsiteMaterialDeleteRequest**](WebsiteMaterialDeleteRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**WebsiteMaterialDeleteResponse**](WebsiteMaterialDeleteResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **website_material_list**
> WebsiteMaterialListResponse website_material_list(body, oid=oid, company_id=company_id, app_id=app_id)

查询网站模块素材列表

查询网站模块素材列表

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.WebsiteMaterialListRequest() # WebsiteMaterialListRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 查询网站模块素材列表
    api_response = api_instance.website_material_list(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->website_material_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WebsiteMaterialListRequest**](WebsiteMaterialListRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**WebsiteMaterialListResponse**](WebsiteMaterialListResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **website_material_update**
> WebsiteMaterialUpdateResponse website_material_update(body, oid=oid, company_id=company_id, app_id=app_id)

更新网站模块素材

更新网站模块素材

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.WebsiteMaterialUpdateRequest() # WebsiteMaterialUpdateRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 更新网站模块素材
    api_response = api_instance.website_material_update(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->website_material_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WebsiteMaterialUpdateRequest**](WebsiteMaterialUpdateRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**WebsiteMaterialUpdateResponse**](WebsiteMaterialUpdateResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **website_page_create**
> WebsitePageCreateResponse website_page_create(body, oid=oid, company_id=company_id, app_id=app_id)

创建网站模块页面

创建网站模块页面

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.WebsitePageCreateRequest() # WebsitePageCreateRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 创建网站模块页面
    api_response = api_instance.website_page_create(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->website_page_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WebsitePageCreateRequest**](WebsitePageCreateRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**WebsitePageCreateResponse**](WebsitePageCreateResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **website_page_delete**
> WebsitePageDeleteResponse website_page_delete(body, oid=oid, company_id=company_id, app_id=app_id)

删除网站模块页面

删除网站模块页面

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.WebsitePageDeleteRequest() # WebsitePageDeleteRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 删除网站模块页面
    api_response = api_instance.website_page_delete(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->website_page_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WebsitePageDeleteRequest**](WebsitePageDeleteRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**WebsitePageDeleteResponse**](WebsitePageDeleteResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **website_page_get**
> WebsitePageGetResponse website_page_get(body, oid=oid, company_id=company_id, app_id=app_id)

通过ID查询网站模板页面

通过ID查询网站模板页面

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.WebsitePageGetRequest() # WebsitePageGetRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 通过ID查询网站模板页面
    api_response = api_instance.website_page_get(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->website_page_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WebsitePageGetRequest**](WebsitePageGetRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**WebsitePageGetResponse**](WebsitePageGetResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **website_page_list**
> WebsitePageListResponse website_page_list(body, oid=oid, company_id=company_id, app_id=app_id)

查询网站模板页面列表

查询网站模板页面列表

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.WebsitePageListRequest() # WebsitePageListRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 查询网站模板页面列表
    api_response = api_instance.website_page_list(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->website_page_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WebsitePageListRequest**](WebsitePageListRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**WebsitePageListResponse**](WebsitePageListResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **website_page_publish**
> WebsitePagePublishResponse website_page_publish(body, oid=oid, company_id=company_id, app_id=app_id)

发布网站模块页面

发布网站模块页面

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.WebsitePagePublishRequest() # WebsitePagePublishRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 发布网站模块页面
    api_response = api_instance.website_page_publish(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->website_page_publish: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WebsitePagePublishRequest**](WebsitePagePublishRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**WebsitePagePublishResponse**](WebsitePagePublishResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **website_page_update**
> WebsitePageUpdateResponse website_page_update(body, oid=oid, company_id=company_id, app_id=app_id)

编辑网站模块页面

编辑网站模块页面

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.WebsitePageUpdateRequest() # WebsitePageUpdateRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 编辑网站模块页面
    api_response = api_instance.website_page_update(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->website_page_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WebsitePageUpdateRequest**](WebsitePageUpdateRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**WebsitePageUpdateResponse**](WebsitePageUpdateResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

