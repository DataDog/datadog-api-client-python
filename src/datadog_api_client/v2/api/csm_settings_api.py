# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    UnsetType,
    unset,
)
from datadog_api_client.v2.model.csm_agentless_hosts_response import CsmAgentlessHostsResponse
from datadog_api_client.v2.model.csm_host_facet_info_response import CsmHostFacetInfoResponse
from datadog_api_client.v2.model.csm_agentless_host_facets_response import CsmAgentlessHostFacetsResponse
from datadog_api_client.v2.model.csm_unified_hosts_response import CsmUnifiedHostsResponse
from datadog_api_client.v2.model.csm_unified_host_facets_response import CsmUnifiedHostFacetsResponse


class CSMSettingsApi:
    """
    Datadog Cloud Security Management (CSM) Settings APIs allow you to list and filter
    your cloud hosts monitored by CSM, covering both agentless and agent-based discovery.
    For more information, see `Cloud Security Management <https://docs.datadoghq.com/security/cloud_security_management>`_.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._get_csm_agentless_host_facet_info_endpoint = _Endpoint(
            settings={
                "response_type": (CsmHostFacetInfoResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/csm/settings/agentless_hosts/facet_info",
                "operation_id": "get_csm_agentless_host_facet_info",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "facet": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "facet",
                    "location": "query",
                },
                "search": {
                    "openapi_types": (str,),
                    "attribute": "search",
                    "location": "query",
                },
                "query": {
                    "openapi_types": (str,),
                    "attribute": "query",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_csm_unified_host_facet_info_endpoint = _Endpoint(
            settings={
                "response_type": (CsmHostFacetInfoResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/csm/settings/hosts/facet_info",
                "operation_id": "get_csm_unified_host_facet_info",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "facet": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "facet",
                    "location": "query",
                },
                "search": {
                    "openapi_types": (str,),
                    "attribute": "search",
                    "location": "query",
                },
                "query": {
                    "openapi_types": (str,),
                    "attribute": "query",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_csm_agentless_host_facets_endpoint = _Endpoint(
            settings={
                "response_type": (CsmAgentlessHostFacetsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/csm/settings/agentless_hosts/facets",
                "operation_id": "list_csm_agentless_host_facets",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_csm_agentless_hosts_endpoint = _Endpoint(
            settings={
                "response_type": (CsmAgentlessHostsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/csm/settings/agentless_hosts",
                "operation_id": "list_csm_agentless_hosts",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "page": {
                    "validation": {
                        "inclusive_maximum": 1000000,
                        "inclusive_minimum": 0,
                    },
                    "openapi_types": (int,),
                    "attribute": "page",
                    "location": "query",
                },
                "size": {
                    "validation": {
                        "inclusive_maximum": 100,
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "size",
                    "location": "query",
                },
                "query": {
                    "openapi_types": (str,),
                    "attribute": "query",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_csm_unified_host_facets_endpoint = _Endpoint(
            settings={
                "response_type": (CsmUnifiedHostFacetsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/csm/settings/hosts/facets",
                "operation_id": "list_csm_unified_host_facets",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_csm_unified_hosts_endpoint = _Endpoint(
            settings={
                "response_type": (CsmUnifiedHostsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/csm/settings/hosts",
                "operation_id": "list_csm_unified_hosts",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "page": {
                    "validation": {
                        "inclusive_maximum": 1000000,
                        "inclusive_minimum": 0,
                    },
                    "openapi_types": (int,),
                    "attribute": "page",
                    "location": "query",
                },
                "size": {
                    "validation": {
                        "inclusive_maximum": 100,
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "size",
                    "location": "query",
                },
                "query": {
                    "openapi_types": (str,),
                    "attribute": "query",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

    def get_csm_agentless_host_facet_info(
        self,
        facet: str,
        *,
        search: Union[str, UnsetType] = unset,
        query: Union[str, UnsetType] = unset,
    ) -> CsmHostFacetInfoResponse:
        """Get agentless host facet info.

        Get the value distribution for a specific agentless host facet, with optional search and filtering.

        :param facet: The facet identifier to retrieve value distribution for. Valid values are ``resource_name`` , ``account_id`` , ``resource_type`` , ``cloud_provider`` , ``has_vulnerability_scanning`` , and ``has_posture_management``.
        :type facet: str
        :param search: A search string to filter the facet values.
        :type search: str, optional
        :param query: A filter query to scope the facet value counts.
        :type query: str, optional
        :rtype: CsmHostFacetInfoResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["facet"] = facet

        if search is not unset:
            kwargs["search"] = search

        if query is not unset:
            kwargs["query"] = query

        return self._get_csm_agentless_host_facet_info_endpoint.call_with_http_info(**kwargs)

    def get_csm_unified_host_facet_info(
        self,
        facet: str,
        *,
        search: Union[str, UnsetType] = unset,
        query: Union[str, UnsetType] = unset,
    ) -> CsmHostFacetInfoResponse:
        """Get unified host facet info.

        Get the value distribution for a specific unified host facet, with optional search and filtering.

        :param facet: The facet identifier to retrieve value distribution for. Valid values include ``resource_name`` , ``account_id`` , ``resource_type`` , ``cloud_provider`` , ``agentless_vulnerability_scanning`` , ``agentless_posture_management`` , ``hostname`` , ``agent_version`` , ``os`` , ``cluster_name`` , ``agent_posture_management`` , ``agent_cws_enabled`` , ``agent_csm_vm_hosts_enabled`` , and ``agent_csm_vm_containers_enabled``.
        :type facet: str
        :param search: A search string to filter the facet values.
        :type search: str, optional
        :param query: A filter query to scope the facet value counts.
        :type query: str, optional
        :rtype: CsmHostFacetInfoResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["facet"] = facet

        if search is not unset:
            kwargs["search"] = search

        if query is not unset:
            kwargs["query"] = query

        return self._get_csm_unified_host_facet_info_endpoint.call_with_http_info(**kwargs)

    def list_csm_agentless_host_facets(
        self,
    ) -> CsmAgentlessHostFacetsResponse:
        """List agentless host facets.

        Get the list of available facets for filtering agentless hosts.

        :rtype: CsmAgentlessHostFacetsResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_csm_agentless_host_facets_endpoint.call_with_http_info(**kwargs)

    def list_csm_agentless_hosts(
        self,
        *,
        page: Union[int, UnsetType] = unset,
        size: Union[int, UnsetType] = unset,
        query: Union[str, UnsetType] = unset,
    ) -> CsmAgentlessHostsResponse:
        """List agentless hosts.

        Get the list of agentless hosts for CSM, with optional pagination and filtering.

        :param page: The page index for pagination (zero-based).
        :type page: int, optional
        :param size: The number of agentless hosts to return per page.
        :type size: int, optional
        :param query: A search query string to filter agentless hosts.
        :type query: str, optional
        :rtype: CsmAgentlessHostsResponse
        """
        kwargs: Dict[str, Any] = {}
        if page is not unset:
            kwargs["page"] = page

        if size is not unset:
            kwargs["size"] = size

        if query is not unset:
            kwargs["query"] = query

        return self._list_csm_agentless_hosts_endpoint.call_with_http_info(**kwargs)

    def list_csm_unified_host_facets(
        self,
    ) -> CsmUnifiedHostFacetsResponse:
        """List unified host facets.

        Get the list of available facets for filtering unified hosts.

        :rtype: CsmUnifiedHostFacetsResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_csm_unified_host_facets_endpoint.call_with_http_info(**kwargs)

    def list_csm_unified_hosts(
        self,
        *,
        page: Union[int, UnsetType] = unset,
        size: Union[int, UnsetType] = unset,
        query: Union[str, UnsetType] = unset,
    ) -> CsmUnifiedHostsResponse:
        """List unified hosts.

        Get the list of unified hosts for CSM, combining agent and agentless host data, with optional pagination and filtering.

        :param page: The page index for pagination (zero-based).
        :type page: int, optional
        :param size: The number of hosts to return per page.
        :type size: int, optional
        :param query: A search query string to filter unified hosts.
        :type query: str, optional
        :rtype: CsmUnifiedHostsResponse
        """
        kwargs: Dict[str, Any] = {}
        if page is not unset:
            kwargs["page"] = page

        if size is not unset:
            kwargs["size"] = size

        if query is not unset:
            kwargs["query"] = query

        return self._list_csm_unified_hosts_endpoint.call_with_http_info(**kwargs)
