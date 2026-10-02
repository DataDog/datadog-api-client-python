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
    from datadog_api_client.v2.model.experiments_experiment_metric_group_v2_dto_data_attributes import (
        ExperimentsExperimentMetricGroupV2DTODataAttributes,
    )
    from datadog_api_client.v2.model.experiments_patch_experiment_metric_group_v2_request_data_type import (
        ExperimentsPatchExperimentMetricGroupV2RequestDataType,
    )


class ExperimentsExperimentMetricGroupMutationV2Data(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_experiment_metric_group_v2_dto_data_attributes import (
            ExperimentsExperimentMetricGroupV2DTODataAttributes,
        )
        from datadog_api_client.v2.model.experiments_patch_experiment_metric_group_v2_request_data_type import (
            ExperimentsPatchExperimentMetricGroupV2RequestDataType,
        )

        return {
            "attributes": (ExperimentsExperimentMetricGroupV2DTODataAttributes,),
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
        id: UUID,
        type: ExperimentsPatchExperimentMetricGroupV2RequestDataType,
        attributes: Union[ExperimentsExperimentMetricGroupV2DTODataAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        Experiment metric group resource with its identifier and metric selection.

        :param attributes: Name, purpose, and selected metrics of an experiment metric group.
        :type attributes: ExperimentsExperimentMetricGroupV2DTODataAttributes, optional

        :param id: Identifier of the experiment metric group.
        :type id: UUID

        :param type: Experiment metric groups resource type.
        :type type: ExperimentsPatchExperimentMetricGroupV2RequestDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
