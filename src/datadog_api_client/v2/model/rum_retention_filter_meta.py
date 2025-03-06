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
    from datadog_api_client.v2.model.rum_retention_filter_source import RumRetentionFilterSource


class RumRetentionFilterMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_retention_filter_source import RumRetentionFilterSource

        return {
            "source": (RumRetentionFilterSource,),
        }

    attribute_map = {
        "source": "source",
    }

    def __init__(self_, source: Union[RumRetentionFilterSource, UnsetType] = unset, **kwargs):
        """
        The object describing metadata of a RUM retention filter.

        :param source: The type of RUM events to filter on.
        :type source: RumRetentionFilterSource, optional
        """
        if source is not unset:
            kwargs["source"] = source
        super().__init__(kwargs)
