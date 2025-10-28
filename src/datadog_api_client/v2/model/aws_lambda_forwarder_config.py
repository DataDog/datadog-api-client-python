# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.aws_lambda_forwarder_config_log_source_config import (
        AWSLambdaForwarderConfigLogSourceConfig,
    )


class AWSLambdaForwarderConfig(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aws_lambda_forwarder_config_log_source_config import (
            AWSLambdaForwarderConfigLogSourceConfig,
        )

        return {
            "lambdas": ([str],),
            "log_source_config": (AWSLambdaForwarderConfigLogSourceConfig,),
            "sources": ([str],),
        }

    attribute_map = {
        "lambdas": "lambdas",
        "log_source_config": "log_source_config",
        "sources": "sources",
    }

    def __init__(
        self_,
        lambdas: Union[List[str], UnsetType] = unset,
        log_source_config: Union[AWSLambdaForwarderConfigLogSourceConfig, UnsetType] = unset,
        sources: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Log Autosubscription configuration for Datadog Forwarder Lambda functions.
        Automatically set up triggers for existing and new logs for some services,
        ensuring no logs from new resources are missed and saving time spent on manual configuration.

        :param lambdas: List of Datadog Lambda Log Forwarder ARNs in your AWS account. Defaults to ``[]``.
        :type lambdas: [str], optional

        :param log_source_config: Log source configuration.
        :type log_source_config: AWSLambdaForwarderConfigLogSourceConfig, optional

        :param sources: List of service IDs set to enable automatic log collection.
            Discover the list of available services with the
            `Get list of AWS log ready services <https://docs.datadoghq.com/api/latest/aws-logs-integration/#get-list-of-aws-log-ready-services>`_
            endpoint.
        :type sources: [str], optional
        """
        if lambdas is not unset:
            kwargs["lambdas"] = lambdas
        if log_source_config is not unset:
            kwargs["log_source_config"] = log_source_config
        if sources is not unset:
            kwargs["sources"] = sources
        super().__init__(kwargs)
