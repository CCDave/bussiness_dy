# Node

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID | [optional] 
**name** | **str** | 名称 | [optional] 
**color** | **str** | 颜色 | [optional] 
**forward_rule** | **str** | 流转规则 | [optional] 
**allow_cancel** | **bool** | 是否允许发起撤销 | [optional] 
**allow_transfer** | **bool** | 是否允许转交他人 | [optional] 
**allow_rollback** | **bool** | 是否允许回退 | [optional] 
**owner** | **list[object]** | 审批人列表 | [optional] 
**cc** | **list[object]** | 抄送人列表 | [optional] 
**field_setting_list** | [**list[FieldSetting]**](FieldSetting.md) | 字段配置 | [optional] 
**submit_text** | **str** | 默认审批意见 | [optional] 
**submit_button_text** | **str** | 同意按钮的文字 | [optional] 
**invoke_api** | **str** | 流转后执行的API | [optional] 
**invoke_automatic** | **str** | 流转后执行的自动化 | [optional] 
**invoke_api_on_enter** | **str** | 进入节点时执行的API | [optional] 
**invoke_automatic_on_enter** | **str** | 进入节点时执行的自动化 | [optional] 
**validate_list** | [**list[WorkflowValidate]**](WorkflowValidate.md) | 校验规则列表 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

