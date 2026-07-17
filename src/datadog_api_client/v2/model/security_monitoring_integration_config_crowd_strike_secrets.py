# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SecurityMonitoringIntegrationConfigCrowdStrikeSecrets(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "client_id": (str,),
            "client_secret": (str,),
        }

    attribute_map = {
        "client_id": "client_id",
        "client_secret": "client_secret",
    }

    def __init__(self_, client_id: str, client_secret: str, **kwargs):
        """
        Credentials for a CrowdStrike entity context sync.

        :param client_id: The CrowdStrike API client ID.
        :type client_id: str

        :param client_secret: The CrowdStrike API client secret.
        :type client_secret: str
        """
        super().__init__(kwargs)

        self_.client_id = client_id
        self_.client_secret = client_secret
