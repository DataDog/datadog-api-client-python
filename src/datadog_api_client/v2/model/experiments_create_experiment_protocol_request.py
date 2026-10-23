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
    from datadog_api_client.v2.model.experiments_create_experiment_protocol_request_data import (
        ExperimentsCreateExperimentProtocolRequestData,
    )


class ExperimentsCreateExperimentProtocolRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_create_experiment_protocol_request_data import (
            ExperimentsCreateExperimentProtocolRequestData,
        )

        return {
            "data": (ExperimentsCreateExperimentProtocolRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ExperimentsCreateExperimentProtocolRequestData, **kwargs):
        """
        Create a draft protocol with the organization default subject type.

        :param data: JSON:API protocol request resource.
        :type data: ExperimentsCreateExperimentProtocolRequestData
        """
        super().__init__(kwargs)

        self_.data = data
