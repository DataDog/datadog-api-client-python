# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.temporal_cloud_open_metrics_integration_account_authentication_request import (
        TemporalCloudOpenMetricsIntegrationAccountAuthenticationRequest,
    )
    from datadog_api_client.v2.model.temporal_cloud_open_metrics_integration_account_settings_request import (
        TemporalCloudOpenMetricsIntegrationAccountSettingsRequest,
    )
    from datadog_api_client.v2.model.temporal_cloud_open_metrics_integration_account_bearer_token_auth_request import (
        TemporalCloudOpenMetricsIntegrationAccountBearerTokenAuthRequest,
    )


class TemporalCloudOpenMetricsIntegrationAccountCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.temporal_cloud_open_metrics_integration_account_authentication_request import (
            TemporalCloudOpenMetricsIntegrationAccountAuthenticationRequest,
        )
        from datadog_api_client.v2.model.temporal_cloud_open_metrics_integration_account_settings_request import (
            TemporalCloudOpenMetricsIntegrationAccountSettingsRequest,
        )

        return {
            "authentication": (TemporalCloudOpenMetricsIntegrationAccountAuthenticationRequest,),
            "name": (str,),
            "settings": (TemporalCloudOpenMetricsIntegrationAccountSettingsRequest,),
        }

    attribute_map = {
        "authentication": "authentication",
        "name": "name",
        "settings": "settings",
    }

    def __init__(
        self_,
        authentication: Union[
            TemporalCloudOpenMetricsIntegrationAccountAuthenticationRequest,
            TemporalCloudOpenMetricsIntegrationAccountBearerTokenAuthRequest,
        ],
        name: str,
        settings: TemporalCloudOpenMetricsIntegrationAccountSettingsRequest,
        **kwargs,
    ):
        """
        Writable attributes used to create a Temporal Cloud OpenMetrics integration account.

        :param authentication: Authentication for creating the Temporal Cloud OpenMetrics integration account. Exactly one method is set.
        :type authentication: TemporalCloudOpenMetricsIntegrationAccountAuthenticationRequest

        :param name: Human-readable name of the Temporal Cloud OpenMetrics integration account.
        :type name: str

        :param settings: Settings for creating the Temporal Cloud OpenMetrics integration account.
        :type settings: TemporalCloudOpenMetricsIntegrationAccountSettingsRequest
        """
        super().__init__(kwargs)

        self_.authentication = authentication
        self_.name = name
        self_.settings = settings
