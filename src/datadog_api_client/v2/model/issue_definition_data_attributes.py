# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class IssueDefinitionDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "category": (str,),
            "label": (str,),
            "level": (str,),
        }

    attribute_map = {
        "category": "category",
        "label": "label",
        "level": "level",
    }

    def __init__(self_, category: str, label: str, level: str, **kwargs):
        """
        Attributes of a single End User Device Monitoring issue definition.

        :param category: Category of the issue (for example, ``battery`` , ``network`` , or ``performance`` ).
        :type category: str

        :param label: Human-readable label describing the issue, suitable for display in the Datadog UI.
        :type label: str

        :param level: Severity level of the issue (for example, ``warning`` or ``critical`` ).
        :type level: str
        """
        super().__init__(kwargs)

        self_.category = category
        self_.label = label
        self_.level = level
