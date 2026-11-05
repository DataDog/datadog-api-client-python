# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ActionConnectionAWSSecretsManagerType(ModelSimple):
    """
    AWS Secrets Manager secret backend.

    :param value: If omitted defaults to "aws_secrets_manager". Must be one of ["aws_secrets_manager"].
    :type value: str
    """

    allowed_values = {
        "aws_secrets_manager",
    }
    AWS_SECRETS_MANAGER: ClassVar["ActionConnectionAWSSecretsManagerType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ActionConnectionAWSSecretsManagerType.AWS_SECRETS_MANAGER = ActionConnectionAWSSecretsManagerType("aws_secrets_manager")
