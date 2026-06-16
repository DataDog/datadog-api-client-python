# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CsmCloudProvider(ModelSimple):
    """
    The cloud provider of a host resource.

    :param value: Must be one of ["aws", "gcp", "azure", "oci"].
    :type value: str
    """

    allowed_values = {
        "aws",
        "gcp",
        "azure",
        "oci",
    }
    AWS: ClassVar["CsmCloudProvider"]
    GCP: ClassVar["CsmCloudProvider"]
    AZURE: ClassVar["CsmCloudProvider"]
    OCI: ClassVar["CsmCloudProvider"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CsmCloudProvider.AWS = CsmCloudProvider("aws")
CsmCloudProvider.GCP = CsmCloudProvider("gcp")
CsmCloudProvider.AZURE = CsmCloudProvider("azure")
CsmCloudProvider.OCI = CsmCloudProvider("oci")
