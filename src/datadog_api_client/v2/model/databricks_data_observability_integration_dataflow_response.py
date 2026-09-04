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
    from datadog_api_client.v2.model.databricks_data_observability_integration_dataflow_settings_response import (
        DatabricksDataObservabilityIntegrationDataflowSettingsResponse,
    )


class DatabricksDataObservabilityIntegrationDataflowResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.databricks_data_observability_integration_dataflow_settings_response import (
            DatabricksDataObservabilityIntegrationDataflowSettingsResponse,
        )

        return {
            "enabled": (bool,),
            "settings": (DatabricksDataObservabilityIntegrationDataflowSettingsResponse,),
        }

    attribute_map = {
        "enabled": "enabled",
        "settings": "settings",
    }

    def __init__(
        self_,
        enabled: Union[bool, UnsetType] = unset,
        settings: Union[DatabricksDataObservabilityIntegrationDataflowSettingsResponse, UnsetType] = unset,
        **kwargs,
    ):
        """
        The Databricks data observability dataflow.

        :param enabled: Whether the Databricks dataflow is enabled.
        :type enabled: bool, optional

        :param settings: Settings of the Databricks data observability dataflow.
        :type settings: DatabricksDataObservabilityIntegrationDataflowSettingsResponse, optional
        """
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if settings is not unset:
            kwargs["settings"] = settings
        super().__init__(kwargs)
