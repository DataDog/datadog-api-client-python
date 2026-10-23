# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.temporal_cloud_open_metrics_integration_account_bearer_token_auth_type import (
        TemporalCloudOpenMetricsIntegrationAccountBearerTokenAuthType,
    )


class TemporalCloudOpenMetricsIntegrationAccountBearerTokenAuthResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.temporal_cloud_open_metrics_integration_account_bearer_token_auth_type import (
            TemporalCloudOpenMetricsIntegrationAccountBearerTokenAuthType,
        )

        return {
            "auth_type": (TemporalCloudOpenMetricsIntegrationAccountBearerTokenAuthType,),
        }

    attribute_map = {
        "auth_type": "auth_type",
    }

    def __init__(self_, auth_type: TemporalCloudOpenMetricsIntegrationAccountBearerTokenAuthType, **kwargs):
        """
        The bearer token authentication method configured on the account.

        :param auth_type: The authentication method type.
        :type auth_type: TemporalCloudOpenMetricsIntegrationAccountBearerTokenAuthType
        """
        super().__init__(kwargs)

        self_.auth_type = auth_type
