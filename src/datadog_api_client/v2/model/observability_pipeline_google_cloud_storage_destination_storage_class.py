# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineGoogleCloudStorageDestinationStorageClass(ModelSimple):
    """
    Storage class used for objects stored in GCS.

    :param value: Must be one of ["STANDARD", "NEARLINE", "COLDLINE", "ARCHIVE"].
    :type value: str
    """

    allowed_values = {
        "STANDARD",
        "NEARLINE",
        "COLDLINE",
        "ARCHIVE",
    }
    STANDARD: ClassVar["ObservabilityPipelineGoogleCloudStorageDestinationStorageClass"]
    NEARLINE: ClassVar["ObservabilityPipelineGoogleCloudStorageDestinationStorageClass"]
    COLDLINE: ClassVar["ObservabilityPipelineGoogleCloudStorageDestinationStorageClass"]
    ARCHIVE: ClassVar["ObservabilityPipelineGoogleCloudStorageDestinationStorageClass"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineGoogleCloudStorageDestinationStorageClass.STANDARD = (
    ObservabilityPipelineGoogleCloudStorageDestinationStorageClass("STANDARD")
)
ObservabilityPipelineGoogleCloudStorageDestinationStorageClass.NEARLINE = (
    ObservabilityPipelineGoogleCloudStorageDestinationStorageClass("NEARLINE")
)
ObservabilityPipelineGoogleCloudStorageDestinationStorageClass.COLDLINE = (
    ObservabilityPipelineGoogleCloudStorageDestinationStorageClass("COLDLINE")
)
ObservabilityPipelineGoogleCloudStorageDestinationStorageClass.ARCHIVE = (
    ObservabilityPipelineGoogleCloudStorageDestinationStorageClass("ARCHIVE")
)
