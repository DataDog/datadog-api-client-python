# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class InvestigationConclusion(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "description": (str,),
            "summary": (str,),
            "title": (str,),
        }

    attribute_map = {
        "description": "description",
        "summary": "summary",
        "title": "title",
    }

    def __init__(self_, description: str, summary: str, title: str, **kwargs):
        """
        A full explanation of the finding, including root cause analysis and supporting evidence.

        :param description: A full explanation of the finding, including root cause analysis and supporting evidence.
        :type description: str

        :param summary: A summary of the finding, including affected components and timeframe.
        :type summary: str

        :param title: The title of the conclusion.
        :type title: str
        """
        super().__init__(kwargs)

        self_.description = description
        self_.summary = summary
        self_.title = title
