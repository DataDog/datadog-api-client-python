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
    from datadog_api_client.v2.model.temporal_cloud_open_metrics_integration_account_authentication_update import (
        TemporalCloudOpenMetricsIntegrationAccountAuthenticationUpdate,
    )
    from datadog_api_client.v2.model.temporal_cloud_open_metrics_integration_account_settings_update import (
        TemporalCloudOpenMetricsIntegrationAccountSettingsUpdate,
    )
    from datadog_api_client.v2.model.temporal_cloud_open_metrics_integration_account_bearer_token_auth_update import (
        TemporalCloudOpenMetricsIntegrationAccountBearerTokenAuthUpdate,
    )


class TemporalCloudOpenMetricsIntegrationAccountUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.temporal_cloud_open_metrics_integration_account_authentication_update import (
            TemporalCloudOpenMetricsIntegrationAccountAuthenticationUpdate,
        )
        from datadog_api_client.v2.model.temporal_cloud_open_metrics_integration_account_settings_update import (
            TemporalCloudOpenMetricsIntegrationAccountSettingsUpdate,
        )

        return {
            "authentication": (TemporalCloudOpenMetricsIntegrationAccountAuthenticationUpdate,),
            "name": (str,),
            "settings": (TemporalCloudOpenMetricsIntegrationAccountSettingsUpdate,),
        }

    attribute_map = {
        "authentication": "authentication",
        "name": "name",
        "settings": "settings",
    }

    def __init__(
        self_,
        authentication: Union[
            TemporalCloudOpenMetricsIntegrationAccountAuthenticationUpdate,
            TemporalCloudOpenMetricsIntegrationAccountBearerTokenAuthUpdate,
            UnsetType,
        ] = unset,
        name: Union[str, UnsetType] = unset,
        settings: Union[TemporalCloudOpenMetricsIntegrationAccountSettingsUpdate, UnsetType] = unset,
        **kwargs,
    ):
        """
        Writable attributes used to update a Temporal Cloud OpenMetrics integration account. Every field is optional; only the fields provided are changed.

        :param authentication: Authentication for updating the Temporal Cloud OpenMetrics integration account. Exactly one method is set.
        :type authentication: TemporalCloudOpenMetricsIntegrationAccountAuthenticationUpdate, optional

        :param name: Human-readable name of the Temporal Cloud OpenMetrics integration account.
        :type name: str, optional

        :param settings: Settings for updating the Temporal Cloud OpenMetrics integration account. Only the fields provided are changed.
        :type settings: TemporalCloudOpenMetricsIntegrationAccountSettingsUpdate, optional
        """
        if authentication is not unset:
            kwargs["authentication"] = authentication
        if name is not unset:
            kwargs["name"] = name
        if settings is not unset:
            kwargs["settings"] = settings
        super().__init__(kwargs)
