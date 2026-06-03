# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

import collections
from typing import Any, Dict, List, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    datetime,
    set_attribute_from_path,
    get_attribute_from_path,
    UnsetType,
    unset,
)
from datadog_api_client.v2.model.rum_analytics_aggregate_response import RUMAnalyticsAggregateResponse
from datadog_api_client.v2.model.rum_aggregate_request import RUMAggregateRequest
from datadog_api_client.v2.model.rum_applications_response import RUMApplicationsResponse
from datadog_api_client.v2.model.rum_application_response import RUMApplicationResponse
from datadog_api_client.v2.model.rum_application_create_request import RUMApplicationCreateRequest
from datadog_api_client.v2.model.rum_application_update_request import RUMApplicationUpdateRequest
from datadog_api_client.v2.model.rum_events_response import RUMEventsResponse
from datadog_api_client.v2.model.rum_sort import RUMSort
from datadog_api_client.v2.model.rum_event import RUMEvent
from datadog_api_client.v2.model.rum_search_events_request import RUMSearchEventsRequest
from datadog_api_client.v2.model.sourcemaps_response import SourcemapsResponse
from datadog_api_client.v2.model.sourcemap_map_kind import SourcemapMapKind
from datadog_api_client.v2.model.sourcemap_file_response import SourcemapFileResponse
from datadog_api_client.v2.model.list_sourcemaps_response import ListSourcemapsResponse
from datadog_api_client.v2.model.service_repository_info_response import ServiceRepositoryInfoResponse
from datadog_api_client.v2.model.service_repository_info_request import ServiceRepositoryInfoRequest


