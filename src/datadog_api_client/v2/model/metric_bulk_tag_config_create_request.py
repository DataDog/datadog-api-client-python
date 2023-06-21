# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.metric_bulk_tag_config_create import MetricBulkTagConfigCreate
    from datadog_api_client.v2.model.metric_bulk_tag_config_email_list import MetricBulkTagConfigEmailList
    from datadog_api_client.v2.model.metric_bulk_tag_config_tag_name_list import MetricBulkTagConfigTagNameList


@dataclass
class MetricBulkTagConfigCreateRequestJSON:
    id: str
    emails: Union[MetricBulkTagConfigEmailList, UnsetType] = unset
    tags: Union[MetricBulkTagConfigTagNameList, UnsetType] = unset


class MetricBulkTagConfigCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.metric_bulk_tag_config_create import MetricBulkTagConfigCreate

        return {
            "data": (MetricBulkTagConfigCreate,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = MetricBulkTagConfigCreateRequestJSON

    def __init__(self_, data: MetricBulkTagConfigCreate, **kwargs):
        """
        Wrapper object for a single bulk tag configuration request.

        :param data: Request object to bulk configure tags for metrics matching the given prefix.
        :type data: MetricBulkTagConfigCreate
        """
        super().__init__(kwargs)

        self_.data = data
