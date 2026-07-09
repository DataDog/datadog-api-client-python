# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class NotebookTemplateVariableAvailableValuesQuery(ModelComposed):
    def __init__(self, **kwargs):
        """
        Query used to dynamically populate the list of available values for the template variable.

        :param data_source: The data source for the query. Must be one of `logs`, `rum`, or `spans`.
        :type data_source: str

        :param group_by: Group-by fields for the query.
        :type group_by: [NotebookTemplateVariableAvailableValuesQueryGroupBy]

        :param search: Search parameters for an available values query.
        :type search: NotebookTemplateVariableAvailableValuesQuerySearch

        :param query: The metrics query string.
        :type query: str
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v1.model.notebook_template_variable_available_values_query_log_rum_spans import (
            NotebookTemplateVariableAvailableValuesQueryLogRumSpans,
        )
        from datadog_api_client.v1.model.notebook_template_variable_available_values_query_metrics import (
            NotebookTemplateVariableAvailableValuesQueryMetrics,
        )

        return {
            "oneOf": [
                NotebookTemplateVariableAvailableValuesQueryLogRumSpans,
                NotebookTemplateVariableAvailableValuesQueryMetrics,
            ],
        }
