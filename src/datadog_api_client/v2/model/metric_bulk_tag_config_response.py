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
    from datadog_api_client.v2.model.metric_bulk_tag_config_status import MetricBulkTagConfigStatus
    from datadog_api_client.v2.model.metric_bulk_tag_config_email_list import MetricBulkTagConfigEmailList
    from datadog_api_client.v2.model.metric_bulk_tag_config_tag_name_list import MetricBulkTagConfigTagNameList


@dataclass
class MetricBulkTagConfigResponseJSON:
    id: str
    emails: Union[MetricBulkTagConfigEmailList, UnsetType] = unset
    status: Union[str, UnsetType] = unset
    tags: Union[MetricBulkTagConfigTagNameList, UnsetType] = unset


class MetricBulkTagConfigResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.metric_bulk_tag_config_status import MetricBulkTagConfigStatus

        return {
            "data": (MetricBulkTagConfigStatus,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = MetricBulkTagConfigResponseJSON

    def __init__(self_, data: Union[MetricBulkTagConfigStatus, UnsetType] = unset, **kwargs):
        """
        Wrapper for a single bulk tag configuration status response.

        :param data: The status of a request to bulk configure metric tags.
            It contains the fields from the original request for reference.
        :type data: MetricBulkTagConfigStatus, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
