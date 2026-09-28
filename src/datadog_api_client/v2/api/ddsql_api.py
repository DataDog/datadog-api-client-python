# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.ddsql_tabular_query_response import DdsqlTabularQueryResponse
from datadog_api_client.v2.model.ddsql_tabular_query_request import DdsqlTabularQueryRequest
from datadog_api_client.v2.model.ddsql_tabular_query_fetch_request import DdsqlTabularQueryFetchRequest


class DDSQLApi:
    """
    Execute DDSQL queries against the Datadog data catalog and poll for their results.
    Queries are dispatched asynchronously: the initial request may return a ``running`` state with
    a ``query_id`` , and clients poll the fetch endpoint until the response transitions to
    ``completed`` with a column-major result set.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._execute_ddsql_tabular_query_endpoint = _Endpoint(
            settings={
                "response_type": (DdsqlTabularQueryResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/ddsql/query/tabular",
                "operation_id": "execute_ddsql_tabular_query",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (DdsqlTabularQueryRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._fetch_ddsql_tabular_query_endpoint = _Endpoint(
            settings={
                "response_type": (DdsqlTabularQueryResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/ddsql/query/tabular/fetch",
                "operation_id": "fetch_ddsql_tabular_query",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (DdsqlTabularQueryFetchRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def execute_ddsql_tabular_query(
        self,
        body: DdsqlTabularQueryRequest,
    ) -> DdsqlTabularQueryResponse:
        """Execute a tabular DDSQL query.

        Submit a DDSQL statement and return either a ``running`` state with an opaque ``query_id``
        for the client to poll, or a ``completed`` state with the column-major result set inlined
        when the query finishes quickly enough to be served synchronously.

        For a scoped application key, include ``timeseries_query`` in its scopes.
        A query that does not read a data source, such as ``SELECT 1`` , requires no additional
        data-source permissions. Queries that read data sources also require the user or
        service account that owns the application key to have the corresponding data access
        permissions through their roles. The ``timeseries_query`` permission does not grant
        access to the underlying data sources.

        :type body: DdsqlTabularQueryRequest
        :rtype: DdsqlTabularQueryResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._execute_ddsql_tabular_query_endpoint.call_with_http_info(**kwargs)

    def fetch_ddsql_tabular_query(
        self,
        body: DdsqlTabularQueryFetchRequest,
    ) -> DdsqlTabularQueryResponse:
        """Fetch the result of a DDSQL query.

        Poll a previously submitted DDSQL query for results. Pass the opaque ``query_id`` returned
        by a prior ``ExecuteDdsqlTabularQuery`` (or by a prior ``FetchDdsqlTabularQuery`` that
        returned ``state: running`` ) and the server returns either a ``running`` state to poll again
        or a ``completed`` state with the column-major result set inlined.

        For a scoped application key, include ``timeseries_query`` in its scopes.
        Fetch results as the same user and organization that submitted the query.
        The user or service account that owns the application key must have the data access
        permissions required by the queried data sources through their roles.

        :type body: DdsqlTabularQueryFetchRequest
        :rtype: DdsqlTabularQueryResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._fetch_ddsql_tabular_query_endpoint.call_with_http_info(**kwargs)
