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
    from datadog_api_client.v2.model.usage_ci_committers_detailed_hour import UsageCICommittersDetailedHour
    from datadog_api_client.v2.model.hourly_usage_metadata import HourlyUsageMetadata


class UsageCICommittersDetailedResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.usage_ci_committers_detailed_hour import UsageCICommittersDetailedHour
        from datadog_api_client.v2.model.hourly_usage_metadata import HourlyUsageMetadata

        return {
            "data": ([UsageCICommittersDetailedHour],),
            "meta": (HourlyUsageMetadata,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: Union[List[UsageCICommittersDetailedHour], UnsetType] = unset,
        meta: Union[HourlyUsageMetadata, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response containing the user email for each CI Committed for each hour for a given organization.

        :param data: An array of objects regarding hourly usage of CI Committers Detailed response.
        :type data: [UsageCICommittersDetailedHour], optional

        :param meta: The object containing document metadata.
        :type meta: HourlyUsageMetadata, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
