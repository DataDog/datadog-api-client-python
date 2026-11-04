# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.commitments_unit import CommitmentsUnit


class CommitmentsListMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.commitments_unit import CommitmentsUnit

        return {
            "committed_spend_unit": (CommitmentsUnit,),
            "unused_cost_unavailable": (bool,),
        }

    attribute_map = {
        "committed_spend_unit": "committed_spend_unit",
        "unused_cost_unavailable": "unused_cost_unavailable",
    }

    def __init__(
        self_,
        committed_spend_unit: Union[CommitmentsUnit, UnsetType] = unset,
        unused_cost_unavailable: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Metadata for a commitments list response.

        :param committed_spend_unit: Unit metadata for a numeric metric.
        :type committed_spend_unit: CommitmentsUnit, optional

        :param unused_cost_unavailable: Whether Azure cost data lacks the unused cost of some commitments, for example when an export is
            scoped below the billing profile. When ``true`` , utilization is overstated.
        :type unused_cost_unavailable: bool, optional
        """
        if committed_spend_unit is not unset:
            kwargs["committed_spend_unit"] = committed_spend_unit
        if unused_cost_unavailable is not unset:
            kwargs["unused_cost_unavailable"] = unused_cost_unavailable
        super().__init__(kwargs)
