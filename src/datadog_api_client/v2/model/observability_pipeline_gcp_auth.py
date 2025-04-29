# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ObservabilityPipelineGcpAuth(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "credentials_file": (str,),
        }

    attribute_map = {
        "credentials_file": "credentials_file",
    }

    def __init__(self_, credentials_file: str, **kwargs):
        """
        GCP credentials used to authenticate with Google Cloud Storage.

        :param credentials_file: Path to the GCP service account key file.
        :type credentials_file: str
        """
        super().__init__(kwargs)

        self_.credentials_file = credentials_file
