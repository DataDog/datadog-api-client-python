# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.experiments_patch_experiment_protocol_request_data import (
        ExperimentsPatchExperimentProtocolRequestData,
    )


class ExperimentsPatchExperimentProtocolRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_patch_experiment_protocol_request_data import (
            ExperimentsPatchExperimentProtocolRequestData,
        )

        return {
            "data": (ExperimentsPatchExperimentProtocolRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ExperimentsPatchExperimentProtocolRequestData, **kwargs):
        """
        Partial protocol update. Omitted attributes remain unchanged. Published protocols accept only name, description, and migration_metadata; archived protocols reject updates.

        :param data: JSON:API protocol request resource.
        :type data: ExperimentsPatchExperimentProtocolRequestData
        """
        super().__init__(kwargs)

        self_.data = data
