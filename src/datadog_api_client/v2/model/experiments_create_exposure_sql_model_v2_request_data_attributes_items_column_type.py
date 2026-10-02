# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsCreateExposureSQLModelV2RequestDataAttributesItemsColumnType(ModelSimple):
    """
    Data type of a column in the SQL model.

    :param value: Must be one of ["STRING", "INTEGER", "FLOAT", "BOOLEAN", "DATE", "TIMESTAMP"].
    :type value: str
    """

    allowed_values = {
        "STRING",
        "INTEGER",
        "FLOAT",
        "BOOLEAN",
        "DATE",
        "TIMESTAMP",
    }
    STRING: ClassVar["ExperimentsCreateExposureSQLModelV2RequestDataAttributesItemsColumnType"]
    INTEGER: ClassVar["ExperimentsCreateExposureSQLModelV2RequestDataAttributesItemsColumnType"]
    FLOAT: ClassVar["ExperimentsCreateExposureSQLModelV2RequestDataAttributesItemsColumnType"]
    BOOLEAN: ClassVar["ExperimentsCreateExposureSQLModelV2RequestDataAttributesItemsColumnType"]
    DATE: ClassVar["ExperimentsCreateExposureSQLModelV2RequestDataAttributesItemsColumnType"]
    TIMESTAMP: ClassVar["ExperimentsCreateExposureSQLModelV2RequestDataAttributesItemsColumnType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsCreateExposureSQLModelV2RequestDataAttributesItemsColumnType.STRING = (
    ExperimentsCreateExposureSQLModelV2RequestDataAttributesItemsColumnType("STRING")
)
ExperimentsCreateExposureSQLModelV2RequestDataAttributesItemsColumnType.INTEGER = (
    ExperimentsCreateExposureSQLModelV2RequestDataAttributesItemsColumnType("INTEGER")
)
ExperimentsCreateExposureSQLModelV2RequestDataAttributesItemsColumnType.FLOAT = (
    ExperimentsCreateExposureSQLModelV2RequestDataAttributesItemsColumnType("FLOAT")
)
ExperimentsCreateExposureSQLModelV2RequestDataAttributesItemsColumnType.BOOLEAN = (
    ExperimentsCreateExposureSQLModelV2RequestDataAttributesItemsColumnType("BOOLEAN")
)
ExperimentsCreateExposureSQLModelV2RequestDataAttributesItemsColumnType.DATE = (
    ExperimentsCreateExposureSQLModelV2RequestDataAttributesItemsColumnType("DATE")
)
ExperimentsCreateExposureSQLModelV2RequestDataAttributesItemsColumnType.TIMESTAMP = (
    ExperimentsCreateExposureSQLModelV2RequestDataAttributesItemsColumnType("TIMESTAMP")
)
