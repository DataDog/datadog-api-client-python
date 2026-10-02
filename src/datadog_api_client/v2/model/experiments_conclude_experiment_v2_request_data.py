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
    from datadog_api_client.v2.model.experiments_conclude_experiment_v2_request_data_attributes import (
        ExperimentsConcludeExperimentV2RequestDataAttributes,
    )
    from datadog_api_client.v2.model.experiments_conclude_experiment_v2_request_data_type import (
        ExperimentsConcludeExperimentV2RequestDataType,
    )


class ExperimentsConcludeExperimentV2RequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_conclude_experiment_v2_request_data_attributes import (
            ExperimentsConcludeExperimentV2RequestDataAttributes,
        )
        from datadog_api_client.v2.model.experiments_conclude_experiment_v2_request_data_type import (
            ExperimentsConcludeExperimentV2RequestDataType,
        )

        return {
            "attributes": (ExperimentsConcludeExperimentV2RequestDataAttributes,),
            "id": (str,),
            "type": (ExperimentsConcludeExperimentV2RequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: ExperimentsConcludeExperimentV2RequestDataAttributes,
        type: ExperimentsConcludeExperimentV2RequestDataType,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Experiment conclusion resource with the experiment identifier and decision.

        :param attributes: Decision to record when concluding the experiment.
        :type attributes: ExperimentsConcludeExperimentV2RequestDataAttributes

        :param id: Identifier of the experiment to conclude.
        :type id: str, optional

        :param type: Conclude experiment request resource type.
        :type type: ExperimentsConcludeExperimentV2RequestDataType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
