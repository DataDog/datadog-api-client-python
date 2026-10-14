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
    from datadog_api_client.v2.model.experiments_patch_experiment_protocol_request_data_attributes import (
        ExperimentsPatchExperimentProtocolRequestDataAttributes,
    )
    from datadog_api_client.v2.model.experiments_public_protocol_response_data_type import (
        ExperimentsPublicProtocolResponseDataType,
    )


class ExperimentsPatchExperimentProtocolRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_patch_experiment_protocol_request_data_attributes import (
            ExperimentsPatchExperimentProtocolRequestDataAttributes,
        )
        from datadog_api_client.v2.model.experiments_public_protocol_response_data_type import (
            ExperimentsPublicProtocolResponseDataType,
        )

        return {
            "attributes": (ExperimentsPatchExperimentProtocolRequestDataAttributes,),
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
        type: ExperimentsPublicProtocolResponseDataType,
        attributes: Union[ExperimentsPatchExperimentProtocolRequestDataAttributes, UnsetType] = unset,
        id: Union[UUID, UnsetType] = unset,
        **kwargs,
    ):
        """
        JSON:API protocol request resource.

        :param attributes: Partial protocol update. Omitted attributes remain unchanged. Published protocols accept only name, description, and migration_metadata; archived protocols reject updates.
        :type attributes: ExperimentsPatchExperimentProtocolRequestDataAttributes, optional

        :param id: Protocol ID. If supplied, must match the path protocol_id.
        :type id: UUID, optional

        :param type: Protocols resource type.
        :type type: ExperimentsPublicProtocolResponseDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
