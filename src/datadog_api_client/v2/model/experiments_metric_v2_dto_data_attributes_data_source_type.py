# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsMetricV2DTODataAttributesDataSourceType(ModelSimple):
    """
    Source of the data used to calculate the metric.

    :param value: Must be one of ["DATADOG", "DATADOG_REFERENCE_TABLE", "CUSTOMER_WAREHOUSE", "IMPORTED", "UNKNOWN"].
    :type value: str
    """

    allowed_values = {
        "DATADOG",
        "DATADOG_REFERENCE_TABLE",
        "CUSTOMER_WAREHOUSE",
        "IMPORTED",
        "UNKNOWN",
    }
    DATADOG: ClassVar["ExperimentsMetricV2DTODataAttributesDataSourceType"]
    DATADOG_REFERENCE_TABLE: ClassVar["ExperimentsMetricV2DTODataAttributesDataSourceType"]
    CUSTOMER_WAREHOUSE: ClassVar["ExperimentsMetricV2DTODataAttributesDataSourceType"]
    IMPORTED: ClassVar["ExperimentsMetricV2DTODataAttributesDataSourceType"]
    UNKNOWN: ClassVar["ExperimentsMetricV2DTODataAttributesDataSourceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsMetricV2DTODataAttributesDataSourceType.DATADOG = ExperimentsMetricV2DTODataAttributesDataSourceType(
    "DATADOG"
)
ExperimentsMetricV2DTODataAttributesDataSourceType.DATADOG_REFERENCE_TABLE = (
    ExperimentsMetricV2DTODataAttributesDataSourceType("DATADOG_REFERENCE_TABLE")
)
ExperimentsMetricV2DTODataAttributesDataSourceType.CUSTOMER_WAREHOUSE = (
    ExperimentsMetricV2DTODataAttributesDataSourceType("CUSTOMER_WAREHOUSE")
)
ExperimentsMetricV2DTODataAttributesDataSourceType.IMPORTED = ExperimentsMetricV2DTODataAttributesDataSourceType(
    "IMPORTED"
)
ExperimentsMetricV2DTODataAttributesDataSourceType.UNKNOWN = ExperimentsMetricV2DTODataAttributesDataSourceType(
    "UNKNOWN"
)
