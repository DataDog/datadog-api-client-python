# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineDatabricksZerobusDestinationType(ModelSimple):
    """
    The destination type. The value must be `databricks_zerobus`.

    :param value: If omitted defaults to "databricks_zerobus". Must be one of ["databricks_zerobus"].
    :type value: str
    """

    allowed_values = {
        "databricks_zerobus",
    }
    DATABRICKS_ZEROBUS: ClassVar["ObservabilityPipelineDatabricksZerobusDestinationType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineDatabricksZerobusDestinationType.DATABRICKS_ZEROBUS = (
    ObservabilityPipelineDatabricksZerobusDestinationType("databricks_zerobus")
)
