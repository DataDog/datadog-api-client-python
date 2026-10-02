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
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.experiments_patch_experiment_metric_group_v2_request_data_attributes import (
        ExperimentsPatchExperimentMetricGroupV2RequestDataAttributes,
    )
    from datadog_api_client.v2.model.experiments_patch_experiment_metric_group_v2_request_data_type import (
        ExperimentsPatchExperimentMetricGroupV2RequestDataType,
    )


class ExperimentsPatchExperimentMetricGroupV2RequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_patch_experiment_metric_group_v2_request_data_attributes import (
            ExperimentsPatchExperimentMetricGroupV2RequestDataAttributes,
        )
        from datadog_api_client.v2.model.experiments_patch_experiment_metric_group_v2_request_data_type import (
            ExperimentsPatchExperimentMetricGroupV2RequestDataType,
        )

        return {
            "attributes": (ExperimentsPatchExperimentMetricGroupV2RequestDataAttributes,),
            "id": (UUID,),
            "type": (ExperimentsPatchExperimentMetricGroupV2RequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        type: ExperimentsPatchExperimentMetricGroupV2RequestDataType,
        attributes: Union[ExperimentsPatchExperimentMetricGroupV2RequestDataAttributes, UnsetType] = unset,
        id: Union[UUID, UnsetType] = unset,
        **kwargs,
    ):
        """
        JSON:API resource containing the experiment metric group identity and fields.

        :param attributes: Fields supplied to update the experiment metric group.
        :type attributes: ExperimentsPatchExperimentMetricGroupV2RequestDataAttributes, optional

        :param id: ID of the experiment metric group.
        :type id: UUID, optional

        :param type: Experiment metric groups resource type.
        :type type: ExperimentsPatchExperimentMetricGroupV2RequestDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
