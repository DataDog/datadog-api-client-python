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
    from datadog_api_client.v2.model.experiments_public_protocol_response_data_attributes_subject_type import (
        ExperimentsPublicProtocolResponseDataAttributesSubjectType,
    )
    from datadog_api_client.v2.model.experiments_public_protocol_response_data_attributes_status import (
        ExperimentsPublicProtocolResponseDataAttributesStatus,
    )


class ExperimentsPublicProtocolListResponseDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_public_protocol_response_data_attributes_subject_type import (
            ExperimentsPublicProtocolResponseDataAttributesSubjectType,
        )
        from datadog_api_client.v2.model.experiments_public_protocol_response_data_attributes_status import (
            ExperimentsPublicProtocolResponseDataAttributesStatus,
        )

        return {
            "description": (str,),
            "name": (str,),
            "primary_metric": (ExperimentsPublicProtocolResponseDataAttributesSubjectType,),
            "primary_metric_id": (str,),
            "status": (ExperimentsPublicProtocolResponseDataAttributesStatus,),
            "subject_type": (ExperimentsPublicProtocolResponseDataAttributesSubjectType,),
            "subject_type_id": (str,),
            "updated_at": (str,),
        }

    attribute_map = {
        "description": "description",
        "name": "name",
        "primary_metric": "primary_metric",
        "primary_metric_id": "primary_metric_id",
        "status": "status",
        "subject_type": "subject_type",
        "subject_type_id": "subject_type_id",
        "updated_at": "updated_at",
    }

    def __init__(
        self_,
        name: str,
        status: ExperimentsPublicProtocolResponseDataAttributesStatus,
        updated_at: str,
        description: Union[str, UnsetType] = unset,
        primary_metric: Union[ExperimentsPublicProtocolResponseDataAttributesSubjectType, UnsetType] = unset,
        primary_metric_id: Union[str, UnsetType] = unset,
        subject_type: Union[ExperimentsPublicProtocolResponseDataAttributesSubjectType, UnsetType] = unset,
        subject_type_id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Summary of the protocol and its selected subject type and primary metric.

        :param description: Text that explains the protocol.
        :type description: str, optional

        :param name: Display name of the protocol.
        :type name: str

        :param primary_metric: Subject type selected by the protocol.
        :type primary_metric: ExperimentsPublicProtocolResponseDataAttributesSubjectType, optional

        :param primary_metric_id: ID of the primary metric supplied by the protocol.
        :type primary_metric_id: str, optional

        :param status: Publication status of the protocol.
        :type status: ExperimentsPublicProtocolResponseDataAttributesStatus

        :param subject_type: Subject type selected by the protocol.
        :type subject_type: ExperimentsPublicProtocolResponseDataAttributesSubjectType, optional

        :param subject_type_id: ID of the subject type used by this configuration.
        :type subject_type_id: str, optional

        :param updated_at: RFC3339 update time. Preserve all fractional seconds when passing this value as expected_updated_at.
        :type updated_at: str
        """
        if description is not unset:
            kwargs["description"] = description
        if primary_metric is not unset:
            kwargs["primary_metric"] = primary_metric
        if primary_metric_id is not unset:
            kwargs["primary_metric_id"] = primary_metric_id
        if subject_type is not unset:
            kwargs["subject_type"] = subject_type
        if subject_type_id is not unset:
            kwargs["subject_type_id"] = subject_type_id
        super().__init__(kwargs)

        self_.name = name
        self_.status = status
        self_.updated_at = updated_at
