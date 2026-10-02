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
    from datadog_api_client.v2.model.experiments_start_experiment_v2_request_data_type import (
        ExperimentsStartExperimentV2RequestDataType,
    )


class ExperimentsStartExperimentV2RequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_start_experiment_v2_request_data_type import (
            ExperimentsStartExperimentV2RequestDataType,
        )

        return {
            "id": (str,),
            "type": (ExperimentsStartExperimentV2RequestDataType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, type: ExperimentsStartExperimentV2RequestDataType, id: Union[str, UnsetType] = unset, **kwargs):
        """
        JSON:API resource containing the experiment identity.

        :param id: ID of the experiment.
        :type id: str, optional

        :param type: Start experiment request resource type.
        :type type: ExperimentsStartExperimentV2RequestDataType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
