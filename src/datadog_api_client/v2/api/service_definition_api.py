# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.v2.model.service_definitions_list_response import ServiceDefinitionsListResponse
from datadog_api_client.v2.model.service_definition_create_response import ServiceDefinitionCreateResponse
from datadog_api_client.v2.model.service_definitions_create_request import ServiceDefinitionsCreateRequest
from datadog_api_client.v2.model.service_definition_v2 import ServiceDefinitionV2
from datadog_api_client.v2.model.service_definition_get_response import ServiceDefinitionGetResponse


class ServiceDefinitionApi:
    """
    API to create, update, retrieve and delete service definitions.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        self._create_or_update_service_definitions_endpoint = _Endpoint(
            settings={
                "response_type": (ServiceDefinitionCreateResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/services/definitions",
                "operation_id": "create_or_update_service_definitions",
                "http_method": "POST",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ServiceDefinitionsCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_service_definition_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/services/definitions/{service_name}",
                "operation_id": "delete_service_definition",
                "http_method": "DELETE",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "service_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "service_name",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._get_service_definition_endpoint = _Endpoint(
            settings={
                "response_type": (ServiceDefinitionGetResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/services/definitions/{service_name}",
                "operation_id": "get_service_definition",
                "http_method": "GET",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "service_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "service_name",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._list_service_definitions_endpoint = _Endpoint(
            settings={
                "response_type": (ServiceDefinitionsListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/services/definitions",
                "operation_id": "list_service_definitions",
                "http_method": "GET",
                "version": "v2",
                "servers": None,
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

    def create_or_update_service_definitions(
        self,
        body: Union[ServiceDefinitionsCreateRequest, ServiceDefinitionV2, str],
    ) -> ServiceDefinitionCreateResponse:
        """Create or update service definition.

        Create or update service definition in the Datadog Service Catalog.

        :param body: Service Definition YAML/JSON.
        :type body: ServiceDefinitionsCreateRequest
        :rtype: ServiceDefinitionCreateResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_or_update_service_definitions_endpoint.call_with_http_info(**kwargs)

    def delete_service_definition(
        self,
        service_name: str,
    ) -> None:
        """Delete a single service definition.

        Delete a single service definition in the Datadog Service Catalog.

        :param service_name: The name of the service.
        :type service_name: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["service_name"] = service_name

        return self._delete_service_definition_endpoint.call_with_http_info(**kwargs)

    def get_service_definition(
        self,
        service_name: str,
    ) -> ServiceDefinitionGetResponse:
        """Get a single service definition.

        Get a single service definition from the Datadog Service Catalog.

        :param service_name: The name of the service.
        :type service_name: str
        :rtype: ServiceDefinitionGetResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["service_name"] = service_name

        return self._get_service_definition_endpoint.call_with_http_info(**kwargs)

    def list_service_definitions(
        self,
    ) -> ServiceDefinitionsListResponse:
        """Get all service definitions.

        Get a list of all service definitions from the Datadog Service Catalog.

        :rtype: ServiceDefinitionsListResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_service_definitions_endpoint.call_with_http_info(**kwargs)
