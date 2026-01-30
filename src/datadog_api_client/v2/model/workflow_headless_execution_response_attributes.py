# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


class WorkflowHeadlessExecutionResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "instance_id": (UUID,),
        }

    attribute_map = {
        "instance_id": "instance_id",
    }

    def __init__(self_, instance_id: UUID, **kwargs):
        """


        :param instance_id: The ID of the workflow instance that was created
        :type instance_id: UUID
        """
        super().__init__(kwargs)

        self_.instance_id = instance_id
