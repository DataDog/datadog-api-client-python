# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
)


class WebIntegrationAccountSecrets(ModelNormal):
    def __init__(self_, **kwargs):
        """
        Integration-specific secrets. The shape of this object varies by integration. Secrets
        are write-only and never returned by the API.
        """
        super().__init__(kwargs)
