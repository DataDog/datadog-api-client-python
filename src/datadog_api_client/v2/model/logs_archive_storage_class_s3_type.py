# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class LogsArchiveStorageClassS3Type(ModelSimple):
    """
    The storage class where the archive will be stored.

    :param value: If omitted defaults to "STANDARD". Must be one of ["STANDARD", "STANDARD_IA", "ONEZONE_IA", "INTELLIGENT_TIERING", "GLACIER_IR"].
    :type value: str
    """

    allowed_values = {
        "STANDARD",
        "STANDARD_IA",
        "ONEZONE_IA",
        "INTELLIGENT_TIERING",
        "GLACIER_IR",
    }
    STANDARD: ClassVar["LogsArchiveStorageClassS3Type"]
    STANDARD_IA: ClassVar["LogsArchiveStorageClassS3Type"]
    ONEZONE_IA: ClassVar["LogsArchiveStorageClassS3Type"]
    INTELLIGENT_TIERING: ClassVar["LogsArchiveStorageClassS3Type"]
    GLACIER_IR: ClassVar["LogsArchiveStorageClassS3Type"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


LogsArchiveStorageClassS3Type.STANDARD = LogsArchiveStorageClassS3Type("STANDARD")
LogsArchiveStorageClassS3Type.STANDARD_IA = LogsArchiveStorageClassS3Type("STANDARD_IA")
LogsArchiveStorageClassS3Type.ONEZONE_IA = LogsArchiveStorageClassS3Type("ONEZONE_IA")
LogsArchiveStorageClassS3Type.INTELLIGENT_TIERING = LogsArchiveStorageClassS3Type("INTELLIGENT_TIERING")
LogsArchiveStorageClassS3Type.GLACIER_IR = LogsArchiveStorageClassS3Type("GLACIER_IR")
