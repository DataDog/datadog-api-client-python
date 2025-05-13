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
    from datadog_api_client.v2.model.shift_data import ShiftData
    from datadog_api_client.v2.model.shift_included import ShiftIncluded
    from datadog_api_client.v2.model.schedule_user import ScheduleUser


class Shift(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.shift_data import ShiftData
        from datadog_api_client.v2.model.shift_included import ShiftIncluded

        return {
            "data": (ShiftData,),
            "included": ([ShiftIncluded],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }

    def __init__(
        self_,
        data: Union[ShiftData, UnsetType] = unset,
        included: Union[List[Union[ShiftIncluded, ScheduleUser]], UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``Shift`` object.

        :param data: The definition of ``ShiftData`` object.
        :type data: ShiftData, optional

        :param included: The ``Shift`` ``included``.
        :type included: [ShiftIncluded], optional
        """
        if data is not unset:
            kwargs["data"] = data
        if included is not unset:
            kwargs["included"] = included
        super().__init__(kwargs)
