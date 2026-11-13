# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class IssueImpactErrorCounts(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "apm": (int,),
            "llmobs": (int,),
            "logs": (int,),
            "rum": (int,),
        }

    attribute_map = {
        "apm": "apm",
        "llmobs": "llmobs",
        "logs": "logs",
        "rum": "rum",
    }

    def __init__(self_, apm: int, llmobs: int, logs: int, rum: int, **kwargs):
        """
        Number of errors reported by each source. Several sources can report the same error, such as an APM span and
        a log, so the counts overlap: don't add them together.

        :param apm: Number of errors reported by APM.
        :type apm: int

        :param llmobs: Number of errors reported by Agent Observability.
        :type llmobs: int

        :param logs: Number of errors reported by Log Management.
        :type logs: int

        :param rum: Number of errors reported by RUM.
        :type rum: int
        """
        super().__init__(kwargs)

        self_.apm = apm
        self_.llmobs = llmobs
        self_.logs = logs
        self_.rum = rum
