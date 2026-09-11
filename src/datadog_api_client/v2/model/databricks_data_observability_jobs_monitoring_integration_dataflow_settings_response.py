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


class DatabricksDataObservabilityJobsMonitoringIntegrationDataflowSettingsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "dd_api_key_id": (str,),
            "djm_global_init_script_enabled": (bool,),
            "script_gpum_enabled": (bool,),
            "script_logs_enabled": (bool,),
            "serverless_jobs_enabled": (bool,),
        }

    attribute_map = {
        "dd_api_key_id": "dd_api_key_id",
        "djm_global_init_script_enabled": "djm_global_init_script_enabled",
        "script_gpum_enabled": "script_gpum_enabled",
        "script_logs_enabled": "script_logs_enabled",
        "serverless_jobs_enabled": "serverless_jobs_enabled",
    }

    def __init__(
        self_,
        dd_api_key_id: Union[str, UnsetType] = unset,
        djm_global_init_script_enabled: Union[bool, UnsetType] = unset,
        script_gpum_enabled: Union[bool, UnsetType] = unset,
        script_logs_enabled: Union[bool, UnsetType] = unset,
        serverless_jobs_enabled: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Settings of the Data Jobs Monitoring dataflow.

        :param dd_api_key_id: ID of the Datadog API key the global init script uses to submit data.
        :type dd_api_key_id: str, optional

        :param djm_global_init_script_enabled: Whether Datadog installs and manages the Agent on your Databricks clusters through a global init script. The script does not apply to clusters in Standard access mode. When ``false`` , the Agent is installed manually.
        :type djm_global_init_script_enabled: bool, optional

        :param script_gpum_enabled: Whether GPU metrics are collected from your Databricks clusters. The Agent installed by the global init script performs the collection, so this requires the dataflow to be enabled with ``djm_global_init_script_enabled`` set to ``true``.
        :type script_gpum_enabled: bool, optional

        :param script_logs_enabled: Whether driver and worker logs are collected from your Databricks clusters. The Agent installed by the global init script performs the collection, so this requires the dataflow to be enabled with ``djm_global_init_script_enabled`` set to ``true``.
        :type script_logs_enabled: bool, optional

        :param serverless_jobs_enabled: Whether health and cost data is collected for jobs running on Serverless or SQL Warehouse compute. This compute has no clusters for the global init script to target, so collection reads the Databricks system tables and requires ``system_tables_sql_warehouse_id``.
        :type serverless_jobs_enabled: bool, optional
        """
        if dd_api_key_id is not unset:
            kwargs["dd_api_key_id"] = dd_api_key_id
        if djm_global_init_script_enabled is not unset:
            kwargs["djm_global_init_script_enabled"] = djm_global_init_script_enabled
        if script_gpum_enabled is not unset:
            kwargs["script_gpum_enabled"] = script_gpum_enabled
        if script_logs_enabled is not unset:
            kwargs["script_logs_enabled"] = script_logs_enabled
        if serverless_jobs_enabled is not unset:
            kwargs["serverless_jobs_enabled"] = serverless_jobs_enabled
        super().__init__(kwargs)
