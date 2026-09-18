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


class SnowflakeDataObservabilityQualityMonitoringIntegrationDataflowSettingsResponse(ModelNormal):
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
        Settings of the Data Observability dataflow.

        :param do_table_crawler_cron: Cron expression setting how often Datadog crawls your Snowflake table metadata.
        :type do_table_crawler_cron: str, optional

        :param sync_snowflake_system_database: Whether metadata from the Snowflake ``SNOWFLAKE`` system database is included in Data Observability alongside your own databases.
        :type sync_snowflake_system_database: bool, optional
        """
        if do_table_crawler_cron is not unset:
            kwargs["do_table_crawler_cron"] = do_table_crawler_cron
        if sync_snowflake_system_database is not unset:
            kwargs["sync_snowflake_system_database"] = sync_snowflake_system_database
        super().__init__(kwargs)
