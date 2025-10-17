# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.custom_attribute_configs_response import CustomAttributeConfigsResponse
from datadog_api_client.v2.model.custom_attribute_config_response import CustomAttributeConfigResponse
from datadog_api_client.v2.model.custom_attribute_config_create_request import CustomAttributeConfigCreateRequest


class CaseManagementAttributeApi:
    """
    View and configure custom attributes within Case Management. See the `Case Management page <https://docs.datadoghq.com/service_management/case_management/>`_ for more information.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_custom_attribute_config_endpoint = _Endpoint(
            settings={
                "response_type": (CustomAttributeConfigResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/cases/types/{case_type_id}/custom_attributes",
                "operation_id": "create_custom_attribute_config",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "case_type_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "case_type_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (CustomAttributeConfigCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_custom_attribute_config_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/cases/types/{case_type_id}/custom_attributes/{custom_attribute_id}",
                "operation_id": "delete_custom_attribute_config",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "case_type_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "case_type_id",
                    "location": "path",
                },
                "custom_attribute_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "custom_attribute_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_all_custom_attribute_configs_by_case_type_endpoint = _Endpoint(
            settings={
                "response_type": (CustomAttributeConfigsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/cases/types/{case_type_id}/custom_attributes",
                "operation_id": "get_all_custom_attribute_configs_by_case_type",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "case_type_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "case_type_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_all_custom_attributes_endpoint = _Endpoint(
            settings={
                "response_type": (CustomAttributeConfigsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/cases/types/custom_attributes",
                "operation_id": "get_all_custom_attributes",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

    def create_custom_attribute_config(
        self,
        case_type_id: str,
        body: CustomAttributeConfigCreateRequest,
    ) -> CustomAttributeConfigResponse:
        """Create custom attribute config for a case type.

        Create custom attribute config for a case type

        :param case_type_id: Case type's UUID
        :type case_type_id: str
        :param body: Custom attribute config payload
        :type body: CustomAttributeConfigCreateRequest
        :rtype: CustomAttributeConfigResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["case_type_id"] = case_type_id

        kwargs["body"] = body

        return self._create_custom_attribute_config_endpoint.call_with_http_info(**kwargs)

    def delete_custom_attribute_config(
        self,
        case_type_id: str,
        custom_attribute_id: str,
    ) -> None:
        """Delete custom attributes config.

        Delete custom attribute config

        :param case_type_id: Case type's UUID
        :type case_type_id: str
        :param custom_attribute_id: Case Custom attribute's UUID
        :type custom_attribute_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["case_type_id"] = case_type_id

        kwargs["custom_attribute_id"] = custom_attribute_id

        return self._delete_custom_attribute_config_endpoint.call_with_http_info(**kwargs)

    def get_all_custom_attribute_configs_by_case_type(
        self,
        case_type_id: str,
    ) -> CustomAttributeConfigsResponse:
        """Get all custom attributes config of case type.

        Get all custom attribute config of case type

        :param case_type_id: Case type's UUID
        :type case_type_id: str
        :rtype: CustomAttributeConfigsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["case_type_id"] = case_type_id

        return self._get_all_custom_attribute_configs_by_case_type_endpoint.call_with_http_info(**kwargs)

    def get_all_custom_attributes(
        self,
    ) -> CustomAttributeConfigsResponse:
        """Get all custom attributes.

        Get all custom attributes

        :rtype: CustomAttributeConfigsResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._get_all_custom_attributes_endpoint.call_with_http_info(**kwargs)
