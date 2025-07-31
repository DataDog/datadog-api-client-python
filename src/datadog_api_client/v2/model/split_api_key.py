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
    from datadog_api_client.v2.model.split_api_key_type import SplitAPIKeyType


class SplitAPIKey(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.split_api_key_type import SplitAPIKeyType

        return {
            "api_key": (str,),
            "type": (SplitAPIKeyType,),
        }

    attribute_map = {
        "api_key": "api_key",
        "type": "type",
    }

    def __init__(self_, api_key: str, type: SplitAPIKeyType, **kwargs):
        """
        The definition of the ``SplitAPIKey`` object.

        :param api_key: The ``SplitAPIKey`` ``api_key``.
        :type api_key: str

        :param type: The definition of the ``SplitAPIKey`` object.
        :type type: SplitAPIKeyType
        """
        super().__init__(kwargs)

        self_.api_key = api_key
        self_.type = type
