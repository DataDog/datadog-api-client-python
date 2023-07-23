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
    from datadog_api_client.v2.model.usage_data_object import UsageDataObject
    from datadog_api_client.v2.model.usage_time_series_object import UsageTimeSeriesObject
    from datadog_api_client.v2.model.hourly_usage_type import HourlyUsageType


@dataclass
class UsageApplicationSecurityMonitoringResponseJSON:
    id: str
    org_name: Union[str, UnsetType] = unset
    product_family: Union[str, UnsetType] = unset
    public_id: Union[str, UnsetType] = unset
    timeseries: Union[List[UsageTimeSeriesObject], UnsetType] = unset
    usage_type: Union[HourlyUsageType, UnsetType] = unset


class UsageApplicationSecurityMonitoringResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.usage_data_object import UsageDataObject

        return {
            "data": ([UsageDataObject],),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = UsageApplicationSecurityMonitoringResponseJSON

    def __init__(self_, data: Union[List[UsageDataObject], UnsetType] = unset, **kwargs):
        """
        Application Security Monitoring usage response.

        :param data: Response containing Application Security Monitoring usage.
        :type data: [UsageDataObject], optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
