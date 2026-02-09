# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


class WorkflowHeadlessExecutionConnection(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "connection_id": (UUID,),
            "label": (str,),
        }

    attribute_map = {
        "connection_id": "connection_id",
        "label": "label",
    }

    def __init__(self_, connection_id: UUID, label: str, **kwargs):
        """


        :param connection_id: The ID of the connection
        :type connection_id: UUID

        :param label: The label for the connection
        :type label: str
        """
        super().__init__(kwargs)

        self_.connection_id = connection_id
        self_.label = label
