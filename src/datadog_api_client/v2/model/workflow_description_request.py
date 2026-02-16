# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class WorkflowDescriptionRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "name": (str,),
            "spec": (dict,),
        }

    attribute_map = {
        "name": "name",
        "spec": "spec",
    }

    def __init__(self_, name: str, spec: dict, **kwargs):
        """


        :param name: The name of the workflow.
        :type name: str

        :param spec: The workflow specification as a JSON object.
        :type spec: dict
        """
        super().__init__(kwargs)

        self_.name = name
        self_.spec = spec
