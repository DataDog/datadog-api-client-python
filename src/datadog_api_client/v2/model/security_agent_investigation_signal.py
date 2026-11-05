# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class SecurityAgentInvestigationSignal(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "severity": (str,),
            "sources": ([str],),
            "tactic": (str,),
            "tags": ([str],),
            "technique": (str,),
            "timestamp": (str,),
            "title": (str,),
        }

    attribute_map = {
        "severity": "severity",
        "sources": "sources",
        "tactic": "tactic",
        "tags": "tags",
        "technique": "technique",
        "timestamp": "timestamp",
        "title": "title",
    }

    def __init__(
        self_,
        severity: Union[str, UnsetType] = unset,
        sources: Union[List[str], UnsetType] = unset,
        tactic: Union[str, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        technique: Union[str, UnsetType] = unset,
        timestamp: Union[str, UnsetType] = unset,
        title: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Summary of the signal the investigation is about.

        :param severity: Severity of the signal: ``info`` , ``low`` , ``medium`` , ``high`` , or ``critical``.
        :type severity: str, optional

        :param sources: Sources of the signal.
        :type sources: [str], optional

        :param tactic: MITRE ATT&CK tactic, from the signal's ``tactic`` tag.
        :type tactic: str, optional

        :param tags: Tags of the signal, written ``key:value``.
        :type tags: [str], optional

        :param technique: MITRE ATT&CK technique, from the signal's ``technique`` tag.
        :type technique: str, optional

        :param timestamp: Time the signal was generated.
        :type timestamp: str, optional

        :param title: Title of the signal.
        :type title: str, optional
        """
        if severity is not unset:
            kwargs["severity"] = severity
        if sources is not unset:
            kwargs["sources"] = sources
        if tactic is not unset:
            kwargs["tactic"] = tactic
        if tags is not unset:
            kwargs["tags"] = tags
        if technique is not unset:
            kwargs["technique"] = technique
        if timestamp is not unset:
            kwargs["timestamp"] = timestamp
        if title is not unset:
            kwargs["title"] = title
        super().__init__(kwargs)
