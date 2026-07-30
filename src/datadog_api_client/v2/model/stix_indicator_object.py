# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.stix_metadata_object import STIXMetadataObject
    from datadog_api_client.v2.model.stix_pattern_type import STIXPatternType
    from datadog_api_client.v2.model.stix_spec_version import STIXSpecVersion
    from datadog_api_client.v2.model.stix_indicator_type import STIXIndicatorType


class STIXIndicatorObject(ModelNormal):
    validations = {
        "confidence": {
            "inclusive_maximum": 100,
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.stix_metadata_object import STIXMetadataObject
        from datadog_api_client.v2.model.stix_pattern_type import STIXPatternType
        from datadog_api_client.v2.model.stix_spec_version import STIXSpecVersion
        from datadog_api_client.v2.model.stix_indicator_type import STIXIndicatorType

        return {
            "confidence": (int,),
            "created": (datetime,),
            "external_references": ([STIXMetadataObject],),
            "id": (str,),
            "indicator_types": ([str],),
            "kill_chain_phases": ([STIXMetadataObject],),
            "labels": ([str],),
            "modified": (datetime,),
            "object_marking_refs": ([str],),
            "pattern": (str,),
            "pattern_type": (STIXPatternType,),
            "revoked": (bool,),
            "spec_version": (STIXSpecVersion,),
            "type": (STIXIndicatorType,),
            "valid_from": (datetime,),
            "valid_until": (datetime,),
        }

    attribute_map = {
        "confidence": "confidence",
        "created": "created",
        "external_references": "external_references",
        "id": "id",
        "indicator_types": "indicator_types",
        "kill_chain_phases": "kill_chain_phases",
        "labels": "labels",
        "modified": "modified",
        "object_marking_refs": "object_marking_refs",
        "pattern": "pattern",
        "pattern_type": "pattern_type",
        "revoked": "revoked",
        "spec_version": "spec_version",
        "type": "type",
        "valid_from": "valid_from",
        "valid_until": "valid_until",
    }

    def __init__(
        self_,
        created: datetime,
        id: str,
        modified: datetime,
        pattern: str,
        pattern_type: STIXPatternType,
        spec_version: STIXSpecVersion,
        type: STIXIndicatorType,
        valid_from: datetime,
        confidence: Union[int, UnsetType] = unset,
        external_references: Union[List[STIXMetadataObject], UnsetType] = unset,
        indicator_types: Union[List[str], UnsetType] = unset,
        kill_chain_phases: Union[List[STIXMetadataObject], UnsetType] = unset,
        labels: Union[List[str], UnsetType] = unset,
        object_marking_refs: Union[List[str], UnsetType] = unset,
        revoked: Union[bool, UnsetType] = unset,
        valid_until: Union[datetime, UnsetType] = unset,
        **kwargs,
    ):
        """
        A STIX 2.1 indicator object.

        :param confidence: The confidence in the correctness of the indicator, from 0 through 100.
        :type confidence: int, optional

        :param created: The time when the indicator was created.
        :type created: datetime

        :param external_references: Optional external reference metadata preserved with the indicator but not interpreted during ingestion.
        :type external_references: [STIXMetadataObject], optional

        :param id: The STIX indicator identifier.
        :type id: str

        :param indicator_types: The open vocabulary terms that categorize the indicator.
        :type indicator_types: [str], optional

        :param kill_chain_phases: Optional kill chain metadata preserved with the indicator but not interpreted during ingestion.
        :type kill_chain_phases: [STIXMetadataObject], optional

        :param labels: Labels associated with the indicator.
        :type labels: [str], optional

        :param modified: The time when the indicator was last modified.
        :type modified: datetime

        :param object_marking_refs: References to marking definition objects that apply to the indicator.
        :type object_marking_refs: [str], optional

        :param pattern: The STIX pattern that identifies the observable.
        :type pattern: str

        :param pattern_type: The supported STIX pattern language.
        :type pattern_type: STIXPatternType

        :param revoked: Whether the indicator has been revoked.
        :type revoked: bool, optional

        :param spec_version: The supported STIX specification version.
        :type spec_version: STIXSpecVersion

        :param type: The STIX object type for an indicator.
        :type type: STIXIndicatorType

        :param valid_from: The time from which the indicator is considered valid.
        :type valid_from: datetime

        :param valid_until: The time until which the indicator is considered valid.
        :type valid_until: datetime, optional
        """
        if confidence is not unset:
            kwargs["confidence"] = confidence
        if external_references is not unset:
            kwargs["external_references"] = external_references
        if indicator_types is not unset:
            kwargs["indicator_types"] = indicator_types
        if kill_chain_phases is not unset:
            kwargs["kill_chain_phases"] = kill_chain_phases
        if labels is not unset:
            kwargs["labels"] = labels
        if object_marking_refs is not unset:
            kwargs["object_marking_refs"] = object_marking_refs
        if revoked is not unset:
            kwargs["revoked"] = revoked
        if valid_until is not unset:
            kwargs["valid_until"] = valid_until
        super().__init__(kwargs)

        self_.created = created
        self_.id = id
        self_.modified = modified
        self_.pattern = pattern
        self_.pattern_type = pattern_type
        self_.spec_version = spec_version
        self_.type = type
        self_.valid_from = valid_from
