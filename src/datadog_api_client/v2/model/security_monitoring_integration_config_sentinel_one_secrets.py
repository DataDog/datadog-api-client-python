# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SecurityMonitoringIntegrationConfigSentinelOneSecrets(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "api_token": (str,),
        }

    attribute_map = {
        "api_token": "api_token",
    }

    def __init__(self_, api_token: str, **kwargs):
        """
        Credentials for a SentinelOne entity context sync.

        :param api_token: The SentinelOne API token.
        :type api_token: str
        """
        super().__init__(kwargs)

        self_.api_token = api_token
