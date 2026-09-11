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
    from datadog_api_client.v2.model.snowflake_event_table_logs_integration_dataflow_settings_request import (
        SnowflakeEventTableLogsIntegrationDataflowSettingsRequest,
    )


class SnowflakeEventTableLogsIntegrationDataflowRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.snowflake_event_table_logs_integration_dataflow_settings_request import (
            SnowflakeEventTableLogsIntegrationDataflowSettingsRequest,
        )

        return {
            "enabled": (bool,),
            "settings": (SnowflakeEventTableLogsIntegrationDataflowSettingsRequest,),
        }

    attribute_map = {
        "enabled": "enabled",
        "settings": "settings",
    }

    def __init__(
        self_,
        enabled: Union[bool, UnsetType] = unset,
        settings: Union[SnowflakeEventTableLogsIntegrationDataflowSettingsRequest, UnsetType] = unset,
        **kwargs,
    ):
        """
        Records from your Snowflake event tables, used to monitor application behavior and identify issues. ``enabled`` turns the dataflow on and off as a whole, and the per-record-type toggles in ``settings`` select which kinds of record it collects while it is on. The Snowflake role needs usage granted on the database, the schema, and the event table itself.

        :param enabled: Whether Datadog collects this data. Defaults to ``false`` ; set to ``true`` to start collection.
        :type enabled: bool, optional

        :param settings: Settings of the event table dataflow. Each record type is collected independently so that you can control ingestion costs, and every record type is ingested into Datadog as logs tagged with its ``record_type``. Only the fields provided are changed.
        :type settings: SnowflakeEventTableLogsIntegrationDataflowSettingsRequest, optional
        """
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if settings is not unset:
            kwargs["settings"] = settings
        super().__init__(kwargs)
