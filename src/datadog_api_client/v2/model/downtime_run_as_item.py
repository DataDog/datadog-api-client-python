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
    from datadog_api_client.v2.model.downtime_run_as_principal import DowntimeRunAsPrincipal


class DowntimeRunAsItem(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.downtime_run_as_principal import DowntimeRunAsPrincipal

        return {
            "principals": ([DowntimeRunAsPrincipal],),
        }

    attribute_map = {
        "principals": "principals",
    }

    def __init__(self_, principals: Union[List[DowntimeRunAsPrincipal], UnsetType] = unset, **kwargs):
        """
        A set of principals allowed to act on behalf of the downtime.

        :param principals: List of principals allowed to act on behalf of the downtime.
        :type principals: [DowntimeRunAsPrincipal], optional
        """
        if principals is not unset:
            kwargs["principals"] = principals
        super().__init__(kwargs)
