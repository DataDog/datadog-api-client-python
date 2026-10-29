# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


class FeatureFlagChangeEventFlag(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "id": (UUID,),
            "key": (str,),
            "name": (str,),
        }

    attribute_map = {
        "id": "id",
        "key": "key",
        "name": "name",
    }

    def __init__(self_, id: UUID, key: str, name: str, **kwargs):
        """
        The feature flag the change applies to.

        :param id: The ID of the feature flag.
        :type id: UUID

        :param key: The key of the feature flag.
        :type key: str

        :param name: The name of the feature flag.
        :type name: str
        """
        super().__init__(kwargs)

        self_.id = id
        self_.key = key
        self_.name = name
