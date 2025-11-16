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
    from datadog_api_client.v2.model.funnel_response_elapsed_time import FunnelResponseElapsedTime


class FunnelResponseDataAttributesFunnelStepsItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.funnel_response_elapsed_time import FunnelResponseElapsedTime

        return {
            "elapsed_time_to_next_step": (FunnelResponseElapsedTime,),
            "label": (str,),
            "value": (int,),
        }

    attribute_map = {
        "elapsed_time_to_next_step": "elapsed_time_to_next_step",
        "label": "label",
        "value": "value",
    }

    def __init__(
        self_,
        elapsed_time_to_next_step: Union[FunnelResponseElapsedTime, UnsetType] = unset,
        label: Union[str, UnsetType] = unset,
        value: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param elapsed_time_to_next_step:
        :type elapsed_time_to_next_step: FunnelResponseElapsedTime, optional

        :param label:
        :type label: str, optional

        :param value:
        :type value: int, optional
        """
        if elapsed_time_to_next_step is not unset:
            kwargs["elapsed_time_to_next_step"] = elapsed_time_to_next_step
        if label is not unset:
            kwargs["label"] = label
        if value is not unset:
            kwargs["value"] = value
        super().__init__(kwargs)
