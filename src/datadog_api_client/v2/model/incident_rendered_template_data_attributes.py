# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class IncidentRenderedTemplateDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "rendered_content": (str,),
        }

    attribute_map = {
        "rendered_content": "rendered_content",
    }

    def __init__(self_, rendered_content: str, **kwargs):
        """
        Attributes of a rendered template.

        :param rendered_content: The rendered template content.
        :type rendered_content: str
        """
        super().__init__(kwargs)

        self_.rendered_content = rendered_content
