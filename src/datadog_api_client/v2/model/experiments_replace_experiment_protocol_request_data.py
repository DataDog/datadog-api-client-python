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
    from datadog_api_client.v2.model.experiments_replace_experiment_protocol_request_data_attributes import (
        ExperimentsReplaceExperimentProtocolRequestDataAttributes,
    )
    from datadog_api_client.v2.model.experiments_public_protocol_response_data_type import (
        ExperimentsPublicProtocolResponseDataType,
    )


class ExperimentsReplaceExperimentProtocolRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_replace_experiment_protocol_request_data_attributes import (
            ExperimentsReplaceExperimentProtocolRequestDataAttributes,
        )
        from datadog_api_client.v2.model.experiments_public_protocol_response_data_type import (
            ExperimentsPublicProtocolResponseDataType,
        )

        return {
            "attributes": (ExperimentsReplaceExperimentProtocolRequestDataAttributes,),
            "id": (UUID,),
            "type": (ExperimentsPublicProtocolResponseDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: ExperimentsReplaceExperimentProtocolRequestDataAttributes,
        type: ExperimentsPublicProtocolResponseDataType,
        id: Union[UUID, UnsetType] = unset,
        **kwargs,
    ):
        """
        JSON:API protocol request resource.

        :param attributes: Replace a published protocol template. Omitted optional template fields are cleared. Omitted enforcement and migration_metadata are preserved. Enabled limits require their values; allocation settings require environment_id.
        :type attributes: ExperimentsReplaceExperimentProtocolRequestDataAttributes

        :param id: Protocol ID. If supplied, must match the path protocol_id.
        :type id: UUID, optional

        :param type: Protocols resource type.
        :type type: ExperimentsPublicProtocolResponseDataType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
