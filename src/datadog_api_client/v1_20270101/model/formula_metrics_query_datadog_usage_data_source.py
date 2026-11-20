# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FormulaMetricsQueryDatadogUsageDataSource(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: If omitted defaults to "datadog_usage". Must be one of ["datadog_usage"].
    :type value: str
    """

    allowed_values = {
        "datadog_usage",
    }
    DATADOG_USAGE: ClassVar["FormulaMetricsQueryDatadogUsageDataSource"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FormulaMetricsQueryDatadogUsageDataSource.DATADOG_USAGE = FormulaMetricsQueryDatadogUsageDataSource("datadog_usage")
