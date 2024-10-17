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
    from datadog_api_client.v2.model.aws_lambda_forwarder_config import AWSLambdaForwarderConfig


class AWSLogsConfig(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aws_lambda_forwarder_config import AWSLambdaForwarderConfig

        return {
            "lambda_forwarder": (AWSLambdaForwarderConfig,),
        }

    attribute_map = {
        "lambda_forwarder": "lambda_forwarder",
    }

    def __init__(self_, lambda_forwarder: Union[AWSLambdaForwarderConfig, UnsetType] = unset, **kwargs):
        """
        AWS Logs config

        :param lambda_forwarder: AWS Lambda forwarder
        :type lambda_forwarder: AWSLambdaForwarderConfig, optional
        """
        if lambda_forwarder is not unset:
            kwargs["lambda_forwarder"] = lambda_forwarder
        super().__init__(kwargs)
