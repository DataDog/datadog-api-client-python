# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsPatchExperimentV2ResponseDataAttributesSplitByPropertiesItemsColumnType(ModelSimple):
    """
    Type of the Datadog exposure field or Warehouse column.

    :param value: Must be one of ["varchar", "int", "double", "boolean", "varchar_array", "int_array", "double_array", "raw", "STRING", "INTEGER", "FLOAT", "BOOLEAN", "DATE", "TIMESTAMP"].
    :type value: str
    """

    allowed_values = {
        "varchar",
        "int",
        "double",
        "boolean",
        "varchar_array",
        "int_array",
        "double_array",
        "raw",
        "STRING",
        "INTEGER",
        "FLOAT",
        "BOOLEAN",
        "DATE",
        "TIMESTAMP",
    }
    VARCHAR: ClassVar["ExperimentsPatchExperimentV2ResponseDataAttributesSplitByPropertiesItemsColumnType"]
    INT: ClassVar["ExperimentsPatchExperimentV2ResponseDataAttributesSplitByPropertiesItemsColumnType"]
    DOUBLE: ClassVar["ExperimentsPatchExperimentV2ResponseDataAttributesSplitByPropertiesItemsColumnType"]
    BOOLEAN_DATADOG: ClassVar["ExperimentsPatchExperimentV2ResponseDataAttributesSplitByPropertiesItemsColumnType"]
    VARCHAR_ARRAY: ClassVar["ExperimentsPatchExperimentV2ResponseDataAttributesSplitByPropertiesItemsColumnType"]
    INT_ARRAY: ClassVar["ExperimentsPatchExperimentV2ResponseDataAttributesSplitByPropertiesItemsColumnType"]
    DOUBLE_ARRAY: ClassVar["ExperimentsPatchExperimentV2ResponseDataAttributesSplitByPropertiesItemsColumnType"]
    RAW: ClassVar["ExperimentsPatchExperimentV2ResponseDataAttributesSplitByPropertiesItemsColumnType"]
    STRING: ClassVar["ExperimentsPatchExperimentV2ResponseDataAttributesSplitByPropertiesItemsColumnType"]
    INTEGER: ClassVar["ExperimentsPatchExperimentV2ResponseDataAttributesSplitByPropertiesItemsColumnType"]
    FLOAT: ClassVar["ExperimentsPatchExperimentV2ResponseDataAttributesSplitByPropertiesItemsColumnType"]
    BOOLEAN_WAREHOUSE: ClassVar["ExperimentsPatchExperimentV2ResponseDataAttributesSplitByPropertiesItemsColumnType"]
    DATE: ClassVar["ExperimentsPatchExperimentV2ResponseDataAttributesSplitByPropertiesItemsColumnType"]
    TIMESTAMP: ClassVar["ExperimentsPatchExperimentV2ResponseDataAttributesSplitByPropertiesItemsColumnType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsPatchExperimentV2ResponseDataAttributesSplitByPropertiesItemsColumnType.VARCHAR = (
    ExperimentsPatchExperimentV2ResponseDataAttributesSplitByPropertiesItemsColumnType("varchar")
)
ExperimentsPatchExperimentV2ResponseDataAttributesSplitByPropertiesItemsColumnType.INT = (
    ExperimentsPatchExperimentV2ResponseDataAttributesSplitByPropertiesItemsColumnType("int")
)
ExperimentsPatchExperimentV2ResponseDataAttributesSplitByPropertiesItemsColumnType.DOUBLE = (
    ExperimentsPatchExperimentV2ResponseDataAttributesSplitByPropertiesItemsColumnType("double")
)
ExperimentsPatchExperimentV2ResponseDataAttributesSplitByPropertiesItemsColumnType.BOOLEAN_DATADOG = (
    ExperimentsPatchExperimentV2ResponseDataAttributesSplitByPropertiesItemsColumnType("boolean")
)
ExperimentsPatchExperimentV2ResponseDataAttributesSplitByPropertiesItemsColumnType.VARCHAR_ARRAY = (
    ExperimentsPatchExperimentV2ResponseDataAttributesSplitByPropertiesItemsColumnType("varchar_array")
)
ExperimentsPatchExperimentV2ResponseDataAttributesSplitByPropertiesItemsColumnType.INT_ARRAY = (
    ExperimentsPatchExperimentV2ResponseDataAttributesSplitByPropertiesItemsColumnType("int_array")
)
ExperimentsPatchExperimentV2ResponseDataAttributesSplitByPropertiesItemsColumnType.DOUBLE_ARRAY = (
    ExperimentsPatchExperimentV2ResponseDataAttributesSplitByPropertiesItemsColumnType("double_array")
)
ExperimentsPatchExperimentV2ResponseDataAttributesSplitByPropertiesItemsColumnType.RAW = (
    ExperimentsPatchExperimentV2ResponseDataAttributesSplitByPropertiesItemsColumnType("raw")
)
ExperimentsPatchExperimentV2ResponseDataAttributesSplitByPropertiesItemsColumnType.STRING = (
    ExperimentsPatchExperimentV2ResponseDataAttributesSplitByPropertiesItemsColumnType("STRING")
)
ExperimentsPatchExperimentV2ResponseDataAttributesSplitByPropertiesItemsColumnType.INTEGER = (
    ExperimentsPatchExperimentV2ResponseDataAttributesSplitByPropertiesItemsColumnType("INTEGER")
)
ExperimentsPatchExperimentV2ResponseDataAttributesSplitByPropertiesItemsColumnType.FLOAT = (
    ExperimentsPatchExperimentV2ResponseDataAttributesSplitByPropertiesItemsColumnType("FLOAT")
)
ExperimentsPatchExperimentV2ResponseDataAttributesSplitByPropertiesItemsColumnType.BOOLEAN_WAREHOUSE = (
    ExperimentsPatchExperimentV2ResponseDataAttributesSplitByPropertiesItemsColumnType("BOOLEAN")
)
ExperimentsPatchExperimentV2ResponseDataAttributesSplitByPropertiesItemsColumnType.DATE = (
    ExperimentsPatchExperimentV2ResponseDataAttributesSplitByPropertiesItemsColumnType("DATE")
)
ExperimentsPatchExperimentV2ResponseDataAttributesSplitByPropertiesItemsColumnType.TIMESTAMP = (
    ExperimentsPatchExperimentV2ResponseDataAttributesSplitByPropertiesItemsColumnType("TIMESTAMP")
)
