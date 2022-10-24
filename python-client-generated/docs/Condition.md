# Condition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_id** | **str** | 字段id | [optional] 
**opt** | **str** | 操作符。 | [optional] 
**value** | **object** | 值。opt为notbetween，between，not in，in时，value为数组。opt为isNull，isNotNull时value不需要传值。Opt为eq，ne，gt，ge，lt，le时为数值类型。Opt为eq，ne时value可以是数值和字符串类型。其余情况下value为字符串类型 | [optional] 
**func** | **str** | 函数 | [optional] 
**var** | **bool** | 是否表达式 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

