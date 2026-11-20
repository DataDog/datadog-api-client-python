# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RetentionGroupByItemsTarget(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["cohort", "return_period"].
    :type value: str
    """

    allowed_values = {
        "cohort",
        "return_period",
    }
    COHORT: ClassVar["RetentionGroupByItemsTarget"]
    RETURN_PERIOD: ClassVar["RetentionGroupByItemsTarget"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RetentionGroupByItemsTarget.COHORT = RetentionGroupByItemsTarget("cohort")
RetentionGroupByItemsTarget.RETURN_PERIOD = RetentionGroupByItemsTarget("return_period")
