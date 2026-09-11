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


class SnowflakeCloudCostMetricsIntegrationDataflowSettingsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "query_tags": (str,),
        }

    attribute_map = {
        "query_tags": "query_tags",
    }

    def __init__(self_, query_tags: Union[str, UnsetType] = unset, **kwargs):
        """
        Settings of the Cloud Cost Management dataflow.

        :param query_tags: Snowflake query tags ingested so that cost data can be broken down by them in Cloud Cost Management, as a comma-separated list of tag names.
        :type query_tags: str, optional
        """
        if query_tags is not unset:
            kwargs["query_tags"] = query_tags
        super().__init__(kwargs)
