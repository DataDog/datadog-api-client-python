# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class SnowflakeDataObservabilityQualityMonitoringIntegrationDataflowSettingsRequest(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "do_table_crawler_cron": (str,),
            "sync_snowflake_system_database": (bool,),
        }

    attribute_map = {
        "do_table_crawler_cron": "do_table_crawler_cron",
        "sync_snowflake_system_database": "sync_snowflake_system_database",
    }

    def __init__(
        self_,
        do_table_crawler_cron: Union[str, UnsetType] = unset,
        sync_snowflake_system_database: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Settings of the Data Observability dataflow. Only the fields provided are changed.

        :param do_table_crawler_cron: Cron expression setting how often Datadog crawls your Snowflake table metadata. It takes the five standard fields, with the restriction that the month must be ``*`` and that the day of the month and the day of the week cannot both be constrained. The Datadog UI offers hourly ( ``0 * * * *`` ) and daily ( ``0 0 * * *`` ). Defaults to hourly.
        :type do_table_crawler_cron: str, optional

        :param sync_snowflake_system_database: Whether metadata from the Snowflake ``SNOWFLAKE`` system database is included in Data Observability alongside your own databases. Defaults to ``true``.
        :type sync_snowflake_system_database: bool, optional
        """
        if do_table_crawler_cron is not unset:
            kwargs["do_table_crawler_cron"] = do_table_crawler_cron
        if sync_snowflake_system_database is not unset:
            kwargs["sync_snowflake_system_database"] = sync_snowflake_system_database
        super().__init__(kwargs)
