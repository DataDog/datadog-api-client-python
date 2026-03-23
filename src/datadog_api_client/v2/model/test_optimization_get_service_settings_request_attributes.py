# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class TestOptimizationGetServiceSettingsRequestAttributes(ModelNormal):
    validations = {
        "repository_id": {
            "min_length": 1,
        },
        "service_name": {
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "env": (str,),
            "repository_id": (str,),
            "service_name": (str,),
        }

    attribute_map = {
        "env": "env",
        "repository_id": "repository_id",
        "service_name": "service_name",
    }

    def __init__(self_, repository_id: str, service_name: str, env: Union[str, UnsetType] = unset, **kwargs):
        """
        Attributes for requesting Test Optimization service settings.

        :param env: The environment name. If omitted, defaults to ``none``.
        :type env: str, optional

        :param repository_id: The repository identifier.
        :type repository_id: str

        :param service_name: The service name.
        :type service_name: str
        """
        if env is not unset:
            kwargs["env"] = env
        super().__init__(kwargs)

        self_.repository_id = repository_id
        self_.service_name = service_name
