# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.action_connection_aws_secrets_manager import ActionConnectionAWSSecretsManager
    from datadog_api_client.v2.model.action_connection_integration import ActionConnectionIntegration
    from datadog_api_client.v2.model.aws_integration import AWSIntegration
    from datadog_api_client.v2.model.anthropic_integration import AnthropicIntegration
    from datadog_api_client.v2.model.asana_integration import AsanaIntegration
    from datadog_api_client.v2.model.azure_integration import AzureIntegration
    from datadog_api_client.v2.model.circle_ci_integration import CircleCIIntegration
    from datadog_api_client.v2.model.clickup_integration import ClickupIntegration
    from datadog_api_client.v2.model.cloudflare_integration import CloudflareIntegration
    from datadog_api_client.v2.model.config_cat_integration import ConfigCatIntegration
    from datadog_api_client.v2.model.datadog_integration import DatadogIntegration
    from datadog_api_client.v2.model.fastly_integration import FastlyIntegration
    from datadog_api_client.v2.model.freshservice_integration import FreshserviceIntegration
    from datadog_api_client.v2.model.gcp_integration import GCPIntegration
    from datadog_api_client.v2.model.gemini_integration import GeminiIntegration
    from datadog_api_client.v2.model.github_integration import GithubIntegration
    from datadog_api_client.v2.model.gitlab_integration import GitlabIntegration
    from datadog_api_client.v2.model.grey_noise_integration import GreyNoiseIntegration
    from datadog_api_client.v2.model.http_integration import HTTPIntegration
    from datadog_api_client.v2.model.launch_darkly_integration import LaunchDarklyIntegration
    from datadog_api_client.v2.model.notion_integration import NotionIntegration
    from datadog_api_client.v2.model.okta_integration import OktaIntegration
    from datadog_api_client.v2.model.open_ai_integration import OpenAIIntegration
    from datadog_api_client.v2.model.service_now_integration import ServiceNowIntegration
    from datadog_api_client.v2.model.split_integration import SplitIntegration
    from datadog_api_client.v2.model.statsig_integration import StatsigIntegration
    from datadog_api_client.v2.model.virus_total_integration import VirusTotalIntegration


class ActionConnectionAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.action_connection_aws_secrets_manager import ActionConnectionAWSSecretsManager
        from datadog_api_client.v2.model.action_connection_integration import ActionConnectionIntegration

        return {
            "external_secrets_manager": (ActionConnectionAWSSecretsManager,),
            "integration": (ActionConnectionIntegration,),
            "name": (str,),
            "tags": ([str],),
        }

    attribute_map = {
        "external_secrets_manager": "external_secrets_manager",
        "integration": "integration",
        "name": "name",
        "tags": "tags",
    }

    def __init__(
        self_,
        integration: Union[
            ActionConnectionIntegration,
            AWSIntegration,
            AnthropicIntegration,
            AsanaIntegration,
            AzureIntegration,
            CircleCIIntegration,
            ClickupIntegration,
            CloudflareIntegration,
            ConfigCatIntegration,
            DatadogIntegration,
            FastlyIntegration,
            FreshserviceIntegration,
            GCPIntegration,
            GeminiIntegration,
            GithubIntegration,
            GitlabIntegration,
            GreyNoiseIntegration,
            HTTPIntegration,
            LaunchDarklyIntegration,
            NotionIntegration,
            OktaIntegration,
            OpenAIIntegration,
            ServiceNowIntegration,
            SplitIntegration,
            StatsigIntegration,
            VirusTotalIntegration,
        ],
        name: str,
        external_secrets_manager: Union[ActionConnectionAWSSecretsManager, none_type, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``ActionConnectionAttributes`` object.

        :param external_secrets_manager: AWS Secrets Manager settings shared by the credential references on a ``DATACENTER`` connection. These settings are required whenever a field uses an AWS Secrets Manager reference.
        :type external_secrets_manager: ActionConnectionAWSSecretsManager, none_type, optional

        :param integration: The definition of ``ActionConnectionIntegration`` object.
        :type integration: ActionConnectionIntegration

        :param name: Name of the connection
        :type name: str

        :param tags: Tags associated with the connection. Each tag must follow the ``key:value`` format.
            The ``default`` tag key is reserved.
        :type tags: [str], optional
        """
        if external_secrets_manager is not unset:
            kwargs["external_secrets_manager"] = external_secrets_manager
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)

        self_.integration = integration
        self_.name = name
