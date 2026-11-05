# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.action_connection_aws_secrets_manager_type import (
        ActionConnectionAWSSecretsManagerType,
    )


class ActionConnectionAWSSecretsManagerReference(ModelNormal):
    validations = {
        "secret_id": {
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.action_connection_aws_secrets_manager_type import (
            ActionConnectionAWSSecretsManagerType,
        )

        return {
            "key": (str,),
            "secret_id": (str,),
            "type": (ActionConnectionAWSSecretsManagerType,),
            "version_id": (str,),
            "version_stage": (str,),
        }

    attribute_map = {
        "key": "key",
        "secret_id": "secret_id",
        "type": "type",
        "version_id": "version_id",
        "version_stage": "version_stage",
    }

    def __init__(
        self_,
        secret_id: str,
        type: ActionConnectionAWSSecretsManagerType,
        key: Union[str, UnsetType] = unset,
        version_id: Union[str, UnsetType] = unset,
        version_stage: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Reference to a string value in AWS Secrets Manager. The connection must also specify ``external_secrets_manager`` settings. AWS Secrets Manager references are supported for token-based credentials and HTTP authentication tokens on ``DATACENTER`` connections.

        :param key: Top-level JSON key to extract from the secret string. Omit this field to use the entire secret string.
        :type key: str, optional

        :param secret_id: Name or ARN of the AWS Secrets Manager secret.
        :type secret_id: str

        :param type: AWS Secrets Manager secret backend.
        :type type: ActionConnectionAWSSecretsManagerType

        :param version_id: ID of the secret version to retrieve. Cannot be used together with ``version_stage``. If both are omitted, the current version is used.
        :type version_id: str, optional

        :param version_stage: Staging label of the secret version to retrieve. Cannot be used together with ``version_id``. If both are omitted, the current version is used.
        :type version_stage: str, optional
        """
        if key is not unset:
            kwargs["key"] = key
        if version_id is not unset:
            kwargs["version_id"] = version_id
        if version_stage is not unset:
            kwargs["version_stage"] = version_stage
        super().__init__(kwargs)

        self_.secret_id = secret_id
        self_.type = type
