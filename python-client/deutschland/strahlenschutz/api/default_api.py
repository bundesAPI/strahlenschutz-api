"""
    ODL-Info API

    Daten zur radioaktiven Belastung in Deutschland. Weitere Informationen unter https://odlinfo.bfs.de/ODL/DE/service/datenschnittstelle/datenschnittstelle_node.html.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from deutschland.strahlenschutz.api_client import ApiClient
from deutschland.strahlenschutz.api_client import Endpoint as _Endpoint
from deutschland.strahlenschutz.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types,
)


class DefaultApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.root_get_endpoint = _Endpoint(
            settings={
                "response_type": (
                    bool,
                    date,
                    datetime,
                    dict,
                    float,
                    int,
                    list,
                    str,
                    none_type,
                ),
                "auth": [],
                "endpoint_path": "/",
                "operation_id": "root_get",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "service",
                    "request",
                    "output_format",
                    "type_name",
                    "viewparams",
                    "sort_by",
                    "max_features",
                    "start_index",
                ],
                "required": [
                    "service",
                    "request",
                    "output_format",
                ],
                "nullable": [],
                "enum": [
                    "service",
                    "request",
                    "output_format",
                    "type_name",
                ],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {
                    ("service",): {"WFS": "WFS"},
                    ("request",): {"GETFEATURE": "GetFeature"},
                    ("output_format",): {"APPLICATION/JSON": "application/json"},
                    ("type_name",): {
                        "ODL_1H_LATEST": "opendata:odlinfo_odl_1h_latest",
                        "TIMESERIES_ODL_1H": "opendata:odlinfo_timeseries_odl_1h",
                        "TIMESERIES_ODL_24H": "opendata:odlinfo_timeseries_odl_24h",
                    },
                },
                "openapi_types": {
                    "service": (str,),
                    "request": (str,),
                    "output_format": (str,),
                    "type_name": (str,),
                    "viewparams": (str,),
                    "sort_by": (str,),
                    "max_features": (float,),
                    "start_index": (float,),
                },
                "attribute_map": {
                    "service": "service",
                    "request": "request",
                    "output_format": "outputFormat",
                    "type_name": "typeName",
                    "viewparams": "viewparams",
                    "sort_by": "sortBy",
                    "max_features": "maxFeatures",
                    "start_index": "startIndex",
                },
                "location_map": {
                    "service": "query",
                    "request": "query",
                    "output_format": "query",
                    "type_name": "query",
                    "viewparams": "query",
                    "sort_by": "query",
                    "max_features": "query",
                    "start_index": "query",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

    def root_get(
        self,
        service="WFS",
        request="GetFeature",
        output_format="application/json",
        **kwargs
    ):
        """Hauptendpunkt  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.root_get(service="WFS", request="GetFeature", output_format="application/json", async_req=True)
        >>> result = thread.get()

        Args:
            service (str): Name des Service der benutzt werden soll. Aktuell immer `WFS`.. defaults to "WFS", must be one of ["WFS"]
            request (str): Name der OWS-Request. Aktuell immer `GetFeature`.. defaults to "GetFeature", must be one of ["GetFeature"]
            output_format (str): Ausgabeformat. Aktuell immer `application/json`.. defaults to "application/json", must be one of ["application/json"]

        Keyword Args:
            type_name (str): Name des Datenlayers, das benutzt werden soll.   * `odlinfo_odl_1h_latest` - Liste der Messstellen inklusive dem jeweils letzten 1-Stunden-Messwert   * `odlinfo_timeseries_odl_1h` - Zeitreihe mit 1-Stunden-Messdaten   * `odlinfo_timeseries_odl_24h` - Zeitreihe mit 24-Stunden-Messdaten . [optional]
            viewparams (str): Nur in Kombination mit historischen Daten (also nur Layer ohne `_latest`) relevant.  Genutzt zur Angabe einer spezifischen Messstelle mittels `kenn`-Wert. . [optional]
            sort_by (str): Hier kann ein Feld von `properties` (also den zurückgegebenen Datenpunkten) angegeben werden, dann wird nach diesem aufsteigend sortiert. Wird an den Namen des Feldes noch `+D` angehängt, so wird absteigend sortiert. . [optional]
            max_features (float): Maximale Anzahl an Datenpunkten die zurückgegeben werden soll.. [optional]
            start_index (float): Offset, von dem aus Datenpunkte zurückgegeben werden sollen. Kann in Kombination mit `maxFeatures` genutzt werden, um Pagination zu ermöglichen.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            bool, date, datetime, dict, float, int, list, str, none_type
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["service"] = service
        kwargs["request"] = request
        kwargs["output_format"] = output_format
        return self.root_get_endpoint.call_with_http_info(**kwargs)