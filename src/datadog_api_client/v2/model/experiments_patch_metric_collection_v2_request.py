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
    from datadog_api_client.v2.model.experiments_patch_metric_collection_v2_request_data import (
        ExperimentsPatchMetricCollectionV2RequestData,
    )


class ExperimentsPatchMetricCollectionV2Request(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_patch_metric_collection_v2_request_data import (
            ExperimentsPatchMetricCollectionV2RequestData,
        )

        return {
            "data": (ExperimentsPatchMetricCollectionV2RequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ExperimentsPatchMetricCollectionV2RequestData, **kwargs):
        """
        Request to update the metric collection.

        :param data: JSON:API resource containing the metric collection identity and fields.
        :type data: ExperimentsPatchMetricCollectionV2RequestData
        """
        super().__init__(kwargs)

        self_.data = data
