# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.deployment import Deployment


class PublishAppResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.deployment import Deployment

        return {
            "data": (Deployment,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[Deployment, UnsetType] = unset, **kwargs):
        """
        The response object after an app is successfully published.

        :param data: The version of the app that was published.
        :type data: Deployment, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
