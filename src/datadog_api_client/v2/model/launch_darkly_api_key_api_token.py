# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class LaunchDarklyAPIKeyApiToken(ModelComposed):
    def __init__(self, **kwargs):
        """
        The ``LaunchDarklyAPIKey`` ``api_token``.

        :param key: Top-level JSON key to extract from the secret string. Omit this field to use the entire secret string.
        :type key: str, optional

        :param secret_id: Name or ARN of the AWS Secrets Manager secret.
        :type secret_id: str

        :param type: AWS Secrets Manager secret backend.
        :type type: ActionConnectionAWSSecretsManagerType

        :param version_id: ID of the secret version to retrieve. Cannot be used together with `version_stage`. If both are omitted, the current version is used.
        :type version_id: str, optional

        :param version_stage: Staging label of the secret version to retrieve. Cannot be used together with `version_id`. If both are omitted, the current version is used.
        :type version_stage: str, optional
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v2.model.action_connection_aws_secrets_manager_reference import (
            ActionConnectionAWSSecretsManagerReference,
        )

        return {
            "oneOf": [
                str,
                ActionConnectionAWSSecretsManagerReference,
            ],
        }
