# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.funnel_response_elapsed_time import FunnelResponseElapsedTime
    from datadog_api_client.v2.model.funnel_response_data_attributes_funnel_steps_items import (
        FunnelResponseDataAttributesFunnelStepsItems,
    )


class FunnelResponseDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.funnel_response_elapsed_time import FunnelResponseElapsedTime
        from datadog_api_client.v2.model.funnel_response_data_attributes_funnel_steps_items import (
            FunnelResponseDataAttributesFunnelStepsItems,
        )

        return {
            "end_to_end_conversion_rate": (float,),
            "end_to_end_elapsed_time": (FunnelResponseElapsedTime,),
            "funnel_steps": ([FunnelResponseDataAttributesFunnelStepsItems],),
            "initial_count": (int,),
        }

    attribute_map = {
        "end_to_end_conversion_rate": "end_to_end_conversion_rate",
        "end_to_end_elapsed_time": "end_to_end_elapsed_time",
        "funnel_steps": "funnel_steps",
        "initial_count": "initial_count",
    }

    def __init__(
        self_,
        end_to_end_conversion_rate: Union[float, UnsetType] = unset,
        end_to_end_elapsed_time: Union[FunnelResponseElapsedTime, UnsetType] = unset,
        funnel_steps: Union[List[FunnelResponseDataAttributesFunnelStepsItems], UnsetType] = unset,
        initial_count: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param end_to_end_conversion_rate:
        :type end_to_end_conversion_rate: float, optional

        :param end_to_end_elapsed_time:
        :type end_to_end_elapsed_time: FunnelResponseElapsedTime, optional

        :param funnel_steps:
        :type funnel_steps: [FunnelResponseDataAttributesFunnelStepsItems], optional

        :param initial_count:
        :type initial_count: int, optional
        """
        if end_to_end_conversion_rate is not unset:
            kwargs["end_to_end_conversion_rate"] = end_to_end_conversion_rate
        if end_to_end_elapsed_time is not unset:
            kwargs["end_to_end_elapsed_time"] = end_to_end_elapsed_time
        if funnel_steps is not unset:
            kwargs["funnel_steps"] = funnel_steps
        if initial_count is not unset:
            kwargs["initial_count"] = initial_count
        super().__init__(kwargs)
