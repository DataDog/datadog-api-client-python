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
    from datadog_api_client.v2.model.logs_archive_encryption_s3_type import LogsArchiveEncryptionS3Type


class LogsArchiveEncryptionS3(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.logs_archive_encryption_s3_type import LogsArchiveEncryptionS3Type

        return {
            "key": (str,),
            "type": (LogsArchiveEncryptionS3Type,),
        }

    attribute_map = {
        "key": "key",
        "type": "type",
    }

    def __init__(self_, type: LogsArchiveEncryptionS3Type, key: Union[str, UnsetType] = unset, **kwargs):
        """
        The S3 encryption settings.

        :param key: An Amazon Resource Name (ARN) used to identify an AWS KMS key.
        :type key: str, optional

        :param type: Type of S3 encryption for a destination.
        :type type: LogsArchiveEncryptionS3Type
        """
        if key is not unset:
            kwargs["key"] = key
        super().__init__(kwargs)

        self_.type = type
