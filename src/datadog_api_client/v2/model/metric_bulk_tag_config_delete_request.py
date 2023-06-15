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


from datadog_api_client.v2.model.metric_bulk_tag_config_email_list import MetricBulkTagConfigEmailList
from datadog_api_client.v2.model.metric_bulk_tag_config_email_list import MetricBulkTagConfigEmailList

if TYPE_CHECKING:
    from datadog_api_client.v2.model.metric_bulk_tag_config_delete import MetricBulkTagConfigDelete


@dataclass
class MetricBulkTagConfigDeleteRequestJSON:
    id: str
    emails: Union[MetricBulkTagConfigEmailList, UnsetType] = unset


class MetricBulkTagConfigDeleteRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.metric_bulk_tag_config_delete import MetricBulkTagConfigDelete

        return {
            "data": (MetricBulkTagConfigDelete,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = MetricBulkTagConfigDeleteRequestJSON

    def __init__(self_, data: MetricBulkTagConfigDelete, **kwargs):
        """
        Wrapper object for a single bulk tag deletion request.

        :param data: Request object to bulk delete all tag configurations for metrics matching the given prefix.
        :type data: MetricBulkTagConfigDelete
        """
        super().__init__(kwargs)

        self_.data = data
