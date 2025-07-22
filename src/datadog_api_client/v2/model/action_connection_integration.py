# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class ActionConnectionIntegration(ModelComposed):
    def __init__(self, **kwargs):
        """
        The definition of ``ActionConnectionIntegration`` object.

        :param credentials: The definition of `AWSCredentials` object.
        :type credentials: AWSCredentials

        :param type: The definition of `AWSIntegrationType` object.
        :type type: AWSIntegrationType

        :param base_url: Base HTTP url for the integration
        :type base_url: str
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
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

        return {
            "oneOf": [
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
        }
