# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ActionMatch(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "action_fqn": (str,),
            "description": (str,),
            "score": (float,),
        }

    attribute_map = {
        "action_fqn": "actionFqn",
        "description": "description",
        "score": "score",
    }

    def __init__(self_, action_fqn: str, description: str, score: float, **kwargs):
        """


        :param action_fqn: The fully qualified name of the action.
        :type action_fqn: str

        :param description: The description of the action.
        :type description: str

        :param score: The relevance score of the match.
        :type score: float
        """
        super().__init__(kwargs)

        self_.action_fqn = action_fqn
        self_.description = description
        self_.score = score
