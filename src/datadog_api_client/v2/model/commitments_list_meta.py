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
        }

    attribute_map = {
        "committed_spend_unit": "committed_spend_unit",
    }

    def __init__(self_, committed_spend_unit: Union[CommitmentsUnit, UnsetType] = unset, **kwargs):
        """
        Metadata for a commitments list response.

        :param committed_spend_unit: Unit metadata for a numeric metric.
        :type committed_spend_unit: CommitmentsUnit, optional
        """
        if committed_spend_unit is not unset:
            kwargs["committed_spend_unit"] = committed_spend_unit
        super().__init__(kwargs)
