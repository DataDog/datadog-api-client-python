# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ObservabilityPipelineRenameMetricTagsProcessorTag(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "rename_to": (str,),
            "tag": (str,),
        }

    attribute_map = {
        "rename_to": "rename_to",
        "tag": "tag",
    }

    def __init__(self_, rename_to: str, tag: str, **kwargs):
        """
        Defines how to rename a tag on metric events.

        :param rename_to: The new tag key to assign in place of the original.
        :type rename_to: str

        :param tag: The original tag key on the metric event.
        :type tag: str
        """
        super().__init__(kwargs)

        self_.rename_to = rename_to
        self_.tag = tag
