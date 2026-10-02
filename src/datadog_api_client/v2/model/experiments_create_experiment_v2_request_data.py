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
    from datadog_api_client.v2.model.experiments_create_experiment_v2_request_data_attributes import (
        ExperimentsCreateExperimentV2RequestDataAttributes,
    )
    from datadog_api_client.v2.model.experiments_patch_experiment_v2_response_data_type import (
        ExperimentsPatchExperimentV2ResponseDataType,
    )


class ExperimentsCreateExperimentV2RequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_create_experiment_v2_request_data_attributes import (
            ExperimentsCreateExperimentV2RequestDataAttributes,
        )
        from datadog_api_client.v2.model.experiments_patch_experiment_v2_response_data_type import (
            ExperimentsPatchExperimentV2ResponseDataType,
        )

        return {
            "attributes": (ExperimentsCreateExperimentV2RequestDataAttributes,),
            "id": (str,),
            "type": (ExperimentsPatchExperimentV2ResponseDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: ExperimentsCreateExperimentV2RequestDataAttributes,
        type: ExperimentsPatchExperimentV2ResponseDataType,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Experiment resource to create.

        :param attributes: Configuration and descriptive fields for the new experiment draft.
        :type attributes: ExperimentsCreateExperimentV2RequestDataAttributes

        :param id: Optional JSON:API resource identifier field.
        :type id: str, optional

        :param type: Experiments resource type.
        :type type: ExperimentsPatchExperimentV2ResponseDataType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
