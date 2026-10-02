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
    from datadog_api_client.v2.model.experiments_patch_experiment_v2_request_data_attributes import (
        ExperimentsPatchExperimentV2RequestDataAttributes,
    )
    from datadog_api_client.v2.model.experiments_patch_experiment_v2_response_data_type import (
        ExperimentsPatchExperimentV2ResponseDataType,
    )


class ExperimentsPatchExperimentV2RequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_patch_experiment_v2_request_data_attributes import (
            ExperimentsPatchExperimentV2RequestDataAttributes,
        )
        from datadog_api_client.v2.model.experiments_patch_experiment_v2_response_data_type import (
            ExperimentsPatchExperimentV2ResponseDataType,
        )

        return {
            "attributes": (ExperimentsPatchExperimentV2RequestDataAttributes,),
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
        type: ExperimentsPatchExperimentV2ResponseDataType,
        attributes: Union[ExperimentsPatchExperimentV2RequestDataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        JSON:API resource containing the experiment identity and fields.

        :param attributes: Fields supplied to update the experiment.
        :type attributes: ExperimentsPatchExperimentV2RequestDataAttributes, optional

        :param id: ID of the experiment.
        :type id: str, optional

        :param type: Experiments resource type.
        :type type: ExperimentsPatchExperimentV2ResponseDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
