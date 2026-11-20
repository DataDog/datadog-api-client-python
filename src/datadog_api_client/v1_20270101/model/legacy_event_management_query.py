# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.tags_execution import TagsExecution


class LegacyEventManagementQuery(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.tags_execution import TagsExecution

        return {
            "search": (str,),
            "tags_execution": (TagsExecution,),
        }

    attribute_map = {
        "search": "search",
        "tags_execution": "tags_execution",
    }

    def __init__(self_, search: str, tags_execution: TagsExecution, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param search: Test-only generated schema for the dashboard versioning proof of concept.
        :type search: str

        :param tags_execution: Test-only generated schema for the dashboard versioning proof of concept.
        :type tags_execution: TagsExecution
        """
        super().__init__(kwargs)

        self_.search = search
        self_.tags_execution = tags_execution
