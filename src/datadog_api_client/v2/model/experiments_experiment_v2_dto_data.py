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
    from datadog_api_client.v2.model.experiments_patch_experiment_v2_response_data_attributes import (
        ExperimentsPatchExperimentV2ResponseDataAttributes,
    )
    from datadog_api_client.v2.model.experiments_patch_experiment_v2_response_data_type import (
        ExperimentsPatchExperimentV2ResponseDataType,
    )


class ExperimentsExperimentV2DTOData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_patch_experiment_v2_response_data_attributes import (
            ExperimentsPatchExperimentV2ResponseDataAttributes,
        )
        from datadog_api_client.v2.model.experiments_patch_experiment_v2_response_data_type import (
            ExperimentsPatchExperimentV2ResponseDataType,
        )

        return {
            "attributes": (ExperimentsPatchExperimentV2ResponseDataAttributes,),
            "id": (UUID,),
            "type": (ExperimentsPatchExperimentV2ResponseDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        id: UUID,
        type: ExperimentsPatchExperimentV2ResponseDataType,
        attributes: Union[ExperimentsPatchExperimentV2ResponseDataAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        Experiment resource with its identifier and configuration.

        :param attributes: Details of the experiment.
        :type attributes: ExperimentsPatchExperimentV2ResponseDataAttributes, optional

        :param id: Identifier of the experiment.
        :type id: UUID

        :param type: Experiments resource type.
        :type type: ExperimentsPatchExperimentV2ResponseDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
