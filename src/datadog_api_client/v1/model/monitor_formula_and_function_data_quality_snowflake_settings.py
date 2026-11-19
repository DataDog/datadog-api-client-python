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


class MonitorFormulaAndFunctionDataQualitySnowflakeSettings(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "warehouse": (str,),
        }

    attribute_map = {
        "warehouse": "warehouse",
    }

    def __init__(self_, warehouse: Union[str, UnsetType] = unset, **kwargs):
        """
        Snowflake-specific settings for a data quality monitor.

        :param warehouse: Snowflake warehouse to run this monitor's queries on instead of the integration user's
            default warehouse. The name is case-sensitive, and the Datadog role must have ``USAGE`` on
            the warehouse directly. Ignored for monitors that read catalog metadata instead of
            running queries (such as default row count and freshness on base tables).
        :type warehouse: str, optional
        """
        if warehouse is not unset:
            kwargs["warehouse"] = warehouse
        super().__init__(kwargs)
