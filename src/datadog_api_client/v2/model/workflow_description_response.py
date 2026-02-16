# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class WorkflowDescriptionResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "description": (str,),
            "id": (str,),
            "summary": (str,),
        }

    attribute_map = {
        "description": "description",
        "id": "id",
        "summary": "summary",
    }

    def __init__(self_, description: str, id: str, summary: str, **kwargs):
        """


        :param description: The generated workflow description.
        :type description: str

        :param id: The generation ID.
        :type id: str

        :param summary: A brief summary of the workflow.
        :type summary: str
        """
        super().__init__(kwargs)

        self_.description = description
        self_.id = id
        self_.summary = summary
