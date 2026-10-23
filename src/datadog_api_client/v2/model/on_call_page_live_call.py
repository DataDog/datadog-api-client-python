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
    from datadog_api_client.v2.model.on_call_page_live_call_over import OnCallPageLiveCallOver


class OnCallPageLiveCall(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.on_call_page_live_call_over import OnCallPageLiveCallOver

        return {
            "call_over": (OnCallPageLiveCallOver,),
        }

    attribute_map = {
        "call_over": "call_over",
    }

    def __init__(self_, call_over: Union[OnCallPageLiveCallOver, UnsetType] = unset, **kwargs):
        """
        Live call information for a page triggered by a live call route.

        :param call_over: Information about a live call that has ended.
        :type call_over: OnCallPageLiveCallOver, optional
        """
        if call_over is not unset:
            kwargs["call_over"] = call_over
        super().__init__(kwargs)
