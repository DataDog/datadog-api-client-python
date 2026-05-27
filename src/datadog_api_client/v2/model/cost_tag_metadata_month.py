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
    from datadog_api_client.v2.model.cost_tag_metadata_month_type import CostTagMetadataMonthType


class CostTagMetadataMonth(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cost_tag_metadata_month_type import CostTagMetadataMonthType

        return {
            "id": (str,),
            "type": (CostTagMetadataMonthType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: str, type: CostTagMetadataMonthType, **kwargs):
        """
        A month that has Cloud Cost Management tag metadata available for a given provider.

        :param id: The month, in ``YYYY-MM`` format.
        :type id: str

        :param type: Type of the Cloud Cost Management tag metadata month resource.
        :type type: CostTagMetadataMonthType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
