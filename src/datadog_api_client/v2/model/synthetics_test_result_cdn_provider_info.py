# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.synthetics_test_result_cdn_cache_status import SyntheticsTestResultCdnCacheStatus


class SyntheticsTestResultCdnProviderInfo(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_test_result_cdn_cache_status import (
            SyntheticsTestResultCdnCacheStatus,
        )

        return {
            "cache": (SyntheticsTestResultCdnCacheStatus,),
            "provider": (str,),
        }

    attribute_map = {
        "cache": "cache",
        "provider": "provider",
    }

    def __init__(
        self_,
        cache: Union[SyntheticsTestResultCdnCacheStatus, UnsetType] = unset,
        provider: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        CDN provider details inferred from response headers.

        :param cache: Cache status reported by the CDN for the response.
        :type cache: SyntheticsTestResultCdnCacheStatus, optional

        :param provider: Name of the CDN provider.
        :type provider: str, optional
        """
        if cache is not unset:
            kwargs["cache"] = cache
        if provider is not unset:
            kwargs["provider"] = provider
        super().__init__(kwargs)