class RUMApi:
    """
    Manage your Real User Monitoring (RUM) applications, and search or aggregate your RUM events over HTTP. See the `RUM & Session Replay page <https://docs.datadoghq.com/real_user_monitoring/>`_ for more information
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._aggregate_rum_events_endpoint = _Endpoint(
            settings={
                "response_type": (RUMAnalyticsAggregateResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/analytics/aggregate",
                "operation_id": "aggregate_rum_events",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (RUMAggregateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_rum_application_endpoint = _Endpoint(
            settings={
                "response_type": (RUMApplicationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/applications",
                "operation_id": "create_rum_application",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (RUMApplicationCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_rum_application_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/applications/{id}",
                "operation_id": "delete_rum_application",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_sourcemaps_endpoint = _Endpoint(
            settings={
                "response_type": (SourcemapsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/sourcemaps",
                "operation_id": "delete_sourcemaps",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "mapkind": {
                    "required": True,
                    "openapi_types": (SourcemapMapKind,),
                    "attribute": "mapkind",
                    "location": "query",
                },
                "dry_run": {
                    "required": True,
                    "openapi_types": (bool,),
                    "attribute": "dry_run",
                    "location": "query",
                },
                "filter_service": {
                    "openapi_types": ([str],),
                    "attribute": "filter[service]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_version": {
                    "openapi_types": ([str],),
                    "attribute": "filter[version]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_variant": {
                    "openapi_types": ([str],),
                    "attribute": "filter[variant]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_id": {
                    "openapi_types": ([str],),
                    "attribute": "filter[id]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_build_id": {
                    "openapi_types": ([str],),
                    "attribute": "filter[build_id]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_uuid": {
                    "openapi_types": ([str],),
                    "attribute": "filter[uuid]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_platform": {
                    "openapi_types": ([str],),
                    "attribute": "filter[platform]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_build_number": {
                    "openapi_types": ([str],),
                    "attribute": "filter[build_number]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_bundle_name": {
                    "openapi_types": ([str],),
                    "attribute": "filter[bundle_name]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_arch": {
                    "openapi_types": ([str],),
                    "attribute": "filter[arch]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_symbol_source": {
                    "openapi_types": ([str],),
                    "attribute": "filter[symbol_source]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_origin": {
                    "openapi_types": ([str],),
                    "attribute": "filter[origin]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_origin_version": {
                    "openapi_types": ([str],),
                    "attribute": "filter[origin_version]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_filename": {
                    "openapi_types": (str,),
                    "attribute": "filter[filename]",
                    "location": "query",
                },
                "filter_debug_id": {
                    "openapi_types": (str,),
                    "attribute": "filter[debug_id]",
                    "location": "query",
                },
                "filter_gnu_build_id": {
                    "openapi_types": (str,),
                    "attribute": "filter[gnu_build_id]",
                    "location": "query",
                },
                "filter_go_build_id": {
                    "openapi_types": (str,),
                    "attribute": "filter[go_build_id]",
                    "location": "query",
                },
                "filter_file_hash": {
                    "openapi_types": (str,),
                    "attribute": "filter[file_hash]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_rum_application_endpoint = _Endpoint(
            settings={
                "response_type": (RUMApplicationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/applications/{id}",
                "operation_id": "get_rum_application",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_rum_applications_endpoint = _Endpoint(
            settings={
                "response_type": (RUMApplicationsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/applications",
                "operation_id": "get_rum_applications",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_service_repository_info_endpoint = _Endpoint(
            settings={
                "response_type": (ServiceRepositoryInfoResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/sourcemaps/service_repository_info",
                "operation_id": "get_service_repository_info",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ServiceRepositoryInfoRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._get_sourcemaps_endpoint = _Endpoint(
            settings={
                "response_type": (SourcemapFileResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/sourcemaps",
                "operation_id": "get_sourcemaps",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "filename": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "filename",
                    "location": "query",
                },
                "service": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "service",
                    "location": "query",
                },
                "version": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "version",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_rum_events_endpoint = _Endpoint(
            settings={
                "response_type": (RUMEventsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/events",
                "operation_id": "list_rum_events",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "filter_query": {
                    "openapi_types": (str,),
                    "attribute": "filter[query]",
                    "location": "query",
                },
                "filter_from": {
                    "openapi_types": (datetime,),
                    "attribute": "filter[from]",
                    "location": "query",
                },
                "filter_to": {
                    "openapi_types": (datetime,),
                    "attribute": "filter[to]",
                    "location": "query",
                },
                "sort": {
                    "openapi_types": (RUMSort,),
                    "attribute": "sort",
                    "location": "query",
                },
                "page_cursor": {
                    "openapi_types": (str,),
                    "attribute": "page[cursor]",
                    "location": "query",
                },
                "page_limit": {
                    "validation": {
                        "inclusive_maximum": 1000,
                    },
                    "openapi_types": (int,),
                    "attribute": "page[limit]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_sourcemaps_endpoint = _Endpoint(
            settings={
                "response_type": (ListSourcemapsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/sourcemaps/list",
                "operation_id": "list_sourcemaps",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "mapkind": {
                    "openapi_types": (SourcemapMapKind,),
                    "attribute": "mapkind",
                    "location": "query",
                },
                "page_size": {
                    "openapi_types": (int,),
                    "attribute": "page[size]",
                    "location": "query",
                },
                "page_number": {
                    "openapi_types": (int,),
                    "attribute": "page[number]",
                    "location": "query",
                },
                "filter_service": {
                    "openapi_types": ([str],),
                    "attribute": "filter[service]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_version": {
                    "openapi_types": ([str],),
                    "attribute": "filter[version]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_variant": {
                    "openapi_types": ([str],),
                    "attribute": "filter[variant]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_id": {
                    "openapi_types": ([str],),
                    "attribute": "filter[id]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_build_id": {
                    "openapi_types": ([str],),
                    "attribute": "filter[build_id]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_uuid": {
                    "openapi_types": ([str],),
                    "attribute": "filter[uuid]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_platform": {
                    "openapi_types": ([str],),
                    "attribute": "filter[platform]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_build_number": {
                    "openapi_types": ([str],),
                    "attribute": "filter[build_number]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_bundle_name": {
                    "openapi_types": ([str],),
                    "attribute": "filter[bundle_name]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_arch": {
                    "openapi_types": ([str],),
                    "attribute": "filter[arch]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_symbol_source": {
                    "openapi_types": ([str],),
                    "attribute": "filter[symbol_source]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_origin": {
                    "openapi_types": ([str],),
                    "attribute": "filter[origin]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_origin_version": {
                    "openapi_types": ([str],),
                    "attribute": "filter[origin_version]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_filename": {
                    "openapi_types": (str,),
                    "attribute": "filter[filename]",
                    "location": "query",
                },
                "filter_debug_id": {
                    "openapi_types": (str,),
                    "attribute": "filter[debug_id]",
                    "location": "query",
                },
                "filter_gnu_build_id": {
                    "openapi_types": (str,),
                    "attribute": "filter[gnu_build_id]",
                    "location": "query",
                },
                "filter_go_build_id": {
                    "openapi_types": (str,),
                    "attribute": "filter[go_build_id]",
                    "location": "query",
                },
                "filter_file_hash": {
                    "openapi_types": (str,),
                    "attribute": "filter[file_hash]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._restore_sourcemaps_endpoint = _Endpoint(
            settings={
                "response_type": (SourcemapsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/sourcemaps/restore",
                "operation_id": "restore_sourcemaps",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "mapkind": {
                    "required": True,
                    "openapi_types": (SourcemapMapKind,),
                    "attribute": "mapkind",
                    "location": "query",
                },
                "dry_run": {
                    "required": True,
                    "openapi_types": (bool,),
                    "attribute": "dry_run",
                    "location": "query",
                },
                "filter_service": {
                    "openapi_types": ([str],),
                    "attribute": "filter[service]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_version": {
                    "openapi_types": ([str],),
                    "attribute": "filter[version]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_variant": {
                    "openapi_types": ([str],),
                    "attribute": "filter[variant]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_id": {
                    "openapi_types": ([str],),
                    "attribute": "filter[id]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_build_id": {
                    "openapi_types": ([str],),
                    "attribute": "filter[build_id]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_uuid": {
                    "openapi_types": ([str],),
                    "attribute": "filter[uuid]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_platform": {
                    "openapi_types": ([str],),
                    "attribute": "filter[platform]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_build_number": {
                    "openapi_types": ([str],),
                    "attribute": "filter[build_number]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_bundle_name": {
                    "openapi_types": ([str],),
                    "attribute": "filter[bundle_name]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_arch": {
                    "openapi_types": ([str],),
                    "attribute": "filter[arch]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_symbol_source": {
                    "openapi_types": ([str],),
                    "attribute": "filter[symbol_source]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_origin": {
                    "openapi_types": ([str],),
                    "attribute": "filter[origin]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_origin_version": {
                    "openapi_types": ([str],),
                    "attribute": "filter[origin_version]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_filename": {
                    "openapi_types": (str,),
                    "attribute": "filter[filename]",
                    "location": "query",
                },
                "filter_debug_id": {
                    "openapi_types": (str,),
                    "attribute": "filter[debug_id]",
                    "location": "query",
                },
                "filter_gnu_build_id": {
                    "openapi_types": (str,),
                    "attribute": "filter[gnu_build_id]",
                    "location": "query",
                },
                "filter_go_build_id": {
                    "openapi_types": (str,),
                    "attribute": "filter[go_build_id]",
                    "location": "query",
                },
                "filter_file_hash": {
                    "openapi_types": (str,),
                    "attribute": "filter[file_hash]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._search_rum_events_endpoint = _Endpoint(
            settings={
                "response_type": (RUMEventsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/events/search",
                "operation_id": "search_rum_events",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (RUMSearchEventsRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_rum_application_endpoint = _Endpoint(
            settings={
                "response_type": (RUMApplicationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/applications/{id}",
                "operation_id": "update_rum_application",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (RUMApplicationUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def aggregate_rum_events(
        self,
        body: RUMAggregateRequest,
    ) -> RUMAnalyticsAggregateResponse:
        """Aggregate RUM events.

        The API endpoint to aggregate RUM events into buckets of computed metrics and timeseries.

        :type body: RUMAggregateRequest
        :rtype: RUMAnalyticsAggregateResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._aggregate_rum_events_endpoint.call_with_http_info(**kwargs)

    def create_rum_application(
        self,
        body: RUMApplicationCreateRequest,
    ) -> RUMApplicationResponse:
        """Create a new RUM application.

        Create a new RUM application in your organization.

        :type body: RUMApplicationCreateRequest
        :rtype: RUMApplicationResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_rum_application_endpoint.call_with_http_info(**kwargs)

    def delete_rum_application(
        self,
        id: str,
    ) -> None:
        """Delete a RUM application.

        Delete an existing RUM application in your organization.

        :param id: RUM application ID.
        :type id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        return self._delete_rum_application_endpoint.call_with_http_info(**kwargs)

    def delete_sourcemaps(
        self,
        mapkind: SourcemapMapKind,
        dry_run: bool,
        *,
        filter_service: Union[List[str], UnsetType] = unset,
        filter_version: Union[List[str], UnsetType] = unset,
        filter_variant: Union[List[str], UnsetType] = unset,
        filter_id: Union[List[str], UnsetType] = unset,
        filter_build_id: Union[List[str], UnsetType] = unset,
        filter_uuid: Union[List[str], UnsetType] = unset,
        filter_platform: Union[List[str], UnsetType] = unset,
        filter_build_number: Union[List[str], UnsetType] = unset,
        filter_bundle_name: Union[List[str], UnsetType] = unset,
        filter_arch: Union[List[str], UnsetType] = unset,
        filter_symbol_source: Union[List[str], UnsetType] = unset,
        filter_origin: Union[List[str], UnsetType] = unset,
        filter_origin_version: Union[List[str], UnsetType] = unset,
        filter_filename: Union[str, UnsetType] = unset,
        filter_debug_id: Union[str, UnsetType] = unset,
        filter_gnu_build_id: Union[str, UnsetType] = unset,
        filter_go_build_id: Union[str, UnsetType] = unset,
        filter_file_hash: Union[str, UnsetType] = unset,
    ) -> SourcemapsResponse:
        """Delete source maps.

        Deletes source maps matching the specified filter criteria. Supports
        dry-run mode to preview which source maps would be deleted without
        performing the actual deletion.

        :param mapkind: The type of source map. Valid values are ``js`` , ``jvm`` , ``ios`` ,
            ``react`` , ``flutter`` , ``elf`` , ``ndk`` , ``il2cpp``.
        :type mapkind: SourcemapMapKind
        :param dry_run: When set to ``true`` , returns the source maps that would be deleted
            without performing the actual deletion. When set to ``false`` ,
            performs the deletion.
        :type dry_run: bool
        :param filter_service: Filter by service names (multiple values allowed). Required for
            ``js`` , ``jvm`` , ``react`` , and ``flutter`` map kinds.
        :type filter_service: [str], optional
        :param filter_version: Filter by version values (multiple values allowed, maximum 10).
            Required for ``js`` , ``jvm`` , ``react`` , and ``flutter`` map kinds.
        :type filter_version: [str], optional
        :param filter_variant: Filter by variant values (multiple values allowed). Supported for ``jvm``.
        :type filter_variant: [str], optional
        :param filter_id: Filter by source map ID values (multiple values allowed). Supported for all map kinds.
        :type filter_id: [str], optional
        :param filter_build_id: Filter by build ID values (multiple values allowed). Supported for ``jvm`` , ``ndk`` , and ``il2cpp``.
        :type filter_build_id: [str], optional
        :param filter_uuid: Filter by UUID values (multiple values allowed). Supported for ``ios``.
        :type filter_uuid: [str], optional
        :param filter_platform: Filter by platform values (multiple values allowed). Supported for ``react``.
        :type filter_platform: [str], optional
        :param filter_build_number: Filter by build number values (multiple values allowed). Supported for ``react``.
        :type filter_build_number: [str], optional
        :param filter_bundle_name: Filter by bundle name values (multiple values allowed). Supported for ``react``.
        :type filter_bundle_name: [str], optional
        :param filter_arch: Filter by architecture values (multiple values allowed). Supported
            for ``flutter`` , ``elf`` , and ``ndk``.
        :type filter_arch: [str], optional
        :param filter_symbol_source: Filter by symbol source values (multiple values allowed). Supported for ``elf``.
        :type filter_symbol_source: [str], optional
        :param filter_origin: Filter by origin values (multiple values allowed). Supported for ``elf``.
        :type filter_origin: [str], optional
        :param filter_origin_version: Filter by origin version values (multiple values allowed). Supported for ``elf``.
        :type filter_origin_version: [str], optional
        :param filter_filename: Filter by filename (single value). Supported for ``js`` , ``elf`` , and ``ndk``.
        :type filter_filename: str, optional
        :param filter_debug_id: Filter by debug ID (single value). Supported for ``react``.
        :type filter_debug_id: str, optional
        :param filter_gnu_build_id: Filter by GNU build ID (single value). Supported for ``elf``.
        :type filter_gnu_build_id: str, optional
        :param filter_go_build_id: Filter by Go build ID (single value). Supported for ``elf``.
        :type filter_go_build_id: str, optional
        :param filter_file_hash: Filter by file hash (single value). Supported for ``elf``.
        :type filter_file_hash: str, optional
        :rtype: SourcemapsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["mapkind"] = mapkind

        kwargs["dry_run"] = dry_run

        if filter_service is not unset:
            kwargs["filter_service"] = filter_service

        if filter_version is not unset:
            kwargs["filter_version"] = filter_version

        if filter_variant is not unset:
            kwargs["filter_variant"] = filter_variant

        if filter_id is not unset:
            kwargs["filter_id"] = filter_id

        if filter_build_id is not unset:
            kwargs["filter_build_id"] = filter_build_id

        if filter_uuid is not unset:
            kwargs["filter_uuid"] = filter_uuid

        if filter_platform is not unset:
            kwargs["filter_platform"] = filter_platform

        if filter_build_number is not unset:
            kwargs["filter_build_number"] = filter_build_number

        if filter_bundle_name is not unset:
            kwargs["filter_bundle_name"] = filter_bundle_name

        if filter_arch is not unset:
            kwargs["filter_arch"] = filter_arch

        if filter_symbol_source is not unset:
            kwargs["filter_symbol_source"] = filter_symbol_source

        if filter_origin is not unset:
            kwargs["filter_origin"] = filter_origin

        if filter_origin_version is not unset:
            kwargs["filter_origin_version"] = filter_origin_version

        if filter_filename is not unset:
            kwargs["filter_filename"] = filter_filename

        if filter_debug_id is not unset:
            kwargs["filter_debug_id"] = filter_debug_id

        if filter_gnu_build_id is not unset:
            kwargs["filter_gnu_build_id"] = filter_gnu_build_id

        if filter_go_build_id is not unset:
            kwargs["filter_go_build_id"] = filter_go_build_id

        if filter_file_hash is not unset:
            kwargs["filter_file_hash"] = filter_file_hash

        return self._delete_sourcemaps_endpoint.call_with_http_info(**kwargs)

    def get_rum_application(
        self,
        id: str,
    ) -> RUMApplicationResponse:
        """Get a RUM application.

        Get the RUM application with given ID in your organization.

        :param id: RUM application ID.
        :type id: str
        :rtype: RUMApplicationResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        return self._get_rum_application_endpoint.call_with_http_info(**kwargs)

    def get_rum_applications(
        self,
    ) -> RUMApplicationsResponse:
        """List all the RUM applications.

        List all the RUM applications in your organization.

        :rtype: RUMApplicationsResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._get_rum_applications_endpoint.call_with_http_info(**kwargs)

    def get_service_repository_info(
        self,
        body: ServiceRepositoryInfoRequest,
    ) -> ServiceRepositoryInfoResponse:
        """Get service repository information.

        Returns the repository URL and commit SHA associated with a given service and version.

        :type body: ServiceRepositoryInfoRequest
        :rtype: ServiceRepositoryInfoResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._get_service_repository_info_endpoint.call_with_http_info(**kwargs)

    def get_sourcemaps(
        self,
        filename: str,
        service: str,
        version: str,
    ) -> SourcemapFileResponse:
        """Get a JavaScript source map.

        Retrieves the content of a specific JavaScript source map file by its
        filename, service name, and version.

        :param filename: The path to the source map file.
        :type filename: str
        :param service: The service name associated with the source map.
        :type service: str
        :param version: The version of the service associated with the source map.
        :type version: str
        :rtype: SourcemapFileResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["filename"] = filename

        kwargs["service"] = service

        kwargs["version"] = version

        return self._get_sourcemaps_endpoint.call_with_http_info(**kwargs)

    def list_rum_events(
        self,
        *,
        filter_query: Union[str, UnsetType] = unset,
        filter_from: Union[datetime, UnsetType] = unset,
        filter_to: Union[datetime, UnsetType] = unset,
        sort: Union[RUMSort, UnsetType] = unset,
        page_cursor: Union[str, UnsetType] = unset,
        page_limit: Union[int, UnsetType] = unset,
    ) -> RUMEventsResponse:
        """Get a list of RUM events.

        List endpoint returns events that match a RUM search query.
        `Results are paginated <https://docs.datadoghq.com/logs/guide/collect-multiple-logs-with-pagination>`_.

        Use this endpoint to see your latest RUM events.

        :param filter_query: Search query following RUM syntax.
        :type filter_query: str, optional
        :param filter_from: Minimum timestamp for requested events.
        :type filter_from: datetime, optional
        :param filter_to: Maximum timestamp for requested events.
        :type filter_to: datetime, optional
        :param sort: Order of events in results.
        :type sort: RUMSort, optional
        :param page_cursor: List following results with a cursor provided in the previous query.
        :type page_cursor: str, optional
        :param page_limit: Maximum number of events in the response.
        :type page_limit: int, optional
        :rtype: RUMEventsResponse
        """
        kwargs: Dict[str, Any] = {}
        if filter_query is not unset:
            kwargs["filter_query"] = filter_query

        if filter_from is not unset:
            kwargs["filter_from"] = filter_from

        if filter_to is not unset:
            kwargs["filter_to"] = filter_to

        if sort is not unset:
            kwargs["sort"] = sort

        if page_cursor is not unset:
            kwargs["page_cursor"] = page_cursor

        if page_limit is not unset:
            kwargs["page_limit"] = page_limit

        return self._list_rum_events_endpoint.call_with_http_info(**kwargs)

    def list_rum_events_with_pagination(
        self,
        *,
        filter_query: Union[str, UnsetType] = unset,
        filter_from: Union[datetime, UnsetType] = unset,
        filter_to: Union[datetime, UnsetType] = unset,
        sort: Union[RUMSort, UnsetType] = unset,
        page_cursor: Union[str, UnsetType] = unset,
        page_limit: Union[int, UnsetType] = unset,
    ) -> collections.abc.Iterable[RUMEvent]:
        """Get a list of RUM events.

        Provide a paginated version of :meth:`list_rum_events`, returning all items.

        :param filter_query: Search query following RUM syntax.
        :type filter_query: str, optional
        :param filter_from: Minimum timestamp for requested events.
        :type filter_from: datetime, optional
        :param filter_to: Maximum timestamp for requested events.
        :type filter_to: datetime, optional
        :param sort: Order of events in results.
        :type sort: RUMSort, optional
        :param page_cursor: List following results with a cursor provided in the previous query.
        :type page_cursor: str, optional
        :param page_limit: Maximum number of events in the response.
        :type page_limit: int, optional

        :return: A generator of paginated results.
        :rtype: collections.abc.Iterable[RUMEvent]
        """
        kwargs: Dict[str, Any] = {}
        if filter_query is not unset:
            kwargs["filter_query"] = filter_query

        if filter_from is not unset:
            kwargs["filter_from"] = filter_from

        if filter_to is not unset:
            kwargs["filter_to"] = filter_to

        if sort is not unset:
            kwargs["sort"] = sort

        if page_cursor is not unset:
            kwargs["page_cursor"] = page_cursor

        if page_limit is not unset:
            kwargs["page_limit"] = page_limit

        local_page_size = get_attribute_from_path(kwargs, "page_limit", 10)
        endpoint = self._list_rum_events_endpoint
        set_attribute_from_path(kwargs, "page_limit", local_page_size, endpoint.params_map)
        pagination = {
            "limit_value": local_page_size,
            "results_path": "data",
            "cursor_param": "page_cursor",
            "cursor_path": "meta.page.after",
            "endpoint": endpoint,
            "kwargs": kwargs,
        }
        return endpoint.call_with_http_info_paginated(pagination)

    def list_sourcemaps(
        self,
        *,
        mapkind: Union[SourcemapMapKind, UnsetType] = unset,
        page_size: Union[int, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
        filter_service: Union[List[str], UnsetType] = unset,
        filter_version: Union[List[str], UnsetType] = unset,
        filter_variant: Union[List[str], UnsetType] = unset,
        filter_id: Union[List[str], UnsetType] = unset,
        filter_build_id: Union[List[str], UnsetType] = unset,
        filter_uuid: Union[List[str], UnsetType] = unset,
        filter_platform: Union[List[str], UnsetType] = unset,
        filter_build_number: Union[List[str], UnsetType] = unset,
        filter_bundle_name: Union[List[str], UnsetType] = unset,
        filter_arch: Union[List[str], UnsetType] = unset,
        filter_symbol_source: Union[List[str], UnsetType] = unset,
        filter_origin: Union[List[str], UnsetType] = unset,
        filter_origin_version: Union[List[str], UnsetType] = unset,
        filter_filename: Union[str, UnsetType] = unset,
        filter_debug_id: Union[str, UnsetType] = unset,
        filter_gnu_build_id: Union[str, UnsetType] = unset,
        filter_go_build_id: Union[str, UnsetType] = unset,
        filter_file_hash: Union[str, UnsetType] = unset,
    ) -> ListSourcemapsResponse:
        """List source maps.

        Retrieves a paginated list of source maps matching the specified filter criteria.

        :param mapkind: The type of source map. Defaults to ``js``.
        :type mapkind: SourcemapMapKind, optional
        :param page_size: The number of results to return per page. Must be at least 1.
        :type page_size: int, optional
        :param page_number: The page number to retrieve, starting from 1.
        :type page_number: int, optional
        :param filter_service: Filter by service names (multiple values allowed). Required for
            ``js`` , ``jvm`` , ``react`` , and ``flutter`` map kinds.
        :type filter_service: [str], optional
        :param filter_version: Filter by version values (multiple values allowed). Required for
            ``js`` , ``jvm`` , ``react`` , and ``flutter`` map kinds.
        :type filter_version: [str], optional
        :param filter_variant: Filter by variant values (multiple values allowed). Supported for ``jvm``.
        :type filter_variant: [str], optional
        :param filter_id: Filter by source map ID values (multiple values allowed). Supported for all map kinds.
        :type filter_id: [str], optional
        :param filter_build_id: Filter by build ID values (multiple values allowed). Supported for ``jvm`` , ``ndk`` , and ``il2cpp``.
        :type filter_build_id: [str], optional
        :param filter_uuid: Filter by UUID values (multiple values allowed). Supported for ``ios``.
        :type filter_uuid: [str], optional
        :param filter_platform: Filter by platform values (multiple values allowed). Supported for ``react``.
        :type filter_platform: [str], optional
        :param filter_build_number: Filter by build number values (multiple values allowed). Supported for ``react``.
        :type filter_build_number: [str], optional
        :param filter_bundle_name: Filter by bundle name values (multiple values allowed). Supported for ``react``.
        :type filter_bundle_name: [str], optional
        :param filter_arch: Filter by architecture values (multiple values allowed). Supported
            for ``flutter`` , ``elf`` , and ``ndk``.
        :type filter_arch: [str], optional
        :param filter_symbol_source: Filter by symbol source values (multiple values allowed). Supported for ``elf``.
        :type filter_symbol_source: [str], optional
        :param filter_origin: Filter by origin values (multiple values allowed). Supported for ``elf``.
        :type filter_origin: [str], optional
        :param filter_origin_version: Filter by origin version values (multiple values allowed). Supported for ``elf``.
        :type filter_origin_version: [str], optional
        :param filter_filename: Filter by filename (single value). Supported for ``js`` , ``elf`` , and ``ndk``.
        :type filter_filename: str, optional
        :param filter_debug_id: Filter by debug ID (single value). Supported for ``react``.
        :type filter_debug_id: str, optional
        :param filter_gnu_build_id: Filter by GNU build ID (single value). Supported for ``elf``.
        :type filter_gnu_build_id: str, optional
        :param filter_go_build_id: Filter by Go build ID (single value). Supported for ``elf``.
        :type filter_go_build_id: str, optional
        :param filter_file_hash: Filter by file hash (single value). Supported for ``elf``.
        :type filter_file_hash: str, optional
        :rtype: ListSourcemapsResponse
        """
        kwargs: Dict[str, Any] = {}
        if mapkind is not unset:
            kwargs["mapkind"] = mapkind

        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_number is not unset:
            kwargs["page_number"] = page_number

        if filter_service is not unset:
            kwargs["filter_service"] = filter_service

        if filter_version is not unset:
            kwargs["filter_version"] = filter_version

        if filter_variant is not unset:
            kwargs["filter_variant"] = filter_variant

        if filter_id is not unset:
            kwargs["filter_id"] = filter_id

        if filter_build_id is not unset:
            kwargs["filter_build_id"] = filter_build_id

        if filter_uuid is not unset:
            kwargs["filter_uuid"] = filter_uuid

        if filter_platform is not unset:
            kwargs["filter_platform"] = filter_platform

        if filter_build_number is not unset:
            kwargs["filter_build_number"] = filter_build_number

        if filter_bundle_name is not unset:
            kwargs["filter_bundle_name"] = filter_bundle_name

        if filter_arch is not unset:
            kwargs["filter_arch"] = filter_arch

        if filter_symbol_source is not unset:
            kwargs["filter_symbol_source"] = filter_symbol_source

        if filter_origin is not unset:
            kwargs["filter_origin"] = filter_origin

        if filter_origin_version is not unset:
            kwargs["filter_origin_version"] = filter_origin_version

        if filter_filename is not unset:
            kwargs["filter_filename"] = filter_filename

        if filter_debug_id is not unset:
            kwargs["filter_debug_id"] = filter_debug_id

        if filter_gnu_build_id is not unset:
            kwargs["filter_gnu_build_id"] = filter_gnu_build_id

        if filter_go_build_id is not unset:
            kwargs["filter_go_build_id"] = filter_go_build_id

        if filter_file_hash is not unset:
            kwargs["filter_file_hash"] = filter_file_hash

        return self._list_sourcemaps_endpoint.call_with_http_info(**kwargs)

    def restore_sourcemaps(
        self,
        mapkind: SourcemapMapKind,
        dry_run: bool,
        *,
        filter_service: Union[List[str], UnsetType] = unset,
        filter_version: Union[List[str], UnsetType] = unset,
        filter_variant: Union[List[str], UnsetType] = unset,
        filter_id: Union[List[str], UnsetType] = unset,
        filter_build_id: Union[List[str], UnsetType] = unset,
        filter_uuid: Union[List[str], UnsetType] = unset,
        filter_platform: Union[List[str], UnsetType] = unset,
        filter_build_number: Union[List[str], UnsetType] = unset,
        filter_bundle_name: Union[List[str], UnsetType] = unset,
        filter_arch: Union[List[str], UnsetType] = unset,
        filter_symbol_source: Union[List[str], UnsetType] = unset,
        filter_origin: Union[List[str], UnsetType] = unset,
        filter_origin_version: Union[List[str], UnsetType] = unset,
        filter_filename: Union[str, UnsetType] = unset,
        filter_debug_id: Union[str, UnsetType] = unset,
        filter_gnu_build_id: Union[str, UnsetType] = unset,
        filter_go_build_id: Union[str, UnsetType] = unset,
        filter_file_hash: Union[str, UnsetType] = unset,
    ) -> SourcemapsResponse:
        """Restore source maps.

        Restores previously deleted source maps matching the specified filter
        criteria. Supports dry-run mode to preview which source maps would be
        restored without performing the actual restoration.

        :param mapkind: The type of source map. Valid values are ``js`` , ``jvm`` , ``ios`` ,
            ``react`` , ``flutter`` , ``elf`` , ``ndk`` , ``il2cpp``.
        :type mapkind: SourcemapMapKind
        :param dry_run: When set to ``true`` , returns the source maps that would be restored
            without performing the actual restoration. When set to ``false`` ,
            performs the restoration.
        :type dry_run: bool
        :param filter_service: Filter by service names (multiple values allowed). Required for
            ``js`` , ``jvm`` , ``react`` , and ``flutter`` map kinds.
        :type filter_service: [str], optional
        :param filter_version: Filter by version values (multiple values allowed, maximum 10).
            Required for ``js`` , ``jvm`` , ``react`` , and ``flutter`` map kinds.
        :type filter_version: [str], optional
        :param filter_variant: Filter by variant values (multiple values allowed). Supported for ``jvm``.
        :type filter_variant: [str], optional
        :param filter_id: Filter by source map ID values (multiple values allowed). Supported for all map kinds.
        :type filter_id: [str], optional
        :param filter_build_id: Filter by build ID values (multiple values allowed). Supported for ``jvm`` , ``ndk`` , and ``il2cpp``.
        :type filter_build_id: [str], optional
        :param filter_uuid: Filter by UUID values (multiple values allowed). Supported for ``ios``.
        :type filter_uuid: [str], optional
        :param filter_platform: Filter by platform values (multiple values allowed). Supported for ``react``.
        :type filter_platform: [str], optional
        :param filter_build_number: Filter by build number values (multiple values allowed). Supported for ``react``.
        :type filter_build_number: [str], optional
        :param filter_bundle_name: Filter by bundle name values (multiple values allowed). Supported for ``react``.
        :type filter_bundle_name: [str], optional
        :param filter_arch: Filter by architecture values (multiple values allowed). Supported
            for ``flutter`` , ``elf`` , and ``ndk``.
        :type filter_arch: [str], optional
        :param filter_symbol_source: Filter by symbol source values (multiple values allowed). Supported for ``elf``.
        :type filter_symbol_source: [str], optional
        :param filter_origin: Filter by origin values (multiple values allowed). Supported for ``elf``.
        :type filter_origin: [str], optional
        :param filter_origin_version: Filter by origin version values (multiple values allowed). Supported for ``elf``.
        :type filter_origin_version: [str], optional
        :param filter_filename: Filter by filename (single value). Supported for ``js`` , ``elf`` , and ``ndk``.
        :type filter_filename: str, optional
        :param filter_debug_id: Filter by debug ID (single value). Supported for ``react``.
        :type filter_debug_id: str, optional
        :param filter_gnu_build_id: Filter by GNU build ID (single value). Supported for ``elf``.
        :type filter_gnu_build_id: str, optional
        :param filter_go_build_id: Filter by Go build ID (single value). Supported for ``elf``.
        :type filter_go_build_id: str, optional
        :param filter_file_hash: Filter by file hash (single value). Supported for ``elf``.
        :type filter_file_hash: str, optional
        :rtype: SourcemapsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["mapkind"] = mapkind

        kwargs["dry_run"] = dry_run

        if filter_service is not unset:
            kwargs["filter_service"] = filter_service

        if filter_version is not unset:
            kwargs["filter_version"] = filter_version

        if filter_variant is not unset:
            kwargs["filter_variant"] = filter_variant

        if filter_id is not unset:
            kwargs["filter_id"] = filter_id

        if filter_build_id is not unset:
            kwargs["filter_build_id"] = filter_build_id

        if filter_uuid is not unset:
            kwargs["filter_uuid"] = filter_uuid

        if filter_platform is not unset:
            kwargs["filter_platform"] = filter_platform

        if filter_build_number is not unset:
            kwargs["filter_build_number"] = filter_build_number

        if filter_bundle_name is not unset:
            kwargs["filter_bundle_name"] = filter_bundle_name

        if filter_arch is not unset:
            kwargs["filter_arch"] = filter_arch

        if filter_symbol_source is not unset:
            kwargs["filter_symbol_source"] = filter_symbol_source

        if filter_origin is not unset:
            kwargs["filter_origin"] = filter_origin

        if filter_origin_version is not unset:
            kwargs["filter_origin_version"] = filter_origin_version

        if filter_filename is not unset:
            kwargs["filter_filename"] = filter_filename

        if filter_debug_id is not unset:
            kwargs["filter_debug_id"] = filter_debug_id

        if filter_gnu_build_id is not unset:
            kwargs["filter_gnu_build_id"] = filter_gnu_build_id

        if filter_go_build_id is not unset:
            kwargs["filter_go_build_id"] = filter_go_build_id

        if filter_file_hash is not unset:
            kwargs["filter_file_hash"] = filter_file_hash

        return self._restore_sourcemaps_endpoint.call_with_http_info(**kwargs)

    def search_rum_events(
        self,
        body: RUMSearchEventsRequest,
    ) -> RUMEventsResponse:
        """Search RUM events.

        List endpoint returns RUM events that match a RUM search query.
        `Results are paginated <https://docs.datadoghq.com/logs/guide/collect-multiple-logs-with-pagination>`_.

        Use this endpoint to build complex RUM events filtering and search.

        :type body: RUMSearchEventsRequest
        :rtype: RUMEventsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._search_rum_events_endpoint.call_with_http_info(**kwargs)

    def search_rum_events_with_pagination(
        self,
        body: RUMSearchEventsRequest,
    ) -> collections.abc.Iterable[RUMEvent]:
        """Search RUM events.

        Provide a paginated version of :meth:`search_rum_events`, returning all items.

        :type body: RUMSearchEventsRequest

        :return: A generator of paginated results.
        :rtype: collections.abc.Iterable[RUMEvent]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        local_page_size = get_attribute_from_path(kwargs, "body.page.limit", 10)
        endpoint = self._search_rum_events_endpoint
        set_attribute_from_path(kwargs, "body.page.limit", local_page_size, endpoint.params_map)
        pagination = {
            "limit_value": local_page_size,
            "results_path": "data",
            "cursor_param": "body.page.cursor",
            "cursor_path": "meta.page.after",
            "endpoint": endpoint,
            "kwargs": kwargs,
        }
        return endpoint.call_with_http_info_paginated(pagination)

    def update_rum_application(
        self,
        id: str,
        body: RUMApplicationUpdateRequest,
    ) -> RUMApplicationResponse:
        """Update a RUM application.

        Update the RUM application with given ID in your organization.

        :param id: RUM application ID.
        :type id: str
        :type body: RUMApplicationUpdateRequest
        :rtype: RUMApplicationResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        kwargs["body"] = body

        return self._update_rum_application_endpoint.call_with_http_info(**kwargs)
