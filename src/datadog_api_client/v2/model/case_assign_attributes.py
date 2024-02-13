# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class CaseAssignAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "assignee_id": (str,),
        }

    attribute_map = {
        "assignee_id": "assignee_id",
    }

    def __init__(self_, assignee_id: str, **kwargs):
        """
        Case assign attributes

        :param assignee_id: Assignee's UUID
        :type assignee_id: str
        """
        super().__init__(kwargs)

        self_.assignee_id = assignee_id
