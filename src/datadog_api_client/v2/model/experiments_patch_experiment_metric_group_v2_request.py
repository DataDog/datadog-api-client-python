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
    from datadog_api_client.v2.model.experiments_patch_experiment_metric_group_v2_request_data import (
        ExperimentsPatchExperimentMetricGroupV2RequestData,
    )


class ExperimentsPatchExperimentMetricGroupV2Request(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_patch_experiment_metric_group_v2_request_data import (
            ExperimentsPatchExperimentMetricGroupV2RequestData,
        )

        return {
            "data": (ExperimentsPatchExperimentMetricGroupV2RequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ExperimentsPatchExperimentMetricGroupV2RequestData, **kwargs):
        """
        Request to update the experiment metric group.

        :param data: JSON:API resource containing the experiment metric group identity and fields.
        :type data: ExperimentsPatchExperimentMetricGroupV2RequestData
        """
        super().__init__(kwargs)

        self_.data = data
