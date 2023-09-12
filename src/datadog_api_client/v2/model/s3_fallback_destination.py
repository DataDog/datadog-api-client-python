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
    from datadog_api_client.v2.model.s3_fallback_destination_integration import S3FallbackDestinationIntegration
    from datadog_api_client.v2.model.s3_fallback_destination_type import S3FallbackDestinationType


class S3FallbackDestination(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.s3_fallback_destination_integration import S3FallbackDestinationIntegration
        from datadog_api_client.v2.model.s3_fallback_destination_type import S3FallbackDestinationType

        return {
            "bucket": (str,),
            "integration": (S3FallbackDestinationIntegration,),
            "path": (str,),
            "type": (S3FallbackDestinationType,),
        }

    attribute_map = {
        "bucket": "bucket",
        "integration": "integration",
        "path": "path",
        "type": "type",
    }

    def __init__(
        self_,
        bucket: str,
        integration: S3FallbackDestinationIntegration,
        type: S3FallbackDestinationType,
        path: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The S3 archive destination.

        :param bucket: The bucket where the archive will be stored.
        :type bucket: str

        :param integration: The S3 Archive's integration destination.
        :type integration: S3FallbackDestinationIntegration

        :param path: The archive path.
        :type path: str, optional

        :param type: Type of the S3 archive destination.
        :type type: S3FallbackDestinationType
        """
        if path is not unset:
            kwargs["path"] = path
        super().__init__(kwargs)

        self_.bucket = bucket
        self_.integration = integration
        self_.type = type
