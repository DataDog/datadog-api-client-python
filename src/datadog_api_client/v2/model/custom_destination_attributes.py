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
    from datadog_api_client.v2.model.custom_destination_compression_type import CustomDestinationCompressionType
    from datadog_api_client.v2.model.custom_destination_fallback_destination import CustomDestinationFallbackDestination
    from datadog_api_client.v2.model.custom_destination_forwarder_destination import (
        CustomDestinationForwarderDestination,
    )
    from datadog_api_client.v2.model.azure_fallback_destination import AzureFallbackDestination
    from datadog_api_client.v2.model.gcs_fallback_destination import GCSFallbackDestination
    from datadog_api_client.v2.model.s3_fallback_destination import S3FallbackDestination
    from datadog_api_client.v2.model.http_destination import HttpDestination
    from datadog_api_client.v2.model.elasticsearch_destination import ElasticsearchDestination
    from datadog_api_client.v2.model.splunk_hec_destination import SplunkHecDestination


class CustomDestinationAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_destination_compression_type import CustomDestinationCompressionType
        from datadog_api_client.v2.model.custom_destination_fallback_destination import (
            CustomDestinationFallbackDestination,
        )
        from datadog_api_client.v2.model.custom_destination_forwarder_destination import (
            CustomDestinationForwarderDestination,
        )

        return {
            "buffer_max_bytes": (int,),
            "buffer_timeout_seconds": (int,),
            "compression": (CustomDestinationCompressionType,),
            "enabled": (bool,),
            "fallback_destination": (CustomDestinationFallbackDestination,),
            "forwarder_destination": (CustomDestinationForwarderDestination,),
            "max_retry_duration_seconds": (int,),
            "name": (str,),
            "query": (str,),
            "version": (int,),
        }

    attribute_map = {
        "buffer_max_bytes": "bufferMaxBytes",
        "buffer_timeout_seconds": "bufferTimeoutSeconds",
        "compression": "compression",
        "enabled": "enabled",
        "fallback_destination": "fallbackDestination",
        "forwarder_destination": "forwarderDestination",
        "max_retry_duration_seconds": "maxRetryDurationSeconds",
        "name": "name",
        "query": "query",
        "version": "version",
    }

    def __init__(
        self_,
        forwarder_destination: Union[
            CustomDestinationForwarderDestination, HttpDestination, ElasticsearchDestination, SplunkHecDestination
        ],
        name: str,
        version: int,
        buffer_max_bytes: Union[int, UnsetType] = unset,
        buffer_timeout_seconds: Union[int, UnsetType] = unset,
        compression: Union[CustomDestinationCompressionType, UnsetType] = unset,
        enabled: Union[bool, UnsetType] = unset,
        fallback_destination: Union[
            CustomDestinationFallbackDestination,
            AzureFallbackDestination,
            GCSFallbackDestination,
            S3FallbackDestination,
            UnsetType,
        ] = unset,
        max_retry_duration_seconds: Union[int, UnsetType] = unset,
        query: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The custom destination attributes.

        :param buffer_max_bytes: The max amount of bytes to buffer for the custom destination.
        :type buffer_max_bytes: int, optional

        :param buffer_timeout_seconds: The timeout amount in seconds to buffer for the custom destination.
        :type buffer_timeout_seconds: int, optional

        :param compression: The compression method used for the custom destination.
        :type compression: CustomDestinationCompressionType, optional

        :param enabled: The enabled status of the custom destination.
        :type enabled: bool, optional

        :param fallback_destination: The archiving destination to fall back to.
        :type fallback_destination: CustomDestinationFallbackDestination, optional

        :param forwarder_destination: The destination to forward events to.
        :type forwarder_destination: CustomDestinationForwarderDestination

        :param max_retry_duration_seconds: The retry duration in seconds for the custom destination.
        :type max_retry_duration_seconds: int, optional

        :param name: The name of the custom destination.
        :type name: str

        :param query: The search query of the custom destination.
        :type query: str, optional

        :param version: The version of the custom destination to prevent concurrent changes.
        :type version: int
        """
        if buffer_max_bytes is not unset:
            kwargs["buffer_max_bytes"] = buffer_max_bytes
        if buffer_timeout_seconds is not unset:
            kwargs["buffer_timeout_seconds"] = buffer_timeout_seconds
        if compression is not unset:
            kwargs["compression"] = compression
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if fallback_destination is not unset:
            kwargs["fallback_destination"] = fallback_destination
        if max_retry_duration_seconds is not unset:
            kwargs["max_retry_duration_seconds"] = max_retry_duration_seconds
        if query is not unset:
            kwargs["query"] = query
        super().__init__(kwargs)

        self_.forwarder_destination = forwarder_destination
        self_.name = name
        self_.version = version
