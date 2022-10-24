# TableWorkflowInstanceNodeVO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**table_id** | **str** | 数据表 | [optional] 
**workflow_id** | **str** | 流程定义 | [optional] 
**instance_id** | **str** | 流程实例 | [optional] 
**before_node_id** | **str** | 上一个节点ID | [optional] 
**before_node_name** | **str** | 上一个节点名称 | [optional] 
**before_node_color** | **str** | 上一个节点颜色 | [optional] 
**node_id** | **str** | 节点ID | [optional] 
**node_name** | **str** | 节点名称 | [optional] 
**node_color** | **str** | 节点颜色 | [optional] 
**node_type** | **str** | 节点类型 | [optional] 
**enter_time** | **float** | 进入时间 | [optional] 
**leave_time** | **float** | 离开时间 | [optional] 
**opt_account_id** | **str** | 操作人 | [optional] 
**status** | **str** | 审批结果 | [optional] 
**name** | **str** | 审批意见 | [optional] 
**owner_account_list** | [**list[TableAccountSimple]**](TableAccountSimple.md) | 责任人 | [optional] 
**cc_account_list** | [**list[TableAccountSimple]**](TableAccountSimple.md) | 抄送人 | [optional] 
**agree_count** | **int** | 同意数量 | [optional] 
**wait_count** | **int** | 等待数量 | [optional] 
**form_data** | **dict(str, object)** | 表单数据 | [optional] 
**transfer** | [**list[TableWorkflowInstanceNodeTransfer]**](TableWorkflowInstanceNodeTransfer.md) | 转交信息 | [optional] 
**opt_account_id_avatar** | **str** | 操作人图标 | [optional] 
**opt_account_id_name** | **str** | 操作人名称 | [optional] 
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

