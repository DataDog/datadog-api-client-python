# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.action_connection_aws_secrets_manager_type import (
        ActionConnectionAWSSecretsManagerType,
    )


class ActionConnectionAWSSecretsManager(ModelNormal):
    validations = {
        "region": {
            "min_length": 1,
        },
    }
    _nullable = True

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.action_connection_aws_secrets_manager_type import (
            ActionConnectionAWSSecretsManagerType,
        )

        return {
            "connection_id": (str,),
            "region": (str,),
            "type": (ActionConnectionAWSSecretsManagerType,),
        }

    attribute_map = {
        "connection_id": "connection_id",
        "region": "region",
        "type": "type",
    }

    def __init__(self_, connection_id: str, region: str, type: ActionConnectionAWSSecretsManagerType, **kwargs):
        """
        AWS Secrets Manager settings shared by the credential references on a ``DATACENTER`` connection. These settings are required whenever a field uses an AWS Secrets Manager reference.

        :param connection_id: ID of the AWS connection used to retrieve secrets. This connection must be in the same Datadog organization.
        :type connection_id: str

        :param region: AWS region containing the referenced secrets.
        :type region: str

        :param type: AWS Secrets Manager secret backend.
        :type type: ActionConnectionAWSSecretsManagerType
        """
        super().__init__(kwargs)

        self_.connection_id = connection_id
        self_.region = region
        self_.type = type
