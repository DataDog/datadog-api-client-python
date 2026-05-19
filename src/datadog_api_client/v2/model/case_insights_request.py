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
    from datadog_api_client.v2.model.case_insights_data import CaseInsightsData


class CaseInsightsRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.case_insights_data import CaseInsightsData

        return {
            "data": (CaseInsightsData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: CaseInsightsData, **kwargs):
        """
        Request payload for adding or removing case insights.

        :param data: Data object containing the insights to add or remove.
        :type data: CaseInsightsData
        """
        super().__init__(kwargs)

        self_.data = data
