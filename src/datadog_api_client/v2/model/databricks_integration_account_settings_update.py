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


class DatabricksIntegrationAccountSettingsUpdate(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "system_tables_sql_warehouse_id": (str,),
            "workspace_url": (str,),
        }

    attribute_map = {
        "system_tables_sql_warehouse_id": "system_tables_sql_warehouse_id",
        "workspace_url": "workspace_url",
    }

    def __init__(
        self_,
        system_tables_sql_warehouse_id: Union[str, UnsetType] = unset,
        workspace_url: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Settings for updating the Databricks integration account. Only the fields provided are changed.

        :param system_tables_sql_warehouse_id: ID of the SQL warehouse used to query the Databricks system tables.
        :type system_tables_sql_warehouse_id: str, optional

        :param workspace_url: URL of the Databricks workspace.
        :type workspace_url: str, optional
        """
        if system_tables_sql_warehouse_id is not unset:
            kwargs["system_tables_sql_warehouse_id"] = system_tables_sql_warehouse_id
        if workspace_url is not unset:
            kwargs["workspace_url"] = workspace_url
        super().__init__(kwargs)
