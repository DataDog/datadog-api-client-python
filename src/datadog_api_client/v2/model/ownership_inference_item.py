# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ownership_evidence_version import OwnershipEvidenceVersion
    from datadog_api_client.v2.model.ownership_owner_type import OwnershipOwnerType
    from datadog_api_client.v2.model.ownership_inference_source import OwnershipInferenceSource
    from datadog_api_client.v2.model.ownership_inference_status import OwnershipInferenceStatus


class OwnershipInferenceItem(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ownership_evidence_version import OwnershipEvidenceVersion
        from datadog_api_client.v2.model.ownership_owner_type import OwnershipOwnerType
        from datadog_api_client.v2.model.ownership_inference_source import OwnershipInferenceSource
        from datadog_api_client.v2.model.ownership_inference_status import OwnershipInferenceStatus

        return {
            "checksum": (str,),
            "confidence": (str,),
            "created_at": (datetime,),
            "evidence_versions": ([OwnershipEvidenceVersion],),
            "explanation": (str,),
            "id": (str,),
            "owner_type": (OwnershipOwnerType,),
            "primary_contact_ref": (str, none_type),
            "sources": ([OwnershipInferenceSource],),
            "status": (OwnershipInferenceStatus,),
            "updated_at": (datetime,),
        }

    attribute_map = {
        "checksum": "checksum",
        "confidence": "confidence",
        "created_at": "created_at",
        "evidence_versions": "evidence_versions",
        "explanation": "explanation",
        "id": "id",
        "owner_type": "owner_type",
        "primary_contact_ref": "primary_contact_ref",
        "sources": "sources",
        "status": "status",
        "updated_at": "updated_at",
    }

    def __init__(
        self_,
        checksum: str,
        confidence: str,
        created_at: datetime,
        evidence_versions: Union[List[OwnershipEvidenceVersion], none_type],
        explanation: str,
        id: str,
        owner_type: OwnershipOwnerType,
        sources: List[OwnershipInferenceSource],
        status: OwnershipInferenceStatus,
        updated_at: datetime,
        primary_contact_ref: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        A single ownership inference, scoped to a specific owner type.

        :param checksum: A checksum that uniquely identifies the current state of the inference. Required when submitting feedback.
        :type checksum: str

        :param confidence: The confidence score of the inference, expressed as a numeric string with up to four decimal places.
        :type confidence: str

        :param created_at: The time when the inference was created.
        :type created_at: datetime

        :param evidence_versions: The list of evidence versions associated with an inference.
        :type evidence_versions: [OwnershipEvidenceVersion], none_type

        :param explanation: A human-readable explanation of how the inference was produced.
        :type explanation: str

        :param id: The identifier of the inference, formatted as ``resource_id:owner_type``.
        :type id: str

        :param owner_type: The owner type for an ownership inference.
        :type owner_type: OwnershipOwnerType

        :param primary_contact_ref: The primary contact reference for the inferred owner, formatted as ``ref:handle/<owner_handle>``.
        :type primary_contact_ref: str, none_type, optional

        :param sources: The list of sources backing an ownership inference. Empty when the inference status is not whitelisted to expose sources.
        :type sources: [OwnershipInferenceSource]

        :param status: The lifecycle status of an ownership inference.
        :type status: OwnershipInferenceStatus

        :param updated_at: The time when the inference was last updated.
        :type updated_at: datetime
        """
        if primary_contact_ref is not unset:
            kwargs["primary_contact_ref"] = primary_contact_ref
        super().__init__(kwargs)

        self_.checksum = checksum
        self_.confidence = confidence
        self_.created_at = created_at
        self_.evidence_versions = evidence_versions
        self_.explanation = explanation
        self_.id = id
        self_.owner_type = owner_type
        self_.sources = sources
        self_.status = status
        self_.updated_at = updated_at
