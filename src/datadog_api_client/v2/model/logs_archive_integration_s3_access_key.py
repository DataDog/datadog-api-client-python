# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LogsArchiveIntegrationS3AccessKey(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "access_key_id": (str,),
        }

    attribute_map = {
        "access_key_id": "access_key_id",
    }

    def __init__(self_, access_key_id: str, **kwargs):
        """
        The S3 Archive's integration destination using an access key.

        :param access_key_id: The access key ID for the integration.
        :type access_key_id: str
        """
        super().__init__(kwargs)

        self_.access_key_id = access_key_id
