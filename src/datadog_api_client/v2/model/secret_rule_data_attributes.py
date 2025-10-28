# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.secret_rule_data_attributes_match_validation import (
        SecretRuleDataAttributesMatchValidation,
    )


class SecretRuleDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.secret_rule_data_attributes_match_validation import (
            SecretRuleDataAttributesMatchValidation,
        )

        return {
            "default_included_keywords": ([str],),
            "description": (str,),
            "license": (str,),
            "match_validation": (SecretRuleDataAttributesMatchValidation,),
            "name": (str,),
            "pattern": (str,),
            "priority": (str,),
            "sds_id": (str,),
            "validators": ([str],),
        }

    attribute_map = {
        "default_included_keywords": "default_included_keywords",
        "description": "description",
        "license": "license",
        "match_validation": "match_validation",
        "name": "name",
        "pattern": "pattern",
        "priority": "priority",
        "sds_id": "sds_id",
        "validators": "validators",
    }

    def __init__(
        self_,
        default_included_keywords: Union[List[str], UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        license: Union[str, UnsetType] = unset,
        match_validation: Union[SecretRuleDataAttributesMatchValidation, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        pattern: Union[str, UnsetType] = unset,
        priority: Union[str, UnsetType] = unset,
        sds_id: Union[str, UnsetType] = unset,
        validators: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """


        :param default_included_keywords:
        :type default_included_keywords: [str], optional

        :param description:
        :type description: str, optional

        :param license:
        :type license: str, optional

        :param match_validation:
        :type match_validation: SecretRuleDataAttributesMatchValidation, optional

        :param name:
        :type name: str, optional

        :param pattern:
        :type pattern: str, optional

        :param priority:
        :type priority: str, optional

        :param sds_id:
        :type sds_id: str, optional

        :param validators:
        :type validators: [str], optional
        """
        if default_included_keywords is not unset:
            kwargs["default_included_keywords"] = default_included_keywords
        if description is not unset:
            kwargs["description"] = description
        if license is not unset:
            kwargs["license"] = license
        if match_validation is not unset:
            kwargs["match_validation"] = match_validation
        if name is not unset:
            kwargs["name"] = name
        if pattern is not unset:
            kwargs["pattern"] = pattern
        if priority is not unset:
            kwargs["priority"] = priority
        if sds_id is not unset:
            kwargs["sds_id"] = sds_id
        if validators is not unset:
            kwargs["validators"] = validators
        super().__init__(kwargs)
