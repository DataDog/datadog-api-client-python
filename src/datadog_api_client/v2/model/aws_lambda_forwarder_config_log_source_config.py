# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.aws_log_source_tag_filter import AWSLogSourceTagFilter


class AWSLambdaForwarderConfigLogSourceConfig(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aws_log_source_tag_filter import AWSLogSourceTagFilter

        return {
            "tag_filters": ([AWSLogSourceTagFilter],),
        }

    attribute_map = {
        "tag_filters": "tag_filters",
    }

    def __init__(self_, tag_filters: Union[List[AWSLogSourceTagFilter], UnsetType] = unset, **kwargs):
        """
        Log source configuration.

        :param tag_filters: List of AWS log source tag filters. Defaults to ``[]``.
        :type tag_filters: [AWSLogSourceTagFilter], optional
        """
        if tag_filters is not unset:
            kwargs["tag_filters"] = tag_filters
        super().__init__(kwargs)
