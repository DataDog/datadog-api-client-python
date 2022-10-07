# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.usage_host_hour import UsageHostHour


class UsageHostsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.usage_host_hour import UsageHostHour

        return {
            "usage": ([UsageHostHour],),
        }

    attribute_map = {
        "usage": "usage",
    }

    def __init__(self_, usage: Union[List[UsageHostHour], UnsetType] = unset, **kwargs):
        """
        Host usage response.

        :param usage: An array of objects related to host usage.
        :type usage: [UsageHostHour], optional
        """
        if usage is not unset:
            kwargs["usage"] = usage
        super().__init__(kwargs)
