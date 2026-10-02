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
    from datadog_api_client.v2.model.experiments_create_experiment_metric_group_v2_request_data_attributes import (
        ExperimentsCreateExperimentMetricGroupV2RequestDataAttributes,
    )
    from datadog_api_client.v2.model.experiments_patch_experiment_metric_group_v2_request_data_type import (
        ExperimentsPatchExperimentMetricGroupV2RequestDataType,
    )


class ExperimentsCreateExperimentMetricGroupV2RequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_create_experiment_metric_group_v2_request_data_attributes import (
            ExperimentsCreateExperimentMetricGroupV2RequestDataAttributes,
        )
        from datadog_api_client.v2.model.experiments_patch_experiment_metric_group_v2_request_data_type import (
            ExperimentsPatchExperimentMetricGroupV2RequestDataType,
        )

        return {
            "attributes": (ExperimentsCreateExperimentMetricGroupV2RequestDataAttributes,),
            "id": (str,),
            "type": (ExperimentsPatchExperimentMetricGroupV2RequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: ExperimentsCreateExperimentMetricGroupV2RequestDataAttributes,
        type: ExperimentsPatchExperimentMetricGroupV2RequestDataType,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Metric group resource to create on the experiment.

        :param attributes: Name and metric selection for the new experiment metric group.
        :type attributes: ExperimentsCreateExperimentMetricGroupV2RequestDataAttributes

        :param id: Optional JSON:API resource identifier field.
        :type id: str, optional

        :param type: Experiment metric groups resource type.
        :type type: ExperimentsPatchExperimentMetricGroupV2RequestDataType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
