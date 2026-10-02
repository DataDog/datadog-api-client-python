# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsUpdateMetricSQLModelV2RequestDataType(ModelSimple):
    """
    Metric SQL models resource type.

    :param value: If omitted defaults to "metric-sql-models". Must be one of ["metric-sql-models"].
    :type value: str
    """

    allowed_values = {
        "metric-sql-models",
    }
    METRIC_SQL_MODELS: ClassVar["ExperimentsUpdateMetricSQLModelV2RequestDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsUpdateMetricSQLModelV2RequestDataType.METRIC_SQL_MODELS = ExperimentsUpdateMetricSQLModelV2RequestDataType(
    "metric-sql-models"
)
