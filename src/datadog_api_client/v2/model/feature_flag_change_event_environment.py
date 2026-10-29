# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


class FeatureFlagChangeEventEnvironment(ModelNormal):
    _nullable = True

    @cached_property
    def openapi_types(_):
        return {
            "id": (UUID,),
            "is_production": (bool,),
            "name": (str,),
        }

    attribute_map = {
        "id": "id",
        "is_production": "is_production",
        "name": "name",
    }

    def __init__(self_, id: UUID, is_production: bool, name: str, **kwargs):
        """
        The environment the change applies to. Null for a change to the flag itself rather than to one environment.

        :param id: The ID of the environment.
        :type id: UUID

        :param is_production: Whether the environment is a production environment.
        :type is_production: bool

        :param name: The name of the environment.
        :type name: str
        """
        super().__init__(kwargs)

        self_.id = id
        self_.is_production = is_production
        self_.name = name
