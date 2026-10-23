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
    from datadog_api_client.v2.model.experiments_create_experiment_protocol_request_data_attributes import (
        ExperimentsCreateExperimentProtocolRequestDataAttributes,
    )
    from datadog_api_client.v2.model.experiments_public_protocol_response_data_type import (
        ExperimentsPublicProtocolResponseDataType,
    )


class ExperimentsCreateExperimentProtocolRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_create_experiment_protocol_request_data_attributes import (
            ExperimentsCreateExperimentProtocolRequestDataAttributes,
        )
        from datadog_api_client.v2.model.experiments_public_protocol_response_data_type import (
            ExperimentsPublicProtocolResponseDataType,
        )

        return {
            "attributes": (ExperimentsCreateExperimentProtocolRequestDataAttributes,),
            "type": (ExperimentsPublicProtocolResponseDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: ExperimentsCreateExperimentProtocolRequestDataAttributes,
        type: ExperimentsPublicProtocolResponseDataType,
        **kwargs,
    ):
        """
        JSON:API protocol request resource.

        :param attributes: Create a draft protocol with the organization default subject type.
        :type attributes: ExperimentsCreateExperimentProtocolRequestDataAttributes

        :param type: Protocols resource type.
        :type type: ExperimentsPublicProtocolResponseDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
