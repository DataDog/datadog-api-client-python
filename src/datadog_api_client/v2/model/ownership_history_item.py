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


class OwnershipHistoryItem(ModelNormal):
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
            "failed_at": (datetime, none_type),
            "failure_reason": (str, none_type),
            "id": (int,),
            "owner_type": (OwnershipOwnerType,),
            "primary_contact_ref": (str, none_type),
            "resource_id": (str,),
            "retry_schedule": (datetime, none_type),
            "sources": ([OwnershipInferenceSource],),
            "status": (OwnershipInferenceStatus,),
        }

    attribute_map = {
        "checksum": "checksum",
        "confidence": "confidence",
        "created_at": "created_at",
        "evidence_versions": "evidence_versions",
        "explanation": "explanation",
        "failed_at": "failed_at",
        "failure_reason": "failure_reason",
        "id": "id",
        "owner_type": "owner_type",
        "primary_contact_ref": "primary_contact_ref",
        "resource_id": "resource_id",
        "retry_schedule": "retry_schedule",
        "sources": "sources",
        "status": "status",
    }

    def __init__(
        self_,
        checksum: str,
        confidence: str,
        created_at: datetime,
        evidence_versions: Union[List[OwnershipEvidenceVersion], none_type],
        explanation: str,
        id: int,
        owner_type: OwnershipOwnerType,
        resource_id: str,
        sources: List[OwnershipInferenceSource],
        status: OwnershipInferenceStatus,
        failed_at: Union[datetime, none_type, UnsetType] = unset,
        failure_reason: Union[str, none_type, UnsetType] = unset,
        primary_contact_ref: Union[str, none_type, UnsetType] = unset,
        retry_schedule: Union[datetime, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        A single ownership inference history entry.

        :param checksum: A checksum identifying the state of the inference at this point in time.
        :type checksum: str

        :param confidence: The confidence score of the inference, expressed as a numeric string with up to four decimal places.
        :type confidence: str

        :param created_at: The time this history entry was created.
        :type created_at: datetime

        :param evidence_versions: The list of evidence versions associated with an inference.
        :type evidence_versions: [OwnershipEvidenceVersion], none_type

        :param explanation: A human-readable explanation of how the inference was produced.
        :type explanation: str

        :param failed_at: The time when this inference failed, if applicable.
        :type failed_at: datetime, none_type, optional

        :param failure_reason: The reason why this inference failed, if applicable.
        :type failure_reason: str, none_type, optional

        :param id: The unique identifier of the history entry.
        :type id: int

        :param owner_type: The owner type for an ownership inference.
        :type owner_type: OwnershipOwnerType

        :param primary_contact_ref: The primary contact reference for the inferred owner, formatted as ``ref:handle/<owner_handle>``.
        :type primary_contact_ref: str, none_type, optional

        :param resource_id: The identifier of the resource that the inference applies to.
        :type resource_id: str

        :param retry_schedule: The scheduled retry time for a failed inference, if applicable.
        :type retry_schedule: datetime, none_type, optional

        :param sources: The list of sources backing an ownership inference. Empty when the inference status is not whitelisted to expose sources.
        :type sources: [OwnershipInferenceSource]

        :param status: The lifecycle status of an ownership inference.
        :type status: OwnershipInferenceStatus
        """
        if failed_at is not unset:
            kwargs["failed_at"] = failed_at
        if failure_reason is not unset:
            kwargs["failure_reason"] = failure_reason
        if primary_contact_ref is not unset:
            kwargs["primary_contact_ref"] = primary_contact_ref
        if retry_schedule is not unset:
            kwargs["retry_schedule"] = retry_schedule
        super().__init__(kwargs)

        self_.checksum = checksum
        self_.confidence = confidence
        self_.created_at = created_at
        self_.evidence_versions = evidence_versions
        self_.explanation = explanation
        self_.id = id
        self_.owner_type = owner_type
        self_.resource_id = resource_id
        self_.sources = sources
        self_.status = status
