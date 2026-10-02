# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsUpdateExposureSQLModelV2RequestDataType(ModelSimple):
    """
    Exposure SQL models resource type.

    :param value: If omitted defaults to "exposure-sql-models". Must be one of ["exposure-sql-models"].
    :type value: str
    """

    allowed_values = {
        "exposure-sql-models",
    }
    EXPOSURE_SQL_MODELS: ClassVar["ExperimentsUpdateExposureSQLModelV2RequestDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsUpdateExposureSQLModelV2RequestDataType.EXPOSURE_SQL_MODELS = (
    ExperimentsUpdateExposureSQLModelV2RequestDataType("exposure-sql-models")
)
