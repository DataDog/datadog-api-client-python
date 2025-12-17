# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.slo_count_condition import SLOCountCondition


class SLOCountSpec(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.slo_count_condition import SLOCountCondition

        return {
            "count": (SLOCountCondition,),
        }

    attribute_map = {
        "count": "count",
    }

    def __init__(self_, count: SLOCountCondition, **kwargs):
        """
        A metric SLI specification.

        :param count: A metric SLI specification, composed of three parts: the good events formula, the total events formula,
            and the involved queries.
        :type count: SLOCountCondition
        """
        super().__init__(kwargs)

        self_.count = count
