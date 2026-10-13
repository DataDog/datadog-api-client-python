# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineAzureDataExplorerDestinationAuthClientSecretKind(ModelSimple):
    """
    The Azure credential kind. The value should always be `client_secret_credential`.

    :param value: If omitted defaults to "client_secret_credential". Must be one of ["client_secret_credential"].
    :type value: str
    """

    allowed_values = {
        "client_secret_credential",
    }
    CLIENT_SECRET_CREDENTIAL: ClassVar["ObservabilityPipelineAzureDataExplorerDestinationAuthClientSecretKind"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineAzureDataExplorerDestinationAuthClientSecretKind.CLIENT_SECRET_CREDENTIAL = (
    ObservabilityPipelineAzureDataExplorerDestinationAuthClientSecretKind("client_secret_credential")
)
