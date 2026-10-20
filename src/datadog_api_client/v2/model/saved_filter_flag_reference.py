# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


class SavedFilterFlagReference(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "id": (UUID,),
            "name": (str,),
        }

    attribute_map = {
        "id": "id",
        "name": "name",
    }

    def __init__(self_, id: UUID, name: str, **kwargs):
        """
        A feature flag that references the saved filter.

        :param id: The ID of the feature flag.
        :type id: UUID

        :param name: The name of the feature flag.
        :type name: str
        """
        super().__init__(kwargs)

        self_.id = id
        self_.name = name
