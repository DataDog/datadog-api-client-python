# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class IntegrationAssignmentDataAttributesRequestAssignment(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "jira": ({str: ([str],)},),
        }

    attribute_map = {
        "jira": "jira",
    }

    def __init__(self_, jira: Dict[str, List[str]], **kwargs):
        """


        :param jira: Map of Jira issue URLs to lists of finding IDs.
        :type jira: {str: ([str],)}
        """
        super().__init__(kwargs)

        self_.jira = jira
