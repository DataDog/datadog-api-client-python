# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsWarehouseEntryPointFilterOperation(ModelSimple):
    """
    Comparison applied by the warehouse entry-point filter.

    :param value: Must be one of ["IS", "IS_NOT"].
    :type value: str
    """

    allowed_values = {
        "IS",
        "IS_NOT",
    }
    IS: ClassVar["ExperimentsWarehouseEntryPointFilterOperation"]
    IS_NOT: ClassVar["ExperimentsWarehouseEntryPointFilterOperation"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsWarehouseEntryPointFilterOperation.IS = ExperimentsWarehouseEntryPointFilterOperation("IS")
ExperimentsWarehouseEntryPointFilterOperation.IS_NOT = ExperimentsWarehouseEntryPointFilterOperation("IS_NOT")
