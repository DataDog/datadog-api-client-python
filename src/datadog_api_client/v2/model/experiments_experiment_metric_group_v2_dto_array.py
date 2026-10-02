# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.experiments_experiment_metric_group_mutation_v2_data import (
        ExperimentsExperimentMetricGroupMutationV2Data,
    )


class ExperimentsExperimentMetricGroupV2DTOArray(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_experiment_metric_group_mutation_v2_data import (
            ExperimentsExperimentMetricGroupMutationV2Data,
        )

        return {
            "data": ([ExperimentsExperimentMetricGroupMutationV2Data],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[ExperimentsExperimentMetricGroupMutationV2Data], **kwargs):
        """
        Response containing the metric groups for an experiment.

        :param data: Metric groups associated with the experiment.
        :type data: [ExperimentsExperimentMetricGroupMutationV2Data]
        """
        super().__init__(kwargs)

        self_.data = data
