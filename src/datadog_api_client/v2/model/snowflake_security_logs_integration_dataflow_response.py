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
    from datadog_api_client.v2.model.snowflake_security_logs_integration_dataflow_settings_response import (
        SnowflakeSecurityLogsIntegrationDataflowSettingsResponse,
    )


class SnowflakeSecurityLogsIntegrationDataflowResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.snowflake_security_logs_integration_dataflow_settings_response import (
            SnowflakeSecurityLogsIntegrationDataflowSettingsResponse,
        )

        return {
            "enabled": (bool,),
            "settings": (SnowflakeSecurityLogsIntegrationDataflowSettingsResponse,),
        }

    attribute_map = {
        "enabled": "enabled",
        "settings": "settings",
    }

    def __init__(
        self_,
        enabled: Union[bool, UnsetType] = unset,
        settings: Union[SnowflakeSecurityLogsIntegrationDataflowSettingsResponse, UnsetType] = unset,
        **kwargs,
    ):
        """
        Security logs from the Snowflake ``ACCOUNT_USAGE`` schema, for analyzing the security of your Snowflake account and running threat detection with `Cloud SIEM <https://docs.datadoghq.com/security/cloud_siem/>`_.

        :param enabled: Whether Datadog collects this data.
        :type enabled: bool, optional

        :param settings: Settings of the security logs dataflow.
        :type settings: SnowflakeSecurityLogsIntegrationDataflowSettingsResponse, optional
        """
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if settings is not unset:
            kwargs["settings"] = settings
        super().__init__(kwargs)
