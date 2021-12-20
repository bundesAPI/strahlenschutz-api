# NormalFeatureProperties

Grundlegende Werte eines einzelnen Datenpunktes

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Internationale ID der Messstelle | [optional] 
**kenn** | **str** | Interne Messstellenkennung | [optional] 
**plz** | **str** | PLZ der Messstelle | [optional] 
**name** | **str** | Name/Ortsname der Messstelle | [optional] 
**start_measure** | **datetime** | Startzeitpunkt der Messperiode für den gegebenen Messwert als ISO-Datetime | [optional] 
**end_measure** | **datetime** | Endzeitpunkt der Messperiode für den gegebenen Messwert als ISO-Datetime | [optional] 
**value** | **float** | Der Messwert in &#x60;unit&#x60; (setzt sich aus &#x60;value_cosmic&#x60; und &#x60;value_terrestrial&#x60; zusammen) | [optional] 
**unit** | **str** | Einheit der Messwerte | [optional] 
**validated** | **float** | Prüfstatus des Messwertes:   * &#x60;1&#x60; - geprüft   * &#x60;2&#x60; - ungeprüft  | [optional] 
**nuclide** | **str** | Bezeichnung der Messgröße | [optional] 
**duration** | **str** | Dauer der Messperiode   * &#x60;1h&#x60; - eine Stunde   * &#x60;1d&#x60; - ein Tag  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


