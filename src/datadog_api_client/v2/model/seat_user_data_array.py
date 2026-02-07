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
    from datadog_api_client.v2.model.seat_user_data import SeatUserData
    from datadog_api_client.v2.model.seat_user_meta import SeatUserMeta


class SeatUserDataArray(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.seat_user_data import SeatUserData
        from datadog_api_client.v2.model.seat_user_meta import SeatUserMeta

        return {
            "data": ([SeatUserData],),
            "meta": (SeatUserMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(self_, data: List[SeatUserData], meta: Union[SeatUserMeta, UnsetType] = unset, **kwargs):
        """


        :param data: The list of seat users.
        :type data: [SeatUserData]

        :param meta:
        :type meta: SeatUserMeta, optional
        """
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.data = data
