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
    from datadog_api_client.v2.model.temporal_cloud_open_metrics_integration_account_authentication_response import (
        TemporalCloudOpenMetricsIntegrationAccountAuthenticationResponse,
    )
    from datadog_api_client.v2.model.temporal_cloud_open_metrics_integration_dataflows_response import (
        TemporalCloudOpenMetricsIntegrationDataflowsResponse,
    )
    from datadog_api_client.v2.model.temporal_cloud_open_metrics_integration_account_settings_response import (
        TemporalCloudOpenMetricsIntegrationAccountSettingsResponse,
    )
    from datadog_api_client.v2.model.temporal_cloud_open_metrics_integration_account_bearer_token_auth_response import (
        TemporalCloudOpenMetricsIntegrationAccountBearerTokenAuthResponse,
    )


class TemporalCloudOpenMetricsIntegrationAccountResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.temporal_cloud_open_metrics_integration_account_authentication_response import (
            TemporalCloudOpenMetricsIntegrationAccountAuthenticationResponse,
        )
        from datadog_api_client.v2.model.temporal_cloud_open_metrics_integration_dataflows_response import (
            TemporalCloudOpenMetricsIntegrationDataflowsResponse,
        )
        from datadog_api_client.v2.model.temporal_cloud_open_metrics_integration_account_settings_response import (
            TemporalCloudOpenMetricsIntegrationAccountSettingsResponse,
        )

        return {
            "authentication": (TemporalCloudOpenMetricsIntegrationAccountAuthenticationResponse,),
            "dataflows": (TemporalCloudOpenMetricsIntegrationDataflowsResponse,),
            "name": (str,),
            "settings": (TemporalCloudOpenMetricsIntegrationAccountSettingsResponse,),
        }

    attribute_map = {
        "authentication": "authentication",
        "dataflows": "dataflows",
        "name": "name",
        "settings": "settings",
    }

    def __init__(
        self_,
        name: str,
        settings: TemporalCloudOpenMetricsIntegrationAccountSettingsResponse,
        authentication: Union[
            TemporalCloudOpenMetricsIntegrationAccountAuthenticationResponse,
            TemporalCloudOpenMetricsIntegrationAccountBearerTokenAuthResponse,
            UnsetType,
        ] = unset,
        dataflows: Union[TemporalCloudOpenMetricsIntegrationDataflowsResponse, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a Temporal Cloud OpenMetrics integration account returned in responses.

        :param authentication: Authentication configured on the Temporal Cloud OpenMetrics integration account.
        :type authentication: TemporalCloudOpenMetricsIntegrationAccountAuthenticationResponse, optional

        :param dataflows: Data Datadog collects from Temporal Cloud OpenMetrics, keyed by dataflow id.
        :type dataflows: TemporalCloudOpenMetricsIntegrationDataflowsResponse, optional

        :param name: Human-readable name of the Temporal Cloud OpenMetrics integration account.
        :type name: str

        :param settings: Settings configured on the Temporal Cloud OpenMetrics integration account.
        :type settings: TemporalCloudOpenMetricsIntegrationAccountSettingsResponse
        """
        if authentication is not unset:
            kwargs["authentication"] = authentication
        if dataflows is not unset:
            kwargs["dataflows"] = dataflows
        super().__init__(kwargs)

        self_.name = name
        self_.settings = settings
