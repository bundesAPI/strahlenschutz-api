# strahlenschutz.DefaultApi

All URIs are relative to *https://www.imis.bfs.de/ogc/opendata/ows*

Method | HTTP request | Description
------------- | ------------- | -------------
[**root_get**](DefaultApi.md#root_get) | **GET** / | Hauptendpunkt


# **root_get**
> bool, date, datetime, dict, float, int, list, str, none_type root_get()

Hauptendpunkt

### Example


```python
import time
from deutschland import strahlenschutz
from deutschland.strahlenschutz.api import default_api
from deutschland.strahlenschutz.model.extended_schema import ExtendedSchema
from deutschland.strahlenschutz.model.normal_schema import NormalSchema
from pprint import pprint
# Defining the host is optional and defaults to https://www.imis.bfs.de/ogc/opendata/ows
# See configuration.py for a list of all supported configuration parameters.
configuration = strahlenschutz.Configuration(
    host = "https://www.imis.bfs.de/ogc/opendata/ows"
)


# Enter a context with an instance of the API client
with strahlenschutz.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    type_name = "opendata:odlinfo_odl_1h_latest" # str | Name des Datenlayers, das benutzt werden soll.   * `odlinfo_odl_1h_latest` - Liste der Messstellen inklusive dem jeweils letzten 1-Stunden-Messwert   * `odlinfo_timeseries_odl_1h` - Zeitreihe mit 1-Stunden-Messdaten   * `odlinfo_timeseries_odl_24h` - Zeitreihe mit 24-Stunden-Messdaten  (optional)
    viewparams = "kenn:031020004" # str | Nur in Kombination mit historischen Daten (also nur Layer ohne `_latest`) relevant.  Genutzt zur Angabe einer spezifischen Messstelle mittels `kenn`-Wert.  (optional)
    sort_by = "end_measure+D" # str | Hier kann ein Feld von `properties` (also den zurückgegebenen Datenpunkten) angegeben werden, dann wird nach diesem aufsteigend sortiert. Wird an den Namen des Feldes noch `+D` angehängt, so wird absteigend sortiert.  (optional)
    max_features = 100 # float | Maximale Anzahl an Datenpunkten die zurückgegeben werden soll. (optional)
    start_index = 3.14 # float | Offset, von dem aus Datenpunkte zurückgegeben werden sollen. Kann in Kombination mit `maxFeatures` genutzt werden, um Pagination zu ermöglichen. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Hauptendpunkt
        api_response = api_instance.root_get()
        pprint(api_response)
    except strahlenschutz.ApiException as e:
        print("Exception when calling DefaultApi->root_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Hauptendpunkt
        api_response = api_instance.root_get(type_name=type_name, viewparams=viewparams, sort_by=sort_by, max_features=max_features, start_index=start_index)
        pprint(api_response)
    except strahlenschutz.ApiException as e:
        print("Exception when calling DefaultApi->root_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**| Name des Service der benutzt werden soll. Aktuell immer &#x60;WFS&#x60;. | defaults to "WFS"
 **request** | **str**| Name der OWS-Request. Aktuell immer &#x60;GetFeature&#x60;. | defaults to "GetFeature"
 **output_format** | **str**| Ausgabeformat. Aktuell immer &#x60;application/json&#x60;. | defaults to "application/json"
 **type_name** | **str**| Name des Datenlayers, das benutzt werden soll.   * &#x60;odlinfo_odl_1h_latest&#x60; - Liste der Messstellen inklusive dem jeweils letzten 1-Stunden-Messwert   * &#x60;odlinfo_timeseries_odl_1h&#x60; - Zeitreihe mit 1-Stunden-Messdaten   * &#x60;odlinfo_timeseries_odl_24h&#x60; - Zeitreihe mit 24-Stunden-Messdaten  | [optional]
 **viewparams** | **str**| Nur in Kombination mit historischen Daten (also nur Layer ohne &#x60;_latest&#x60;) relevant.  Genutzt zur Angabe einer spezifischen Messstelle mittels &#x60;kenn&#x60;-Wert.  | [optional]
 **sort_by** | **str**| Hier kann ein Feld von &#x60;properties&#x60; (also den zurückgegebenen Datenpunkten) angegeben werden, dann wird nach diesem aufsteigend sortiert. Wird an den Namen des Feldes noch &#x60;+D&#x60; angehängt, so wird absteigend sortiert.  | [optional]
 **max_features** | **float**| Maximale Anzahl an Datenpunkten die zurückgegeben werden soll. | [optional]
 **start_index** | **float**| Offset, von dem aus Datenpunkte zurückgegeben werden sollen. Kann in Kombination mit &#x60;maxFeatures&#x60; genutzt werden, um Pagination zu ermöglichen. | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Erfolgreicher Abruf - je nach Layer werden entweder grundlegende oder erweiterte Werte pro Datenpunkt zurückgegeben. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

