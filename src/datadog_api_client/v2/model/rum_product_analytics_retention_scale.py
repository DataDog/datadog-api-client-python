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
    from datadog_api_client.v2.model.rum_product_analytics_retention_state import RUMProductAnalyticsRetentionState


class RUMProductAnalyticsRetentionScale(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_product_analytics_retention_state import RUMProductAnalyticsRetentionState

        return {
            "last_modified_at": (int,),
            "state": (RUMProductAnalyticsRetentionState,),
        }

    attribute_map = {
        "last_modified_at": "last_modified_at",
        "state": "state",
    }

    def __init__(
        self_,
        last_modified_at: Union[int, UnsetType] = unset,
        state: Union[RUMProductAnalyticsRetentionState, UnsetType] = unset,
        **kwargs,
    ):
        """
        Product Analytics retention scale configuration.

        :param last_modified_at: Timestamp in milliseconds when this scale was last modified.
        :type last_modified_at: int, optional

        :param state: Controls the retention policy for Product Analytics data derived from RUM events.
        :type state: RUMProductAnalyticsRetentionState, optional
        """
        if last_modified_at is not unset:
            kwargs["last_modified_at"] = last_modified_at
        if state is not unset:
            kwargs["state"] = state
        super().__init__(kwargs)
