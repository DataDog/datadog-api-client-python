# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.notebook_template_variable_available_values_query_group_by import (
        NotebookTemplateVariableAvailableValuesQueryGroupBy,
    )
    from datadog_api_client.v1.model.notebook_template_variable_available_values_query_search import (
        NotebookTemplateVariableAvailableValuesQuerySearch,
    )


class NotebookTemplateVariableAvailableValuesQueryLogRumSpans(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.notebook_template_variable_available_values_query_group_by import (
            NotebookTemplateVariableAvailableValuesQueryGroupBy,
        )
        from datadog_api_client.v1.model.notebook_template_variable_available_values_query_search import (
            NotebookTemplateVariableAvailableValuesQuerySearch,
        )

        return {
            "data_source": (str,),
            "group_by": ([NotebookTemplateVariableAvailableValuesQueryGroupBy],),
            "search": (NotebookTemplateVariableAvailableValuesQuerySearch,),
        }

    attribute_map = {
        "data_source": "data_source",
        "group_by": "group_by",
        "search": "search",
    }

    def __init__(
        self_,
        data_source: str,
        group_by: List[NotebookTemplateVariableAvailableValuesQueryGroupBy],
        search: NotebookTemplateVariableAvailableValuesQuerySearch,
        **kwargs,
    ):
        """
        Available values query for logs, RUM, or spans data sources.

        :param data_source: The data source for the query. Must be one of ``logs`` , ``rum`` , or ``spans``.
        :type data_source: str

        :param group_by: Group-by fields for the query.
        :type group_by: [NotebookTemplateVariableAvailableValuesQueryGroupBy]

        :param search: Search parameters for an available values query.
        :type search: NotebookTemplateVariableAvailableValuesQuerySearch
        """
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.group_by = group_by
        self_.search = search
