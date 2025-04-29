# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineGoogleCloudStorageDestinationAcl(ModelSimple):
    """
    Access control list setting for objects written to the bucket.

    :param value: Must be one of ["private", "project-private", "public-read", "authenticated-read", "bucket-owner-read", "bucket-owner-full-control"].
    :type value: str
    """

    allowed_values = {
        "private",
        "project-private",
        "public-read",
        "authenticated-read",
        "bucket-owner-read",
        "bucket-owner-full-control",
    }
    PRIVATE: ClassVar["ObservabilityPipelineGoogleCloudStorageDestinationAcl"]
    PROJECTNOT_PRIVATE: ClassVar["ObservabilityPipelineGoogleCloudStorageDestinationAcl"]
    PUBLICNOT_READ: ClassVar["ObservabilityPipelineGoogleCloudStorageDestinationAcl"]
    AUTHENTICATEDNOT_READ: ClassVar["ObservabilityPipelineGoogleCloudStorageDestinationAcl"]
    BUCKETNOT_OWNERNOT_READ: ClassVar["ObservabilityPipelineGoogleCloudStorageDestinationAcl"]
    BUCKETNOT_OWNERNOT_FULLNOT_CONTROL: ClassVar["ObservabilityPipelineGoogleCloudStorageDestinationAcl"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineGoogleCloudStorageDestinationAcl.PRIVATE = ObservabilityPipelineGoogleCloudStorageDestinationAcl(
    "private"
)
ObservabilityPipelineGoogleCloudStorageDestinationAcl.PROJECTNOT_PRIVATE = (
    ObservabilityPipelineGoogleCloudStorageDestinationAcl("project-private")
)
ObservabilityPipelineGoogleCloudStorageDestinationAcl.PUBLICNOT_READ = (
    ObservabilityPipelineGoogleCloudStorageDestinationAcl("public-read")
)
ObservabilityPipelineGoogleCloudStorageDestinationAcl.AUTHENTICATEDNOT_READ = (
    ObservabilityPipelineGoogleCloudStorageDestinationAcl("authenticated-read")
)
ObservabilityPipelineGoogleCloudStorageDestinationAcl.BUCKETNOT_OWNERNOT_READ = (
    ObservabilityPipelineGoogleCloudStorageDestinationAcl("bucket-owner-read")
)
ObservabilityPipelineGoogleCloudStorageDestinationAcl.BUCKETNOT_OWNERNOT_FULLNOT_CONTROL = (
    ObservabilityPipelineGoogleCloudStorageDestinationAcl("bucket-owner-full-control")
)
