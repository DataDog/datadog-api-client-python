# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CloudcraftWidgetDefinitionProvider(ModelSimple):
    """
    Cloud provider for the Cloudcraft widget.

    :param value: Must be one of ["aws", "azure", "gcp", "ndm", "oci"].
    :type value: str
    """

    allowed_values = {
        "aws",
        "azure",
        "gcp",
        "ndm",
        "oci",
    }
    AWS: ClassVar["CloudcraftWidgetDefinitionProvider"]
    AZURE: ClassVar["CloudcraftWidgetDefinitionProvider"]
    GCP: ClassVar["CloudcraftWidgetDefinitionProvider"]
    NDM: ClassVar["CloudcraftWidgetDefinitionProvider"]
    OCI: ClassVar["CloudcraftWidgetDefinitionProvider"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CloudcraftWidgetDefinitionProvider.AWS = CloudcraftWidgetDefinitionProvider("aws")
CloudcraftWidgetDefinitionProvider.AZURE = CloudcraftWidgetDefinitionProvider("azure")
CloudcraftWidgetDefinitionProvider.GCP = CloudcraftWidgetDefinitionProvider("gcp")
CloudcraftWidgetDefinitionProvider.NDM = CloudcraftWidgetDefinitionProvider("ndm")
CloudcraftWidgetDefinitionProvider.OCI = CloudcraftWidgetDefinitionProvider("oci")
