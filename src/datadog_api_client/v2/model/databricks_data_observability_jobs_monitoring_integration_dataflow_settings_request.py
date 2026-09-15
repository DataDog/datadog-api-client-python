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


class DatabricksDataObservabilityJobsMonitoringIntegrationDataflowSettingsRequest(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "dd_api_key_id": (str,),
            "dd_api_key_secret": (str,),
            "djm_global_init_script_enabled": (bool,),
            "script_gpum_enabled": (bool,),
            "script_logs_enabled": (bool,),
            "serverless_jobs_enabled": (bool,),
        }

    attribute_map = {
        "dd_api_key_id": "dd_api_key_id",
        "dd_api_key_secret": "dd_api_key_secret",
        "djm_global_init_script_enabled": "djm_global_init_script_enabled",
        "script_gpum_enabled": "script_gpum_enabled",
        "script_logs_enabled": "script_logs_enabled",
        "serverless_jobs_enabled": "serverless_jobs_enabled",
    }

    def __init__(
        self_,
        dd_api_key_id: Union[str, UnsetType] = unset,
        dd_api_key_secret: Union[str, UnsetType] = unset,
        djm_global_init_script_enabled: Union[bool, UnsetType] = unset,
        script_gpum_enabled: Union[bool, UnsetType] = unset,
        script_logs_enabled: Union[bool, UnsetType] = unset,
        serverless_jobs_enabled: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Settings of the Data Jobs Monitoring dataflow. Only the fields provided are changed.

        :param dd_api_key_id: ID of the Datadog API key the global init script uses to submit data. Setting or changing it requires ``dd_api_key_secret`` in the same request.
        :type dd_api_key_id: str, optional

        :param dd_api_key_secret: Secret value of the Datadog API key identified by ``dd_api_key_id``.
        :type dd_api_key_secret: str, optional

        :param djm_global_init_script_enabled: Whether Datadog installs and manages the Agent on your Databricks clusters through a global init script. Installation can take up to 15 minutes and requires Databricks Workspace Admin permissions. The script does not apply to clusters in Standard access mode. Leave this ``false`` to install the Agent yourself. Defaults to ``false``.
        :type djm_global_init_script_enabled: bool, optional

        :param script_gpum_enabled: Whether GPU metrics are collected from your Databricks clusters. The Agent installed by the global init script performs the collection, so this requires the dataflow to be enabled with ``djm_global_init_script_enabled`` set to ``true``. Defaults to ``false``.
        :type script_gpum_enabled: bool, optional

        :param script_logs_enabled: Whether driver and worker logs are collected from your Databricks clusters. The Agent installed by the global init script performs the collection, so this requires the dataflow to be enabled with ``djm_global_init_script_enabled`` set to ``true``. Defaults to ``false``.
        :type script_logs_enabled: bool, optional

        :param serverless_jobs_enabled: Whether health and cost data is collected for jobs running on Serverless or SQL Warehouse compute. This compute has no clusters for the global init script to target, so collection reads the Databricks system tables and requires ``system_tables_sql_warehouse_id``. Defaults to ``true``.
        :type serverless_jobs_enabled: bool, optional
        """
        if dd_api_key_id is not unset:
            kwargs["dd_api_key_id"] = dd_api_key_id
        if dd_api_key_secret is not unset:
            kwargs["dd_api_key_secret"] = dd_api_key_secret
        if djm_global_init_script_enabled is not unset:
            kwargs["djm_global_init_script_enabled"] = djm_global_init_script_enabled
        if script_gpum_enabled is not unset:
            kwargs["script_gpum_enabled"] = script_gpum_enabled
        if script_logs_enabled is not unset:
            kwargs["script_logs_enabled"] = script_logs_enabled
        if serverless_jobs_enabled is not unset:
            kwargs["serverless_jobs_enabled"] = serverless_jobs_enabled
        super().__init__(kwargs)
