# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class WorkflowFavoriteRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "favorite": (bool,),
        }

    attribute_map = {
        "favorite": "favorite",
    }

    def __init__(self_, favorite: bool, **kwargs):
        """


        :param favorite: Whether to mark the workflow as favorite (true) or unfavorite (false)
        :type favorite: bool
        """
        super().__init__(kwargs)

        self_.favorite = favorite
