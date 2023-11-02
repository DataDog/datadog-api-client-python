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
    from datadog_api_client.v2.model.metric_bulk_tag_config_email_list import MetricBulkTagConfigEmailList
    from datadog_api_client.v2.model.metric_bulk_tag_config_tag_name_list import MetricBulkTagConfigTagNameList


class MetricBulkTagConfigCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.metric_bulk_tag_config_email_list import MetricBulkTagConfigEmailList
        from datadog_api_client.v2.model.metric_bulk_tag_config_tag_name_list import MetricBulkTagConfigTagNameList

        return {
            "emails": (MetricBulkTagConfigEmailList,),
            "exclude_tags_mode": (bool,),
            "tags": (MetricBulkTagConfigTagNameList,),
        }

    attribute_map = {
        "emails": "emails",
        "exclude_tags_mode": "exclude_tags_mode",
        "tags": "tags",
    }

    def __init__(
        self_,
        emails: Union[MetricBulkTagConfigEmailList, UnsetType] = unset,
        exclude_tags_mode: Union[bool, UnsetType] = unset,
        tags: Union[MetricBulkTagConfigTagNameList, UnsetType] = unset,
        **kwargs,
    ):
        """
        Optional parameters for bulk creating metric tag configurations.

        :param emails: A list of account emails to notify when the configuration is applied.
        :type emails: MetricBulkTagConfigEmailList, optional

        :param exclude_tags_mode: When set to true, the configuration will exclude the configured tags and include any other submitted tags.
            When set to false, the configuration will include the configured tags and exclude any other submitted tags.
            Defaults to false.
        :type exclude_tags_mode: bool, optional

        :param tags: A list of tag names to apply to the configuration.
        :type tags: MetricBulkTagConfigTagNameList, optional
        """
        if emails is not unset:
            kwargs["emails"] = emails
        if exclude_tags_mode is not unset:
            kwargs["exclude_tags_mode"] = exclude_tags_mode
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)
