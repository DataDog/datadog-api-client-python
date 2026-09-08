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
    from datadog_api_client.v2.model.custom_rule_revision_input import CustomRuleRevisionInput


class CustomRule(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_rule_revision_input import CustomRuleRevisionInput

        return {
            "created_at": (datetime,),
            "created_by": (str,),
            "id": (str,),
            "last_revision": (CustomRuleRevisionInput,),
            "name": (str,),
            "revisions": ([CustomRuleRevisionInput], none_type),
        }

    attribute_map = {
        "created_at": "created_at",
        "created_by": "created_by",
        "id": "id",
        "last_revision": "last_revision",
        "name": "name",
        "revisions": "revisions",
    }
    read_only_vars = {
        "created_at",
        "created_by",
    }

    def __init__(
        self_,
        id: str,
        name: str,
        created_at: Union[datetime, UnsetType] = unset,
        created_by: Union[str, UnsetType] = unset,
        last_revision: Union[CustomRuleRevisionInput, UnsetType] = unset,
        revisions: Union[List[CustomRuleRevisionInput], none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        A custom static analysis rule within a ruleset, as supplied in a create or update
        request. Nested rules are sent flat, without a ``data`` / ``type`` / ``attributes`` envelope.
        ``id`` and ``name`` are client-supplied and must match each other. The remaining members
        are server-assigned and read-only; they are declared so that a ruleset previously
        read back can be supplied unchanged.

        :param created_at: Creation timestamp
        :type created_at: datetime, optional

        :param created_by: Creator identifier
        :type created_by: str, optional

        :param id: Rule identifier, which is the same as the rule name.
        :type id: str

        :param last_revision: A revision of a custom static analysis rule as embedded in a rule supplied by a create
            or update request. Nested revisions are sent flat, without a ``data`` / ``type`` / ``attributes``
            envelope. ``id`` , ``version_id`` , ``checksum`` , ``created_at`` and ``created_by`` are server-assigned
            and read-only; they are declared so that a ruleset previously read back can be supplied
            unchanged.
        :type last_revision: CustomRuleRevisionInput, optional

        :param name: Rule name
        :type name: str

        :param revisions: Revision history of the rule.
        :type revisions: [CustomRuleRevisionInput], none_type, optional
        """
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if created_by is not unset:
            kwargs["created_by"] = created_by
        if last_revision is not unset:
            kwargs["last_revision"] = last_revision
        if revisions is not unset:
            kwargs["revisions"] = revisions
        super().__init__(kwargs)

        self_.id = id
        self_.name = name
