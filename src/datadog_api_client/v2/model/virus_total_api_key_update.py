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
    from datadog_api_client.v2.model.virus_total_api_key_type import VirusTotalAPIKeyType


class VirusTotalAPIKeyUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.virus_total_api_key_type import VirusTotalAPIKeyType

        return {
            "api_key": (str,),
            "type": (VirusTotalAPIKeyType,),
        }

    attribute_map = {
        "api_key": "api_key",
        "type": "type",
    }

    def __init__(self_, type: VirusTotalAPIKeyType, api_key: Union[str, UnsetType] = unset, **kwargs):
        """
        The definition of the ``VirusTotalAPIKey`` object.

        :param api_key: The ``VirusTotalAPIKeyUpdate`` ``api_key``.
        :type api_key: str, optional

        :param type: The definition of the ``VirusTotalAPIKey`` object.
        :type type: VirusTotalAPIKeyType
        """
        if api_key is not unset:
            kwargs["api_key"] = api_key
        super().__init__(kwargs)

        self_.type = type
