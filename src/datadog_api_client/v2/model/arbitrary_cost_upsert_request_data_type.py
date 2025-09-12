# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ArbitraryCostUpsertRequestDataType(ModelSimple):
    """
    Upsert arbitrary rule resource type.

    :param value: If omitted defaults to "upsert_arbitrary_rule". Must be one of ["upsert_arbitrary_rule"].
    :type value: str
    """

    allowed_values = {
        "upsert_arbitrary_rule",
    }
    UPSERT_ARBITRARY_RULE: ClassVar["ArbitraryCostUpsertRequestDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ArbitraryCostUpsertRequestDataType.UPSERT_ARBITRARY_RULE = ArbitraryCostUpsertRequestDataType("upsert_arbitrary_rule")
