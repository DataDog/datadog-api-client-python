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
    from datadog_api_client.v2.model.experiments_cancel_experiment_v2_request_data import (
        ExperimentsCancelExperimentV2RequestData,
    )


class ExperimentsCancelExperimentV2Request(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_cancel_experiment_v2_request_data import (
            ExperimentsCancelExperimentV2RequestData,
        )

        return {
            "data": (ExperimentsCancelExperimentV2RequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ExperimentsCancelExperimentV2RequestData, **kwargs):
        """
        Request to cancel an experiment and record a reason.

        :param data: Experiment cancellation resource with the experiment identifier and reason.
        :type data: ExperimentsCancelExperimentV2RequestData
        """
        super().__init__(kwargs)

        self_.data = data
