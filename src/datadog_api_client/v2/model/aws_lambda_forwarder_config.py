# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class AWSLambdaForwarderConfig(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "lambdas": ([str],),
            "sources": ([str],),
        }

    attribute_map = {
        "lambdas": "lambdas",
        "sources": "sources",
    }

    def __init__(
        self_, lambdas: Union[List[str], UnsetType] = unset, sources: Union[List[str], UnsetType] = unset, **kwargs
    ):
        """
        Log Autosubscription configuration for Datadog Forwarder Lambda functions. Automatically set up triggers for existing
        and new logs for some services, ensuring no logs from new resources are missed and saving time spent on manual configuration.

        :param lambdas: List of Datadog Lambda Log Forwarder ARNs in your AWS account. Defaults to ``[]``.
        :type lambdas: [str], optional

        :param sources: List of service IDs set to enable automatic log collection. Discover the list of available services with the
            `Get list of AWS log ready services <https://docs.datadoghq.com/api/latest/aws-logs-integration/#get-list-of-aws-log-ready-services>`_ endpoint.
        :type sources: [str], optional
        """
        if lambdas is not unset:
            kwargs["lambdas"] = lambdas
        if sources is not unset:
            kwargs["sources"] = sources
        super().__init__(kwargs)
