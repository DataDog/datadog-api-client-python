# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.usage_specified_custom_reports_data import UsageSpecifiedCustomReportsData
    from datadog_api_client.v1.model.usage_specified_custom_reports_meta import UsageSpecifiedCustomReportsMeta


@dataclass
class UsageSpecifiedCustomReportsResponseJSON:
    id: str
    computed_on: Union[str, UnsetType] = unset
    end_date: Union[str, UnsetType] = unset
    location: Union[str, UnsetType] = unset
    size: Union[int, UnsetType] = unset
    start_date: Union[str, UnsetType] = unset
    tags: Union[List[str], UnsetType] = unset


class UsageSpecifiedCustomReportsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.usage_specified_custom_reports_data import UsageSpecifiedCustomReportsData
        from datadog_api_client.v1.model.usage_specified_custom_reports_meta import UsageSpecifiedCustomReportsMeta

        return {
            "data": (UsageSpecifiedCustomReportsData,),
            "meta": (UsageSpecifiedCustomReportsMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }
    json_api_model = UsageSpecifiedCustomReportsResponseJSON

    def __init__(
        self_,
        data: Union[UsageSpecifiedCustomReportsData, UnsetType] = unset,
        meta: Union[UsageSpecifiedCustomReportsMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        Returns available specified custom reports.

        :param data: Response containing date and type for specified custom reports.
        :type data: UsageSpecifiedCustomReportsData, optional

        :param meta: The object containing document metadata.
        :type meta: UsageSpecifiedCustomReportsMeta, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
