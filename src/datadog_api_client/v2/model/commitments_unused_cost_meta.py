# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class CommitmentsUnusedCostMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "unused_cost_unavailable": (bool,),
        }

    attribute_map = {
        "unused_cost_unavailable": "unused_cost_unavailable",
    }

    def __init__(self_, unused_cost_unavailable: Union[bool, UnsetType] = unset, **kwargs):
        """
        Metadata reporting that the cost data lacks the unused costs of some commitments, as with Azure exports
        scoped below the billing profile. Utilization is then overstated, and realized savings and effective
        savings rate are upper bounds. Omitted when the unused costs are available.

        :param unused_cost_unavailable: Whether the cost data lacks the unused costs of some commitments.
        :type unused_cost_unavailable: bool, optional
        """
        if unused_cost_unavailable is not unset:
            kwargs["unused_cost_unavailable"] = unused_cost_unavailable
        super().__init__(kwargs)
