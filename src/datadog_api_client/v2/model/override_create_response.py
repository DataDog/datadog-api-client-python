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
    from datadog_api_client.v2.model.override_data import OverrideData
    from datadog_api_client.v2.model.override_included import OverrideIncluded
    from datadog_api_client.v2.model.schedule_user import ScheduleUser


class OverrideCreateResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.override_data import OverrideData
        from datadog_api_client.v2.model.override_included import OverrideIncluded

        return {
            "data": ([OverrideData],),
            "included": ([OverrideIncluded],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }

    def __init__(
        self_,
        data: List[OverrideData],
        included: Union[List[Union[OverrideIncluded, ScheduleUser]], UnsetType] = unset,
        **kwargs,
    ):
        """
        The on-call schedule overrides that were created, and any related included resources (such as users).

        :param data: The on-call schedule overrides that were created.
        :type data: [OverrideData]

        :param included: Related resources referenced in the overrides' relationships, such as users.
        :type included: [OverrideIncluded], optional
        """
        if included is not unset:
            kwargs["included"] = included
        super().__init__(kwargs)

        self_.data = data
