# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ObservabilityPipelineAddEnvVarsProcessorVariable(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "field": (str,),
            "name": (str,),
        }

    attribute_map = {
        "field": "field",
        "name": "name",
    }

    def __init__(self_, field: str, name: str, **kwargs):
        """
        Defines a mapping between an environment variable and a log field.

        :param field: The target field in the log event.
        :type field: str

        :param name: The name of the environment variable to read.
        :type name: str
        """
        super().__init__(kwargs)

        self_.field = field
        self_.name = name
