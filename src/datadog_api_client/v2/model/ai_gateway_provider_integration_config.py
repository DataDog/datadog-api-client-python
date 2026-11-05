# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ai_gateway_custom_provider_supported_operation import (
        AiGatewayCustomProviderSupportedOperation,
    )


class AiGatewayProviderIntegrationConfig(ModelNormal):
    validations = {
        "bedrock_region": {
            "max_length": 64,
        },
        "foundry_project": {
            "max_length": 256,
        },
        "foundry_resource_id": {
            "max_length": 512,
        },
        "location": {
            "max_length": 256,
        },
        "project_id": {
            "max_length": 256,
        },
        "supported_operations": {
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_custom_provider_supported_operation import (
            AiGatewayCustomProviderSupportedOperation,
        )

        return {
            "bedrock_region": (str,),
            "foundry_project": (str,),
            "foundry_resource_id": (str,),
            "location": (str,),
            "project_id": (str,),
            "supported_operations": ([AiGatewayCustomProviderSupportedOperation],),
        }

    attribute_map = {
        "bedrock_region": "bedrock_region",
        "foundry_project": "foundry_project",
        "foundry_resource_id": "foundry_resource_id",
        "location": "location",
        "project_id": "project_id",
        "supported_operations": "supported_operations",
    }

    def __init__(
        self_,
        bedrock_region: Union[str, UnsetType] = unset,
        foundry_project: Union[str, UnsetType] = unset,
        foundry_resource_id: Union[str, UnsetType] = unset,
        location: Union[str, UnsetType] = unset,
        project_id: Union[str, UnsetType] = unset,
        supported_operations: Union[List[AiGatewayCustomProviderSupportedOperation], UnsetType] = unset,
        **kwargs,
    ):
        """
        Provider-specific integration configuration.

        :param bedrock_region: AWS region used for Bedrock model discovery, routing, and request signing.
        :type bedrock_region: str, optional

        :param foundry_project: Azure AI Foundry project name, used to call the project's agents.
        :type foundry_project: str, optional

        :param foundry_resource_id: ARM resource ID of the Azure AI Foundry resource, such as ``/subscriptions/<id>/resourceGroups/<group>/providers/Microsoft.CognitiveServices/accounts/<name>``. Required for ``azure_foundry`` providers.
        :type foundry_resource_id: str, optional

        :param location: GCP location used for Gemini model discovery and credential resolution.
        :type location: str, optional

        :param project_id: GCP project ID used for Gemini model discovery and credential resolution.
        :type project_id: str, optional

        :param supported_operations: Custom provider default for discovered and new manual models. Omit to use Chat Completions. An empty list is invalid.
        :type supported_operations: [AiGatewayCustomProviderSupportedOperation], optional
        """
        if bedrock_region is not unset:
            kwargs["bedrock_region"] = bedrock_region
        if foundry_project is not unset:
            kwargs["foundry_project"] = foundry_project
        if foundry_resource_id is not unset:
            kwargs["foundry_resource_id"] = foundry_resource_id
        if location is not unset:
            kwargs["location"] = location
        if project_id is not unset:
            kwargs["project_id"] = project_id
        if supported_operations is not unset:
            kwargs["supported_operations"] = supported_operations
        super().__init__(kwargs)
