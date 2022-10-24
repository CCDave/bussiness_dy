# TableRecordListRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_by_list** | [**list[OrderBy]**](OrderBy.md) | 排序方式 | [optional] 
**page_size** | **int** | 每页数量 | [optional] 
**page_index** | **int** | 页码 | [optional] 
**table_id** | **str** | 数据表ID | 
**condition_list** | [**list[Condition]**](Condition.md) | 过滤条件列表 | [optional] 
**id** | **str** | 指定记录ID | [optional] 
**group_by_field_list** | **list[object]** | 分组列表 | [optional] 
**aggregation_query_list** | [**list[AggregationQuery]**](AggregationQuery.md) | 聚合查询列表 | [optional] 
**use_field_name** | **bool** | 使用字段名称作为返回数据的键 | [optional] 
**show_parent** | **bool** | 查询父节点数据 | [optional] 
**show_children** | **bool** | 查询子节点数据 | [optional] 
**children_filter_field_list** | **list[object]** | 查询子节点数据的字段列表 | [optional] 
**aggregation_split_multi_value** | **bool** | 是否分离多选值 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

