# swagger_client.CompanyApi

All URIs are relative to *http://uat.informat.cn/webapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**company_department_create**](CompanyApi.md#company_department_create) | **POST** /v2/company_department/create | 创建部门
[**company_department_delete**](CompanyApi.md#company_department_delete) | **POST** /v2/company_department/delete | 删除部门
[**company_department_list**](CompanyApi.md#company_department_list) | **POST** /v2/company_department/list | 获取部门列表
[**company_department_update**](CompanyApi.md#company_department_update) | **POST** /v2/company_department/update | 更新部门
[**company_get**](CompanyApi.md#company_get) | **POST** /v2/company/get | 获取当前团队信息
[**company_member_batch_delete**](CompanyApi.md#company_member_batch_delete) | **POST** /v2/company_member/batch_delete | 从团队批量移除成员
[**company_member_get**](CompanyApi.md#company_member_get) | **POST** /v2/company_member/get | 根据token查询用户信息
[**company_member_list**](CompanyApi.md#company_member_list) | **POST** /v2/company_member/list | 获取成员列表
[**company_member_role_create**](CompanyApi.md#company_member_role_create) | **POST** /v2/company_member_role/create | 创建角色
[**company_member_role_delete**](CompanyApi.md#company_member_role_delete) | **POST** /v2/company_member_role/delete | 删除角色
[**company_member_role_list**](CompanyApi.md#company_member_role_list) | **POST** /v2/company_member_role/list | 获取角色列表
[**company_member_role_update**](CompanyApi.md#company_member_role_update) | **POST** /v2/company_member_role/update | 更新角色
[**company_member_update**](CompanyApi.md#company_member_update) | **POST** /v2/company_member/update | 更新成员信息
[**company_refresh_token**](CompanyApi.md#company_refresh_token) | **POST** /v2/company/refresh_token | 刷新团队token
[**company_token**](CompanyApi.md#company_token) | **POST** /v2/company/token | 获取团队token
[**company_update_logo**](CompanyApi.md#company_update_logo) | **POST** /v2/company/update_logo | 修改团队logo

# **company_department_create**
> CompanyDepartmentCreateResponse company_department_create(body, oid=oid, company_id=company_id, app_id=app_id)

创建部门

创建部门

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CompanyApi(swagger_client.ApiClient(configuration))
body = swagger_client.CompanyDepartmentCreateRequest() # CompanyDepartmentCreateRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 创建部门
    api_response = api_instance.company_department_create(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->company_department_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CompanyDepartmentCreateRequest**](CompanyDepartmentCreateRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**CompanyDepartmentCreateResponse**](CompanyDepartmentCreateResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **company_department_delete**
> CompanyDepartmentDeleteResponse company_department_delete(body, oid=oid, company_id=company_id, app_id=app_id)

删除部门

删除部门

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CompanyApi(swagger_client.ApiClient(configuration))
body = swagger_client.CompanyDepartmentDeleteRequest() # CompanyDepartmentDeleteRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 删除部门
    api_response = api_instance.company_department_delete(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->company_department_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CompanyDepartmentDeleteRequest**](CompanyDepartmentDeleteRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**CompanyDepartmentDeleteResponse**](CompanyDepartmentDeleteResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **company_department_list**
> CompanyDepartmentListResponse company_department_list(body, oid=oid, company_id=company_id, app_id=app_id)

获取部门列表

获取部门列表

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CompanyApi(swagger_client.ApiClient(configuration))
body = swagger_client.CompanyDepartmentListRequest() # CompanyDepartmentListRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 获取部门列表
    api_response = api_instance.company_department_list(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->company_department_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CompanyDepartmentListRequest**](CompanyDepartmentListRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**CompanyDepartmentListResponse**](CompanyDepartmentListResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **company_department_update**
> CompanyDepartmentUpdateResponse company_department_update(body, oid=oid, company_id=company_id, app_id=app_id)

更新部门

更新部门

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CompanyApi(swagger_client.ApiClient(configuration))
body = swagger_client.CompanyDepartmentUpdateRequest() # CompanyDepartmentUpdateRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 更新部门
    api_response = api_instance.company_department_update(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->company_department_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CompanyDepartmentUpdateRequest**](CompanyDepartmentUpdateRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**CompanyDepartmentUpdateResponse**](CompanyDepartmentUpdateResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **company_get**
> CompanyGetResponse company_get(body, oid=oid, company_id=company_id, app_id=app_id)

获取当前团队信息

获取当前团队信息

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CompanyApi(swagger_client.ApiClient(configuration))
body = swagger_client.CompanyGetRequest() # CompanyGetRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 获取当前团队信息
    api_response = api_instance.company_get(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->company_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CompanyGetRequest**](CompanyGetRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**CompanyGetResponse**](CompanyGetResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **company_member_batch_delete**
> APIResponse company_member_batch_delete(body, oid=oid, company_id=company_id, app_id=app_id)

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
api_instance = swagger_client.CompanyApi(swagger_client.ApiClient(configuration))
body = swagger_client.CompanyMemberBatchDeleteRequest() # CompanyMemberBatchDeleteRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 从团队批量移除成员
    api_response = api_instance.company_member_batch_delete(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->company_member_batch_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CompanyMemberBatchDeleteRequest**](CompanyMemberBatchDeleteRequest.md)|  | 
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

# **company_member_get**
> CompanyMemberGetResponse company_member_get(body, oid=oid, company_id=company_id, app_id=app_id)

根据token查询用户信息

根据token查询用户信息

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CompanyApi(swagger_client.ApiClient(configuration))
body = swagger_client.CompanyMemberGetRequest() # CompanyMemberGetRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 根据token查询用户信息
    api_response = api_instance.company_member_get(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->company_member_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CompanyMemberGetRequest**](CompanyMemberGetRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**CompanyMemberGetResponse**](CompanyMemberGetResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **company_member_list**
> CompanyMemberListResponse company_member_list(body, oid=oid, company_id=company_id, app_id=app_id)

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
api_instance = swagger_client.CompanyApi(swagger_client.ApiClient(configuration))
body = swagger_client.CompanyMemberListRequest() # CompanyMemberListRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 获取成员列表
    api_response = api_instance.company_member_list(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->company_member_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CompanyMemberListRequest**](CompanyMemberListRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**CompanyMemberListResponse**](CompanyMemberListResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **company_member_role_create**
> CompanyMemberRoleCreateResponse company_member_role_create(body, oid=oid, company_id=company_id, app_id=app_id)

创建角色

创建角色

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CompanyApi(swagger_client.ApiClient(configuration))
body = swagger_client.CompanyMemberRoleCreateRequest() # CompanyMemberRoleCreateRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 创建角色
    api_response = api_instance.company_member_role_create(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->company_member_role_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CompanyMemberRoleCreateRequest**](CompanyMemberRoleCreateRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**CompanyMemberRoleCreateResponse**](CompanyMemberRoleCreateResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **company_member_role_delete**
> CompanyMemberRoleDeleteResponse company_member_role_delete(body, oid=oid, company_id=company_id, app_id=app_id)

删除角色

删除角色

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CompanyApi(swagger_client.ApiClient(configuration))
body = swagger_client.CompanyMemberRoleDeleteRequest() # CompanyMemberRoleDeleteRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 删除角色
    api_response = api_instance.company_member_role_delete(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->company_member_role_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CompanyMemberRoleDeleteRequest**](CompanyMemberRoleDeleteRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**CompanyMemberRoleDeleteResponse**](CompanyMemberRoleDeleteResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **company_member_role_list**
> CompanyMemberRoleListResponse company_member_role_list(body, oid=oid, company_id=company_id, app_id=app_id)

获取角色列表

获取角色列表

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CompanyApi(swagger_client.ApiClient(configuration))
body = swagger_client.CompanyMemberRoleListRequest() # CompanyMemberRoleListRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 获取角色列表
    api_response = api_instance.company_member_role_list(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->company_member_role_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CompanyMemberRoleListRequest**](CompanyMemberRoleListRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**CompanyMemberRoleListResponse**](CompanyMemberRoleListResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **company_member_role_update**
> CompanyMemberRoleUpdateResponse company_member_role_update(body, oid=oid, company_id=company_id, app_id=app_id)

更新角色

更新角色

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CompanyApi(swagger_client.ApiClient(configuration))
body = swagger_client.CompanyMemberRoleUpdateRequest() # CompanyMemberRoleUpdateRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 更新角色
    api_response = api_instance.company_member_role_update(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->company_member_role_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CompanyMemberRoleUpdateRequest**](CompanyMemberRoleUpdateRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**CompanyMemberRoleUpdateResponse**](CompanyMemberRoleUpdateResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **company_member_update**
> CompanyMemberUpdateResponse company_member_update(body, oid=oid, company_id=company_id, app_id=app_id)

更新成员信息

更新成员信息

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CompanyApi(swagger_client.ApiClient(configuration))
body = swagger_client.CompanyMemberUpdateRequest() # CompanyMemberUpdateRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 更新成员信息
    api_response = api_instance.company_member_update(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->company_member_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CompanyMemberUpdateRequest**](CompanyMemberUpdateRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**CompanyMemberUpdateResponse**](CompanyMemberUpdateResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **company_refresh_token**
> CompanyRefreshTokenResponse company_refresh_token(body, oid=oid, company_id=company_id, app_id=app_id)

刷新团队token

刷新团队token

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CompanyApi(swagger_client.ApiClient(configuration))
body = swagger_client.CompanyRefreshTokenRequest() # CompanyRefreshTokenRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 刷新团队token
    api_response = api_instance.company_refresh_token(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->company_refresh_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CompanyRefreshTokenRequest**](CompanyRefreshTokenRequest.md)|  | 
 **oid** | **str**| OID | [optional] 
 **company_id** | **str**| 团队ID | [optional] 
 **app_id** | **str**| 应用ID | [optional] 

### Return type

[**CompanyRefreshTokenResponse**](CompanyRefreshTokenResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **company_token**
> CompanyTokenResponse company_token(body)

获取团队token

获取团队token

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CompanyApi()
body = swagger_client.CompanyTokenRequest() # CompanyTokenRequest | 

try:
    # 获取团队token
    api_response = api_instance.company_token(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->company_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CompanyTokenRequest**](CompanyTokenRequest.md)|  | 

### Return type

[**CompanyTokenResponse**](CompanyTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **company_update_logo**
> APIResponse company_update_logo(body, oid=oid, company_id=company_id, app_id=app_id)

修改团队logo

修改团队logo

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CompanyApi(swagger_client.ApiClient(configuration))
body = swagger_client.CompanyUpdateLogoRequest() # CompanyUpdateLogoRequest | 
oid = 'oid_example' # str | OID (optional)
company_id = 'company_id_example' # str | 团队ID (optional)
app_id = 'app_id_example' # str | 应用ID (optional)

try:
    # 修改团队logo
    api_response = api_instance.company_update_logo(body, oid=oid, company_id=company_id, app_id=app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->company_update_logo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CompanyUpdateLogoRequest**](CompanyUpdateLogoRequest.md)|  | 
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

