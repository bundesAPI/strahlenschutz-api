# BaseSchema

Abstraktes Standardschema der API. Diese Ebene entspricht einer `FeatureCollection` in GeoJSON.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | FeatureCollection-Feld, immer &#x60;FeatureCollection&#x60; | [optional]  if omitted the server will use the default value of "FeatureCollection"
**total_features** | **float** | Anzahl der insgesamt gefundenen Datensätze | [optional] 
**number_returned** | **float** | Anzahl zurückgegebener Datensätze, also die Länge von &#x60;features&#x60;. Kleinergleich &#x60;totalFeatures&#x60;. | [optional] 
**time_stamp** | **datetime** | Zeitstempel der Antwort | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


