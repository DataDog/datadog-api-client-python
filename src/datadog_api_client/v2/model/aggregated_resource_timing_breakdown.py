# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AggregatedResourceTimingBreakdown(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "avg_connect_ms": (float,),
            "avg_dns_ms": (float,),
            "avg_download_ms": (float,),
            "avg_first_byte_ms": (float,),
            "avg_redirect_ms": (float,),
            "avg_ssl_ms": (float,),
        }

    attribute_map = {
        "avg_connect_ms": "avg_connect_ms",
        "avg_dns_ms": "avg_dns_ms",
        "avg_download_ms": "avg_download_ms",
        "avg_first_byte_ms": "avg_first_byte_ms",
        "avg_redirect_ms": "avg_redirect_ms",
        "avg_ssl_ms": "avg_ssl_ms",
    }

    def __init__(
        self_,
        avg_connect_ms: float,
        avg_dns_ms: float,
        avg_download_ms: float,
        avg_first_byte_ms: float,
        avg_redirect_ms: float,
        avg_ssl_ms: float,
        **kwargs,
    ):
        """
        Average timing breakdown per network phase for a resource.

        :param avg_connect_ms: Average TCP connect duration in milliseconds.
        :type avg_connect_ms: float

        :param avg_dns_ms: Average DNS resolution duration in milliseconds.
        :type avg_dns_ms: float

        :param avg_download_ms: Average download phase duration in milliseconds.
        :type avg_download_ms: float

        :param avg_first_byte_ms: Average time to first byte in milliseconds.
        :type avg_first_byte_ms: float

        :param avg_redirect_ms: Average redirect phase duration in milliseconds.
        :type avg_redirect_ms: float

        :param avg_ssl_ms: Average SSL handshake duration in milliseconds.
        :type avg_ssl_ms: float
        """
        super().__init__(kwargs)

        self_.avg_connect_ms = avg_connect_ms
        self_.avg_dns_ms = avg_dns_ms
        self_.avg_download_ms = avg_download_ms
        self_.avg_first_byte_ms = avg_first_byte_ms
        self_.avg_redirect_ms = avg_redirect_ms
        self_.avg_ssl_ms = avg_ssl_ms
