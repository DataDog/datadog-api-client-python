# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.statsig_api_key_type import StatsigAPIKeyType


class StatsigAPIKey(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.statsig_api_key_type import StatsigAPIKeyType

        return {
            "api_key": (str,),
            "type": (StatsigAPIKeyType,),
        }

    attribute_map = {
        "api_key": "api_key",
        "type": "type",
    }

    def __init__(self_, api_key: str, type: StatsigAPIKeyType, **kwargs):
        """
        The definition of the ``StatsigAPIKey`` object.

        :param api_key: The ``StatsigAPIKey`` ``api_key``.
        :type api_key: str

        :param type: The definition of the ``StatsigAPIKey`` object.
        :type type: StatsigAPIKeyType
        """
        super().__init__(kwargs)

        self_.api_key = api_key
        self_.type = type
