# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class UpdateAppFavoriteRequestDataAttributes(ModelNormal):
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
        Attributes for updating an app's favorite status.

        :param favorite: Whether the app should be marked as a favorite for the current user.
        :type favorite: bool
        """
        super().__init__(kwargs)

        self_.favorite = favorite
