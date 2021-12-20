# NormalFeature

Einzelner Datenpunkt, der nur über den normalen Umfang an Werten verfügt

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | [**NormalFeatureProperties**](NormalFeatureProperties.md) |  | [optional] 
**type** | **str** | Feature-Feld, immer &#x60;Feature&#x60; | [optional]  if omitted the server will use the default value of "Feature"
**id** | **str** | ID des Features, setzt sich zusammen aus dem Name des Layers und einer eindeutigen ID | [optional] 
**geometry** | [**GeometryPoint**](GeometryPoint.md) |  | [optional] 
**geometry_name** | **str** | Geometriename, immer &#x60;geom&#x60; | [optional]  if omitted the server will use the default value of "geom"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


