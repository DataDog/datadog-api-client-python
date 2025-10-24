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
    from datadog_api_client.v1.model.logs_schema_category_mapper_category import LogsSchemaCategoryMapperCategory
    from datadog_api_client.v1.model.logs_schema_category_mapper_fallback import LogsSchemaCategoryMapperFallback
    from datadog_api_client.v1.model.logs_schema_category_mapper_targets import LogsSchemaCategoryMapperTargets
    from datadog_api_client.v1.model.logs_schema_category_mapper_type import LogsSchemaCategoryMapperType


class LogsSchemaCategoryMapper(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.logs_schema_category_mapper_category import LogsSchemaCategoryMapperCategory
        from datadog_api_client.v1.model.logs_schema_category_mapper_fallback import LogsSchemaCategoryMapperFallback
        from datadog_api_client.v1.model.logs_schema_category_mapper_targets import LogsSchemaCategoryMapperTargets
        from datadog_api_client.v1.model.logs_schema_category_mapper_type import LogsSchemaCategoryMapperType

        return {
            "categories": ([LogsSchemaCategoryMapperCategory],),
            "fallback": (LogsSchemaCategoryMapperFallback,),
            "name": (str,),
            "targets": (LogsSchemaCategoryMapperTargets,),
            "type": (LogsSchemaCategoryMapperType,),
        }

    attribute_map = {
        "categories": "categories",
        "fallback": "fallback",
        "name": "name",
        "targets": "targets",
        "type": "type",
    }

    def __init__(
        self_,
        categories: List[LogsSchemaCategoryMapperCategory],
        name: str,
        targets: LogsSchemaCategoryMapperTargets,
        type: LogsSchemaCategoryMapperType,
        fallback: Union[LogsSchemaCategoryMapperFallback, UnsetType] = unset,
        **kwargs,
    ):
        """
        Use the Schema Category Mapper to categorize log event into enum fields.
        In the case of OCSF, they can be used to map sibling fields which are composed of an ID and a name.

        **Notes** :

        * The syntax of the query is the one of Logs Explorer search bar.
          The query can be done on any log attribute or tag, whether it is a facet or not.
          Wildcards can also be used inside your query.
        * Categories are executed in order and processing stops at the first match.
          Make sure categories are properly ordered in case a log could match multiple queries.
        * Sibling fields always have a numerical ID field and a human-readable string name.
        * A fallback section handles cases where the name or ID value matches a specific value.
          If the name matches "Other" or the ID matches 99, the value of the sibling name field will be pulled from a source field from the original log.

        :param categories: Array of filters to match or not a log and their
            corresponding ``name`` to assign a custom value to the log.
        :type categories: [LogsSchemaCategoryMapperCategory]

        :param fallback: Used to override hardcoded category values with a value pulled from a source attribute on the log.
        :type fallback: LogsSchemaCategoryMapperFallback, optional

        :param name: Name of the logs schema category mapper.
        :type name: str

        :param targets: Name of the target attributes which value is defined by the matching category.
        :type targets: LogsSchemaCategoryMapperTargets

        :param type: Type of logs schema category mapper.
        :type type: LogsSchemaCategoryMapperType
        """
        if fallback is not unset:
            kwargs["fallback"] = fallback
        super().__init__(kwargs)

        self_.categories = categories
        self_.name = name
        self_.targets = targets
        self_.type = type
