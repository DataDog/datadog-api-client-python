# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsCreateMetricV2RequestDataAttributesDataSourceType(ModelSimple):
    """
    Source of the data backing this metric.

    :param value: Must be one of ["DATADOG", "DATADOG_REFERENCE_TABLE", "CUSTOMER_WAREHOUSE"].
    :type value: str
    """

    allowed_values = {
        "DATADOG",
        "DATADOG_REFERENCE_TABLE",
        "CUSTOMER_WAREHOUSE",
    }
    DATADOG: ClassVar["ExperimentsCreateMetricV2RequestDataAttributesDataSourceType"]
    DATADOG_REFERENCE_TABLE: ClassVar["ExperimentsCreateMetricV2RequestDataAttributesDataSourceType"]
    CUSTOMER_WAREHOUSE: ClassVar["ExperimentsCreateMetricV2RequestDataAttributesDataSourceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsCreateMetricV2RequestDataAttributesDataSourceType.DATADOG = (
    ExperimentsCreateMetricV2RequestDataAttributesDataSourceType("DATADOG")
)
ExperimentsCreateMetricV2RequestDataAttributesDataSourceType.DATADOG_REFERENCE_TABLE = (
    ExperimentsCreateMetricV2RequestDataAttributesDataSourceType("DATADOG_REFERENCE_TABLE")
)
ExperimentsCreateMetricV2RequestDataAttributesDataSourceType.CUSTOMER_WAREHOUSE = (
    ExperimentsCreateMetricV2RequestDataAttributesDataSourceType("CUSTOMER_WAREHOUSE")
)
