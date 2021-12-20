# ExtendedFeatureProperties

Erweiterte Werte eines einzelnen Datenpunktes

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**site_status** | **float** | Status der Messstelle:   * &#x60;1&#x60; - In Betrieb   * &#x60;2&#x60; - Defekt   * &#x60;3&#x60; - Testbetrieb  | [optional] 
**site_status_text** | **str** | Status der Messstelle als Text | [optional] 
**kid** | **float** | ID des Messnetzknotens, dem die Messstelle zugeordnet ist:   * &#x60;1&#x60; - Freiburg   * &#x60;2&#x60; - Berlin   * &#x60;3&#x60; - München   * &#x60;4&#x60; - Bonn   * &#x60;5&#x60; - Salzgitter   * &#x60;6&#x60; - Rendsburg  | [optional] 
**height_above_sea** | **float** | Höhe der Messstelle über NN (Normal Null, Meereshöhe) | [optional] 
**value_cosmic** | **float** | Kosmischer Anteil in &#x60;unit&#x60; | [optional] 
**value_terrestrial** | **float** | Terrestrischer Anteil in &#x60;unit&#x60; | [optional] 
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


