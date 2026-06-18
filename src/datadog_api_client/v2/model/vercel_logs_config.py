# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.vercel_environment import VercelEnvironment
    from datadog_api_client.v2.model.vercel_log_source import VercelLogSource


class VercelLogsConfig(ModelNormal):
    validations = {
        "sampling_percentage": {
            "inclusive_maximum": 100,
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.vercel_environment import VercelEnvironment
        from datadog_api_client.v2.model.vercel_log_source import VercelLogSource

        return {
            "enabled": (bool,),
            "environments": ([VercelEnvironment],),
            "log_sources": ([VercelLogSource],),
            "sampling_percentage": (int,),
        }

    attribute_map = {
        "enabled": "enabled",
        "environments": "environments",
        "log_sources": "logSources",
        "sampling_percentage": "samplingPercentage",
    }

    def __init__(
        self_,
        enabled: bool,
        environments: List[VercelEnvironment],
        log_sources: List[VercelLogSource],
        sampling_percentage: int,
        **kwargs,
    ):
        """
        Logs forwarding configuration for the Vercel integration.

        :param enabled: Whether logs forwarding is enabled.
        :type enabled: bool

        :param environments: List of Vercel deployment environments to forward telemetry from.
        :type environments: [VercelEnvironment]

        :param log_sources: List of Vercel log sources to forward to Datadog.
        :type log_sources: [VercelLogSource]

        :param sampling_percentage: Percentage of logs to forward to Datadog, between 0 and 100.
        :type sampling_percentage: int
        """
        super().__init__(kwargs)

        self_.enabled = enabled
        self_.environments = environments
        self_.log_sources = log_sources
        self_.sampling_percentage = sampling_percentage
