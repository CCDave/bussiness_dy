# swagger_client.AdminApi

All URIs are relative to *http://uat.informat.cn/webapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_account_batch_delete**](AdminApi.md#admin_account_batch_delete) | **POST** /v2/admin_account/batch_delete | 从团队批量移除成员
[**admin_account_create**](AdminApi.md#admin_account_create) | **POST** /v2/admin_account/create | 创建用户
[**admin_account_delete**](AdminApi.md#admin_account_delete) | **POST** /v2/admin_account/delete | 删除用户
[**admin_account_get**](AdminApi.md#admin_account_get) | **POST** /v2/admin_account/get | 查询用户信息
[**admin_account_join_company**](AdminApi.md#admin_account_join_company) | **POST** /v2/admin_account/join_company | 指定用户加入指定团队
[**admin_account_list**](AdminApi.md#admin_account_list) | **POST** /v2/admin_account/list | 获取用户列表
[**admin_account_password**](AdminApi.md#admin_account_password) | **POST** /v2/admin_account/password | 更改指定用户的密码
[**admin_account_update**](AdminApi.md#admin_account_update) | **POST** /v2/admin_account/update | 更改用户信息
[**admin_app_template_delete**](AdminApi.md#admin_app_template_delete) | **POST** /v2/admin_app_template/delete | 删除应用模板
[**admin_app_template_get**](AdminApi.md#admin_app_template_get) | **POST** /v2/admin_app_template/get | 根据id获取应用模板
[**admin_app_template_import**](AdminApi.md#admin_app_template_import) | **POST** /v2/admin_app_template/import | 导入应用模板
[**admin_app_template_list**](AdminApi.md#admin_app_template_list) | **POST** /v2/admin_app_template/list | 获取应用模板列表
[**admin_app_template_update**](AdminApi.md#admin_app_template_update) | **POST** /v2/admin_app_template/update | 更新应用模板
[**admin_company_delete**](AdminApi.md#admin_company_delete) | **POST** /v2/admin_company/delete | 删除团队
[**admin_company_get**](AdminApi.md#admin_company_get) | **POST** /v2/admin_company/get | 根据ID获取团队
[**admin_company_list**](AdminApi.md#admin_company_list) | **POST** /v2/admin_company/list | 获取团队列表
[**admin_company_pro**](AdminApi.md#admin_company_pro) | **POST** /v2/admin_company/pro | 设置团队版本为专业版
[**admin_config_list**](AdminApi.md#admin_config_list) | **POST** /v2/admin_config/list | 查询配置列表
[**admin_config_update**](AdminApi.md#admin_config_update) | **POST** /v2/admin_config/update | 更新配置信息
[**admin_import_license**](AdminApi.md#admin_import_license) | **POST** /v2/admin/import_license | 导入许可证
[**admin_import_sub_license**](AdminApi.md#admin_import_sub_license) | **POST** /v2/admin/import_sub_license | 导入子许可证
[**admin_refresh_token**](AdminApi.md#admin_refresh_token) | **POST** /v2/admin/refresh_token | 刷新adminToken
[**admin_token**](AdminApi.md#admin_token) | **POST** /v2/admin/token | 获取adminToken
[**admin_version**](AdminApi.md#admin_version) | **POST** /v2/admin/version | 系统版本号

# **admin_account_batch_delete**
> APIResponse admin_account_batch_delete(body, oid=oid, company_id=company_id, app_id=app_id)

从团队批量移除成员

从团队批量移除成员

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AdminApi(swagger_client.ApiClient(configuration))
body = swagger_client.AdminCompanyMemberBatchDeleteRequest() # AdminCompanyMemberBatchDeleteRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 从团队批量移除成员
    api_response = api_instance.admin_account_batch_delete(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_account_batch_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AdminCompanyMemberBatchDeleteRequest**](AdminCompanyMemberBatchDeleteRequest.md)|  | 
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

# **admin_account_create**
> AdminAccountCreateResponse admin_account_create(body, oid=oid, company_id=company_id, app_id=app_id)

创建用户

创建用户

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AdminApi(swagger_client.ApiClient(configuration))
body = swagger_client.AdminAccountCreateRequest() # AdminAccountCreateRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 创建用户
    api_response = api_instance.admin_account_create(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_account_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AdminAccountCreateRequest**](AdminAccountCreateRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**AdminAccountCreateResponse**](AdminAccountCreateResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_account_delete**
> AdminAccountDeleteResponse admin_account_delete(body, oid=oid, company_id=company_id, app_id=app_id)

删除用户

删除用户

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AdminApi(swagger_client.ApiClient(configuration))
body = swagger_client.AdminAccountDeleteRequest() # AdminAccountDeleteRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 删除用户
    api_response = api_instance.admin_account_delete(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_account_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AdminAccountDeleteRequest**](AdminAccountDeleteRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**AdminAccountDeleteResponse**](AdminAccountDeleteResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_account_get**
> AdminAccountGetResponse admin_account_get(body, oid=oid, company_id=company_id, app_id=app_id)

查询用户信息

查询用户信息

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AdminApi(swagger_client.ApiClient(configuration))
body = swagger_client.AdminAccountGetRequest() # AdminAccountGetRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 查询用户信息
    api_response = api_instance.admin_account_get(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_account_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AdminAccountGetRequest**](AdminAccountGetRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**AdminAccountGetResponse**](AdminAccountGetResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_account_join_company**
> APIResponse admin_account_join_company(body, oid=oid, company_id=company_id, app_id=app_id)

指定用户加入指定团队

指定用户加入指定团队

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AdminApi(swagger_client.ApiClient(configuration))
body = swagger_client.AccountMemberJoinCompanyRequest() # AccountMemberJoinCompanyRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 指定用户加入指定团队
    api_response = api_instance.admin_account_join_company(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_account_join_company: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountMemberJoinCompanyRequest**](AccountMemberJoinCompanyRequest.md)|  | 
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

# **admin_account_list**
> AdminAccountListResponse admin_account_list(body, oid=oid, company_id=company_id, app_id=app_id)

获取用户列表

获取用户列表

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AdminApi(swagger_client.ApiClient(configuration))
body = swagger_client.AdminAccountListRequest() # AdminAccountListRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 获取用户列表
    api_response = api_instance.admin_account_list(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_account_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AdminAccountListRequest**](AdminAccountListRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**AdminAccountListResponse**](AdminAccountListResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_account_password**
> AdminAccountPasswordResponse admin_account_password(body, oid=oid, company_id=company_id, app_id=app_id)

更改指定用户的密码

更改指定用户的密码

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AdminApi(swagger_client.ApiClient(configuration))
body = swagger_client.AdminAccountPasswordRequest() # AdminAccountPasswordRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 更改指定用户的密码
    api_response = api_instance.admin_account_password(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_account_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AdminAccountPasswordRequest**](AdminAccountPasswordRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**AdminAccountPasswordResponse**](AdminAccountPasswordResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_account_update**
> AdminAccountUpdateResponse admin_account_update(body, oid=oid, company_id=company_id, app_id=app_id)

更改用户信息

更改用户信息

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AdminApi(swagger_client.ApiClient(configuration))
body = swagger_client.AdminAccountUpdateRequest() # AdminAccountUpdateRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 更改用户信息
    api_response = api_instance.admin_account_update(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_account_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AdminAccountUpdateRequest**](AdminAccountUpdateRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**AdminAccountUpdateResponse**](AdminAccountUpdateResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_app_template_delete**
> AdminAppTemplateDeleteResponse admin_app_template_delete(body, oid=oid, company_id=company_id, app_id=app_id)

删除应用模板

删除应用模板

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AdminApi(swagger_client.ApiClient(configuration))
body = swagger_client.AdminAppTemplateDeleteRequest() # AdminAppTemplateDeleteRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 删除应用模板
    api_response = api_instance.admin_app_template_delete(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_app_template_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AdminAppTemplateDeleteRequest**](AdminAppTemplateDeleteRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**AdminAppTemplateDeleteResponse**](AdminAppTemplateDeleteResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_app_template_get**
> AdminAppTemplateGetResponse admin_app_template_get(body, oid=oid, company_id=company_id, app_id=app_id)

根据id获取应用模板

根据id获取应用模板

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AdminApi(swagger_client.ApiClient(configuration))
body = swagger_client.AdminAppTemplateGetRequest() # AdminAppTemplateGetRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 根据id获取应用模板
    api_response = api_instance.admin_app_template_get(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_app_template_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AdminAppTemplateGetRequest**](AdminAppTemplateGetRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**AdminAppTemplateGetResponse**](AdminAppTemplateGetResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_app_template_import**
> AdminAppTemplateImportResponse admin_app_template_import(body, oid=oid, company_id=company_id, app_id=app_id)

导入应用模板

导入应用模板

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AdminApi(swagger_client.ApiClient(configuration))
body = swagger_client.AdminAppTemplateImportRequest() # AdminAppTemplateImportRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 导入应用模板
    api_response = api_instance.admin_app_template_import(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_app_template_import: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AdminAppTemplateImportRequest**](AdminAppTemplateImportRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**AdminAppTemplateImportResponse**](AdminAppTemplateImportResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_app_template_list**
> AdminAppTemplateListResponse admin_app_template_list(body, oid=oid, company_id=company_id, app_id=app_id)

获取应用模板列表

获取应用模板列表

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AdminApi(swagger_client.ApiClient(configuration))
body = swagger_client.AdminAppTemplateListRequest() # AdminAppTemplateListRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 获取应用模板列表
    api_response = api_instance.admin_app_template_list(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_app_template_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AdminAppTemplateListRequest**](AdminAppTemplateListRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**AdminAppTemplateListResponse**](AdminAppTemplateListResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_app_template_update**
> AdminAppTemplateUpdateResponse admin_app_template_update(body, oid=oid, company_id=company_id, app_id=app_id)

更新应用模板

更新应用模板

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AdminApi(swagger_client.ApiClient(configuration))
body = swagger_client.AdminAppTemplateUpdateRequest() # AdminAppTemplateUpdateRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 更新应用模板
    api_response = api_instance.admin_app_template_update(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_app_template_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AdminAppTemplateUpdateRequest**](AdminAppTemplateUpdateRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**AdminAppTemplateUpdateResponse**](AdminAppTemplateUpdateResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_company_delete**
> AdminCompanyDeleteResponse admin_company_delete(body, oid=oid, company_id=company_id, app_id=app_id)

删除团队

删除团队

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AdminApi(swagger_client.ApiClient(configuration))
body = swagger_client.AccountCompanyDeleteRequest() # AccountCompanyDeleteRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 删除团队
    api_response = api_instance.admin_company_delete(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_company_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountCompanyDeleteRequest**](AccountCompanyDeleteRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**AdminCompanyDeleteResponse**](AdminCompanyDeleteResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_company_get**
> AdminCompanyGetResponse admin_company_get(body, oid=oid, company_id=company_id, app_id=app_id)

根据ID获取团队

根据ID获取团队

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AdminApi(swagger_client.ApiClient(configuration))
body = swagger_client.AccountCompanyGetRequest() # AccountCompanyGetRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 根据ID获取团队
    api_response = api_instance.admin_company_get(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_company_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountCompanyGetRequest**](AccountCompanyGetRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**AdminCompanyGetResponse**](AdminCompanyGetResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_company_list**
> AdminCompanyListResponse admin_company_list(body, oid=oid, company_id=company_id, app_id=app_id)

获取团队列表

获取团队列表

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AdminApi(swagger_client.ApiClient(configuration))
body = swagger_client.AccountCompanyListRequest() # AccountCompanyListRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 获取团队列表
    api_response = api_instance.admin_company_list(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_company_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountCompanyListRequest**](AccountCompanyListRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**AdminCompanyListResponse**](AdminCompanyListResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_company_pro**
> AdminCompanyProResponse admin_company_pro(body, oid=oid, company_id=company_id, app_id=app_id)

设置团队版本为专业版

设置团队版本为专业版

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AdminApi(swagger_client.ApiClient(configuration))
body = swagger_client.AccountCompanySetProRequest() # AccountCompanySetProRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 设置团队版本为专业版
    api_response = api_instance.admin_company_pro(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_company_pro: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountCompanySetProRequest**](AccountCompanySetProRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**AdminCompanyProResponse**](AdminCompanyProResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_config_list**
> AdminConfigListResponse admin_config_list(body, oid=oid, company_id=company_id, app_id=app_id)

查询配置列表

查询配置列表

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AdminApi(swagger_client.ApiClient(configuration))
body = swagger_client.AdminConfigListRequest() # AdminConfigListRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 查询配置列表
    api_response = api_instance.admin_config_list(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_config_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AdminConfigListRequest**](AdminConfigListRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**AdminConfigListResponse**](AdminConfigListResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_config_update**
> APIResponse admin_config_update(body, oid=oid, company_id=company_id, app_id=app_id)

更新配置信息

更新配置信息

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AdminApi(swagger_client.ApiClient(configuration))
body = swagger_client.AdminConfigUpdateRequest() # AdminConfigUpdateRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 更新配置信息
    api_response = api_instance.admin_config_update(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_config_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AdminConfigUpdateRequest**](AdminConfigUpdateRequest.md)|  | 
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

# **admin_import_license**
> AdminImportLicenseResponse admin_import_license(body, oid=oid, company_id=company_id, app_id=app_id)

导入许可证

导入许可证

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AdminApi(swagger_client.ApiClient(configuration))
body = swagger_client.AdminImportLicenseRequest() # AdminImportLicenseRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 导入许可证
    api_response = api_instance.admin_import_license(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_import_license: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AdminImportLicenseRequest**](AdminImportLicenseRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**AdminImportLicenseResponse**](AdminImportLicenseResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_import_sub_license**
> AdminImportSubLicenseResponse admin_import_sub_license(body, oid=oid, company_id=company_id, app_id=app_id)

导入子许可证

导入子许可证

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AdminApi(swagger_client.ApiClient(configuration))
body = swagger_client.AdminImportSubLicenseRequest() # AdminImportSubLicenseRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 导入子许可证
    api_response = api_instance.admin_import_sub_license(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_import_sub_license: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AdminImportSubLicenseRequest**](AdminImportSubLicenseRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**AdminImportSubLicenseResponse**](AdminImportSubLicenseResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_refresh_token**
> AdminRefreshTokenResponse admin_refresh_token(body, oid=oid, company_id=company_id, app_id=app_id)

刷新adminToken

刷新adminToken

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AdminApi(swagger_client.ApiClient(configuration))
body = swagger_client.AdminTokenRefreshRequest() # AdminTokenRefreshRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 刷新adminToken
    api_response = api_instance.admin_refresh_token(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_refresh_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AdminTokenRefreshRequest**](AdminTokenRefreshRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**AdminRefreshTokenResponse**](AdminRefreshTokenResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_token**
> AdminTokenResponse admin_token(body)

获取adminToken

获取adminToken

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdminApi()
body = swagger_client.AdminTokenRequest() # AdminTokenRequest | 

try:
    # 获取adminToken
    api_response = api_instance.admin_token(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AdminTokenRequest**](AdminTokenRequest.md)|  | 

### Return type

[**AdminTokenResponse**](AdminTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_version**
> AdminVersionResponse admin_version(body, oid=oid, company_id=company_id, app_id=app_id)

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
api_instance = swagger_client.AdminApi(swagger_client.ApiClient(configuration))
body = NULL # object | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 系统版本号
    api_response = api_instance.admin_version(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**AdminVersionResponse**](AdminVersionResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

