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
    from datadog_api_client.v2.model.experiments_cancel_experiment_v2_request_data_attributes import (
        ExperimentsCancelExperimentV2RequestDataAttributes,
    )
    from datadog_api_client.v2.model.experiments_cancel_experiment_v2_request_data_type import (
        ExperimentsCancelExperimentV2RequestDataType,
    )


class ExperimentsCancelExperimentV2RequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_cancel_experiment_v2_request_data_attributes import (
            ExperimentsCancelExperimentV2RequestDataAttributes,
        )
        from datadog_api_client.v2.model.experiments_cancel_experiment_v2_request_data_type import (
            ExperimentsCancelExperimentV2RequestDataType,
        )

        return {
            "attributes": (ExperimentsCancelExperimentV2RequestDataAttributes,),
            "id": (str,),
            "type": (ExperimentsCancelExperimentV2RequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: ExperimentsCancelExperimentV2RequestDataAttributes,
        type: ExperimentsCancelExperimentV2RequestDataType,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Experiment cancellation resource with the experiment identifier and reason.

        :param attributes: Reason to record when canceling the experiment.
        :type attributes: ExperimentsCancelExperimentV2RequestDataAttributes

        :param id: Identifier of the experiment to cancel.
        :type id: str, optional

        :param type: Cancel experiment request resource type.
        :type type: ExperimentsCancelExperimentV2RequestDataType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
