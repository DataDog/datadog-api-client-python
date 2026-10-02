# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.archive_search_response import ArchiveSearchResponse
from datadog_api_client.v2.model.archive_search_create_request import ArchiveSearchCreateRequest


class LogsArchiveSearchesApi:
    """
    Archive Search queries logs directly from long-term storage archives without prior
    rehydration and charges only for the data scanned.

    A search runs in one of two modes. By default it scans the archive and retains up to
    100,000 matching logs for 24 hours on a dedicated results page. Include a ``rehydration``
    object to run a Search & Rehydration instead, which retains the matches for a custom
    retention period and makes them available in Log Explorer, Dashboards, and Notebooks.

    A search requires the ``logs_write_historical_view`` or ``logs_write_archive_search``
    permission. Rehydration requires ``logs_write_historical_view``.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_archive_search_endpoint = _Endpoint(
            settings={
                "response_type": (ArchiveSearchResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/logs/archive_searches",
                "operation_id": "create_archive_search",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ArchiveSearchCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._get_archive_search_endpoint = _Endpoint(
            settings={
                "response_type": (ArchiveSearchResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/logs/archive_searches/{archive_search_id}",
                "operation_id": "get_archive_search",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "archive_search_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "archive_search_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

    def create_archive_search(
        self,
        body: ArchiveSearchCreateRequest,
    ) -> ArchiveSearchResponse:
        """Create an Archive Search.

        Start a search over the logs stored in an archive.

        Without a ``rehydration`` object, the search only scans the archive and reports how much data
        matched. With one, the matched logs are also indexed into a retained historical view, which
        requires the ``logs_write_historical_view`` permission.

        :type body: ArchiveSearchCreateRequest
        :rtype: ArchiveSearchResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_archive_search_endpoint.call_with_http_info(**kwargs)

    def get_archive_search(
        self,
        archive_search_id: str,
    ) -> ArchiveSearchResponse:
        """Get an Archive Search.

        Get a single Archive Search, including its status and the amount of archive data scanned when the search finishes.

        :param archive_search_id: Unique identifier of the Archive Search.
        :type archive_search_id: str
        :rtype: ArchiveSearchResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["archive_search_id"] = archive_search_id

        return self._get_archive_search_endpoint.call_with_http_info(**kwargs)
