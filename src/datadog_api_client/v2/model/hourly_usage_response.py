# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


from datadog_api_client.v2.model.hourly_usage_measurement import HourlyUsageMeasurement
from datadog_api_client.v2.model.hourly_usage_measurement import HourlyUsageMeasurement

if TYPE_CHECKING:
    from datadog_api_client.v2.model.hourly_usage import HourlyUsage
    from datadog_api_client.v2.model.hourly_usage_metadata import HourlyUsageMetadata


@dataclass
class HourlyUsageResponseJSON:
    id: str
    measurements: Union[List[HourlyUsageMeasurement], UnsetType] = unset
    org_name: Union[str, UnsetType] = unset
    product_family: Union[str, UnsetType] = unset
    public_id: Union[str, UnsetType] = unset
    region: Union[str, UnsetType] = unset
    timestamp: Union[datetime, UnsetType] = unset


class HourlyUsageResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.hourly_usage import HourlyUsage
        from datadog_api_client.v2.model.hourly_usage_metadata import HourlyUsageMetadata

        return {
            "data": ([HourlyUsage],),
            "meta": (HourlyUsageMetadata,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }
    json_api_model = HourlyUsageResponseJSON

    def __init__(
        self_,
        data: Union[List[HourlyUsage], UnsetType] = unset,
        meta: Union[HourlyUsageMetadata, UnsetType] = unset,
        **kwargs,
    ):
        """
        Hourly usage response.

        :param data: Response containing hourly usage.
        :type data: [HourlyUsage], optional

        :param meta: The object containing document metadata.
        :type meta: HourlyUsageMetadata, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
