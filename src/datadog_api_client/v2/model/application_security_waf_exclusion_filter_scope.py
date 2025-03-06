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


class ApplicationSecurityWafExclusionFilterScope(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "env": (str,),
            "service": (str,),
        }

    attribute_map = {
        "env": "env",
        "service": "service",
    }

    def __init__(self_, env: Union[str, UnsetType] = unset, service: Union[str, UnsetType] = unset, **kwargs):
        """
        Deploy on services based on their environment and/or service name.

        :param env: Deploy on this environment.
        :type env: str, optional

        :param service: Deploy on this service.
        :type service: str, optional
        """
        if env is not unset:
            kwargs["env"] = env
        if service is not unset:
            kwargs["service"] = service
        super().__init__(kwargs)
