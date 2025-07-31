# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.action_connection_integration_update import ActionConnectionIntegrationUpdate
    from datadog_api_client.v2.model.aws_integration_update import AWSIntegrationUpdate
    from datadog_api_client.v2.model.anthropic_integration_update import AnthropicIntegrationUpdate
    from datadog_api_client.v2.model.asana_integration_update import AsanaIntegrationUpdate
    from datadog_api_client.v2.model.azure_integration_update import AzureIntegrationUpdate
    from datadog_api_client.v2.model.circle_ci_integration_update import CircleCIIntegrationUpdate
    from datadog_api_client.v2.model.clickup_integration_update import ClickupIntegrationUpdate
    from datadog_api_client.v2.model.cloudflare_integration_update import CloudflareIntegrationUpdate
    from datadog_api_client.v2.model.config_cat_integration_update import ConfigCatIntegrationUpdate
    from datadog_api_client.v2.model.datadog_integration_update import DatadogIntegrationUpdate
    from datadog_api_client.v2.model.fastly_integration_update import FastlyIntegrationUpdate
    from datadog_api_client.v2.model.freshservice_integration_update import FreshserviceIntegrationUpdate
    from datadog_api_client.v2.model.gcp_integration_update import GCPIntegrationUpdate
    from datadog_api_client.v2.model.gemini_integration_update import GeminiIntegrationUpdate
    from datadog_api_client.v2.model.gitlab_integration_update import GitlabIntegrationUpdate
    from datadog_api_client.v2.model.grey_noise_integration_update import GreyNoiseIntegrationUpdate
    from datadog_api_client.v2.model.http_integration_update import HTTPIntegrationUpdate
    from datadog_api_client.v2.model.launch_darkly_integration_update import LaunchDarklyIntegrationUpdate
    from datadog_api_client.v2.model.notion_integration_update import NotionIntegrationUpdate
    from datadog_api_client.v2.model.okta_integration_update import OktaIntegrationUpdate
    from datadog_api_client.v2.model.open_ai_integration_update import OpenAIIntegrationUpdate
    from datadog_api_client.v2.model.service_now_integration_update import ServiceNowIntegrationUpdate
    from datadog_api_client.v2.model.split_integration_update import SplitIntegrationUpdate
    from datadog_api_client.v2.model.statsig_integration_update import StatsigIntegrationUpdate
    from datadog_api_client.v2.model.virus_total_integration_update import VirusTotalIntegrationUpdate


class ActionConnectionAttributesUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.action_connection_integration_update import ActionConnectionIntegrationUpdate

        return {
            "integration": (ActionConnectionIntegrationUpdate,),
            "name": (str,),
        }

    attribute_map = {
        "integration": "integration",
        "name": "name",
    }

    def __init__(
        self_,
        integration: Union[
            ActionConnectionIntegrationUpdate,
            AWSIntegrationUpdate,
            AnthropicIntegrationUpdate,
            AsanaIntegrationUpdate,
            AzureIntegrationUpdate,
            CircleCIIntegrationUpdate,
            ClickupIntegrationUpdate,
            CloudflareIntegrationUpdate,
            ConfigCatIntegrationUpdate,
            DatadogIntegrationUpdate,
            FastlyIntegrationUpdate,
            FreshserviceIntegrationUpdate,
            GCPIntegrationUpdate,
            GeminiIntegrationUpdate,
            GitlabIntegrationUpdate,
            GreyNoiseIntegrationUpdate,
            HTTPIntegrationUpdate,
            LaunchDarklyIntegrationUpdate,
            NotionIntegrationUpdate,
            OktaIntegrationUpdate,
            OpenAIIntegrationUpdate,
            ServiceNowIntegrationUpdate,
            SplitIntegrationUpdate,
            StatsigIntegrationUpdate,
            VirusTotalIntegrationUpdate,
            UnsetType,
        ] = unset,
        name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``ActionConnectionAttributesUpdate`` object.

        :param integration: The definition of ``ActionConnectionIntegrationUpdate`` object.
        :type integration: ActionConnectionIntegrationUpdate, optional

        :param name: Name of the connection
        :type name: str, optional
        """
        if integration is not unset:
            kwargs["integration"] = integration
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)
