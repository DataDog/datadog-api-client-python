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


class SecurityMonitoringReferenceTable(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "check_presence": (bool,),
            "column_name": (str,),
            "log_field_path": (str,),
            "rule_query_name": (str,),
            "table_name": (str,),
        }

    attribute_map = {
        "check_presence": "checkPresence",
        "column_name": "columnName",
        "log_field_path": "logFieldPath",
        "rule_query_name": "ruleQueryName",
        "table_name": "tableName",
    }

    def __init__(
        self_,
        check_presence: Union[bool, UnsetType] = unset,
        column_name: Union[str, UnsetType] = unset,
        log_field_path: Union[str, UnsetType] = unset,
        rule_query_name: Union[str, UnsetType] = unset,
        table_name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Reference tables used in the queries.

        :param check_presence: Whether to include or exclude the matched values.
        :type check_presence: bool, optional

        :param column_name: The name of the column in the reference table.
        :type column_name: str, optional

        :param log_field_path: The field in the log to match against the reference table.
        :type log_field_path: str, optional

        :param rule_query_name: The name of the query to apply the reference table to.
        :type rule_query_name: str, optional

        :param table_name: The name of the reference table.
        :type table_name: str, optional
        """
        if check_presence is not unset:
            kwargs["check_presence"] = check_presence
        if column_name is not unset:
            kwargs["column_name"] = column_name
        if log_field_path is not unset:
            kwargs["log_field_path"] = log_field_path
        if rule_query_name is not unset:
            kwargs["rule_query_name"] = rule_query_name
        if table_name is not unset:
            kwargs["table_name"] = table_name
        super().__init__(kwargs)
