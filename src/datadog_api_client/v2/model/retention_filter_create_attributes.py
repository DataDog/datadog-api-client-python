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
    from datadog_api_client.v2.model.spans_filter_create import SpansFilterCreate
    from datadog_api_client.v2.model.retention_filter_type import RetentionFilterType


class RetentionFilterCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.spans_filter_create import SpansFilterCreate
        from datadog_api_client.v2.model.retention_filter_type import RetentionFilterType

        return {
            "enabled": (bool,),
            "filter": (SpansFilterCreate,),
            "filter_type": (RetentionFilterType,),
            "name": (str,),
            "rate": (float,),
        }

    attribute_map = {
        "enabled": "enabled",
        "filter": "filter",
        "filter_type": "filter_type",
        "name": "name",
        "rate": "rate",
    }

    def __init__(
        self_,
        enabled: bool,
        filter: SpansFilterCreate,
        filter_type: RetentionFilterType,
        name: str,
        rate: float,
        **kwargs,
    ):
        """
        The object describing the configuration of the retention filter to create/update.

        :param enabled: Enable/Disable the retention filter.
        :type enabled: bool

        :param filter: The spans filter. Spans matching this filter will be indexed and stored.
        :type filter: SpansFilterCreate

        :param filter_type: The type of retention filter. The value should always be spans-sampling-processor.
        :type filter_type: RetentionFilterType

        :param name: The name of the retention filter.
        :type name: str

        :param rate: Sample rate to apply to spans going through this retention filter,
            a value of 1.0 keeps all spans matching the query.
        :type rate: float
        """
        super().__init__(kwargs)

        self_.enabled = enabled
        self_.filter = filter
        self_.filter_type = filter_type
        self_.name = name
        self_.rate = rate
