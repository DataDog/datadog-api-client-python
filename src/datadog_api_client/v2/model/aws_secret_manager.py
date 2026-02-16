# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


class AWSSecretManager(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "connection_id": (UUID,),
            "region": (str,),
        }

    attribute_map = {
        "connection_id": "connection_id",
        "region": "region",
    }

    def __init__(self_, connection_id: UUID, region: str, **kwargs):
        """
        AWS Secrets Manager configuration.

        :param connection_id: The ID of the connection used to access AWS Secrets Manager.
        :type connection_id: UUID

        :param region: The AWS region where the secret is stored.
        :type region: str
        """
        super().__init__(kwargs)

        self_.connection_id = connection_id
        self_.region = region
