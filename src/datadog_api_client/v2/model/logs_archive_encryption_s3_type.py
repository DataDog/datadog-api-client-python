# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class LogsArchiveEncryptionS3Type(ModelSimple):
    """
    Type of S3 encryption for a destination.

    :param value: Must be one of ["NO_OVERRIDE", "SSE_S3", "SSE_KMS"].
    :type value: str
    """

    allowed_values = {
        "NO_OVERRIDE",
        "SSE_S3",
        "SSE_KMS",
    }
    NO_OVERRIDE: ClassVar["LogsArchiveEncryptionS3Type"]
    SSE_S3: ClassVar["LogsArchiveEncryptionS3Type"]
    SSE_KMS: ClassVar["LogsArchiveEncryptionS3Type"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


LogsArchiveEncryptionS3Type.NO_OVERRIDE = LogsArchiveEncryptionS3Type("NO_OVERRIDE")
LogsArchiveEncryptionS3Type.SSE_S3 = LogsArchiveEncryptionS3Type("SSE_S3")
LogsArchiveEncryptionS3Type.SSE_KMS = LogsArchiveEncryptionS3Type("SSE_KMS")
