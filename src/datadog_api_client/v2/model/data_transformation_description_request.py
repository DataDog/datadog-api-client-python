# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class DataTransformationDescriptionRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "action_id": (str,),
            "script": (str,),
        }

    attribute_map = {
        "action_id": "actionId",
        "script": "script",
    }

    def __init__(self_, action_id: str, script: str, **kwargs):
        """


        :param action_id: The fully qualified name (FQN) of the action.
        :type action_id: str

        :param script: The transformation script to describe.
        :type script: str
        """
        super().__init__(kwargs)

        self_.action_id = action_id
        self_.script = script
