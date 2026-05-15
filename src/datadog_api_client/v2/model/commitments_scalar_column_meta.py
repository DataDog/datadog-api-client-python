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
    from datadog_api_client.v2.model.commitments_unit import CommitmentsUnit


class CommitmentsScalarColumnMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.commitments_unit import CommitmentsUnit

        return {
            "unit": (CommitmentsUnit,),
        }

    attribute_map = {
        "unit": "unit",
    }

    def __init__(self_, unit: CommitmentsUnit, **kwargs):
        """
        Metadata for a scalar column, including unit information.

        :param unit: Unit metadata for a numeric metric.
        :type unit: CommitmentsUnit
        """
        super().__init__(kwargs)

        self_.unit = unit
