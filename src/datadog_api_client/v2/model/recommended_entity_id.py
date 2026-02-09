# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class RecommendedEntityID(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "id": (str,),
        }

    attribute_map = {
        "id": "id",
    }

    def __init__(self_, id: str, **kwargs):
        """
        A recommended entity identifier.

        :param id: Unique identifier for the recommended entity.
        :type id: str
        """
        super().__init__(kwargs)

        self_.id = id
