# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineAzureDataExplorerDestinationAuthClientCertificateKind(ModelSimple):
    """
    The Azure credential kind. The value should always be `client_certificate_credential`.

    :param value: If omitted defaults to "client_certificate_credential". Must be one of ["client_certificate_credential"].
    :type value: str
    """

    allowed_values = {
        "client_certificate_credential",
    }
    CLIENT_CERTIFICATE_CREDENTIAL: ClassVar[
        "ObservabilityPipelineAzureDataExplorerDestinationAuthClientCertificateKind"
    ]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineAzureDataExplorerDestinationAuthClientCertificateKind.CLIENT_CERTIFICATE_CREDENTIAL = (
    ObservabilityPipelineAzureDataExplorerDestinationAuthClientCertificateKind("client_certificate_credential")
)
