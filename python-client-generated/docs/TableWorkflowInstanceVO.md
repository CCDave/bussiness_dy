# TableWorkflowInstanceVO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**table_id** | **str** | 数据表ID | [optional] 
**record_id** | **str** | 记录ID | [optional] 
**workflow_id** | **str** | 流程定义ID | [optional] 
**title** | **str** | 标题 | [optional] 
**is_finished** | **bool** | 是否结束 | [optional] 
**finish_type** | **str** | 结束类型  | [optional] 
**finish_text** | **str** | 结束文本 | [optional] 
**finish_time** | **float** | 结束时间 | [optional] 
**form_data** | **dict(str, object)** | 表单数据 | [optional] 
**remark** | **str** | 描述 | [optional] 
**owner_account_list** | [**list[TableAccountSimple]**](TableAccountSimple.md) | 当前责任人列表 | [optional] 
**cc_account_list** | [**list[TableAccountSimple]**](TableAccountSimple.md) | 抄送人列表 | [optional] 
**chart_id** | **str** | 流程图ID | [optional] 
**chart_version** | **int** | 流程图版本 | [optional] 
**owner_config** | [**TableWorkflowInstanceOwnerConfig**](TableWorkflowInstanceOwnerConfig.md) |  | [optional] 
**status** | **int** | 状态 | [optional] 
**module_name** | **str** | 模块名称 | [optional] 
**module_icon** | **str** | 模块图标 | [optional] 
**id** | **str** | ID | [optional] 
**company_id** | **str** | 团队ID | [optional] 
**application_id** | **str** | 应用ID | [optional] 
**create_time** | **float** | 创建时间 | [optional] 
**update_time** | **float** | 最后更新时间 | [optional] 
**create_account_id** | **str** | 创建人ID | [optional] 
**create_account_name** | **str** | 创建人名称 | [optional] 
**update_account_id** | **str** | 最后更新人ID | [optional] 
**update_account_name** | **str** | 最后更新人名称 | [optional] 
**app_name** | **str** | 应用名称 | [optional] 
**app_color** | **str** | 应用颜色 | [optional] 
**app_icon** | **str** | 应用图标 | [optional] 
**is_delete** | **bool** | 是否已删除 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

