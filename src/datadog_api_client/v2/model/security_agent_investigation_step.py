# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SecurityAgentInvestigationStep(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "name": (str,),
            "summary": (str,),
        }

    attribute_map = {
        "name": "name",
        "summary": "summary",
    }

    def __init__(self_, name: str, summary: str, **kwargs):
        """
        A step of the investigation.

        :param name: Name of the step, usually the question it answers.
        :type name: str

        :param summary: Summary of what the step found. It can be empty.
        :type summary: str
        """
        super().__init__(kwargs)

        self_.name = name
        self_.summary = summary
