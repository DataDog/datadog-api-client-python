# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.synthetics_test_result_cdn_provider_info import SyntheticsTestResultCdnProviderInfo


class SyntheticsTestResultCdnResource(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_test_result_cdn_provider_info import (
            SyntheticsTestResultCdnProviderInfo,
        )

        return {
            "cdn": (SyntheticsTestResultCdnProviderInfo,),
            "resolved_ip": (str,),
            "timestamp": (int,),
            "timings": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        UUID,
                        none_type,
                    )
                },
            ),
        }

    attribute_map = {
        "cdn": "cdn",
        "resolved_ip": "resolved_ip",
        "timestamp": "timestamp",
        "timings": "timings",
    }

    def __init__(
        self_,
        cdn: Union[SyntheticsTestResultCdnProviderInfo, UnsetType] = unset,
        resolved_ip: Union[str, UnsetType] = unset,
        timestamp: Union[int, UnsetType] = unset,
        timings: Union[Dict[str, Any], UnsetType] = unset,
        **kwargs,
    ):
        """
        A CDN resource encountered while executing a browser step.

        :param cdn: CDN provider details inferred from response headers.
        :type cdn: SyntheticsTestResultCdnProviderInfo, optional

        :param resolved_ip: Resolved IP address for the CDN resource.
        :type resolved_ip: str, optional

        :param timestamp: Unix timestamp (ms) of when the resource was fetched.
        :type timestamp: int, optional

        :param timings: Timing breakdown for fetching the CDN resource.
        :type timings: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional
        """
        if cdn is not unset:
            kwargs["cdn"] = cdn
        if resolved_ip is not unset:
            kwargs["resolved_ip"] = resolved_ip
        if timestamp is not unset:
            kwargs["timestamp"] = timestamp
        if timings is not unset:
            kwargs["timings"] = timings
        super().__init__(kwargs)
