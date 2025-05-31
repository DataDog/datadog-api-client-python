# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class ObservabilityPipelineSensitiveDataScannerProcessorScope(ModelComposed):
    def __init__(self, **kwargs):
        """
        Determines which parts of the log the pattern-matching rule should be applied to.

        :param options: Fields to which the scope rule applies.
        :type options: ObservabilityPipelineSensitiveDataScannerProcessorScopeOptions

        :param target: Applies the rule only to included fields.
        :type target: ObservabilityPipelineSensitiveDataScannerProcessorScopeIncludeTarget
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
        from datadog_api_client.v2.model.observability_pipeline_sensitive_data_scanner_processor_scope_include import (
            ObservabilityPipelineSensitiveDataScannerProcessorScopeInclude,
        )
        from datadog_api_client.v2.model.observability_pipeline_sensitive_data_scanner_processor_scope_exclude import (
            ObservabilityPipelineSensitiveDataScannerProcessorScopeExclude,
        )
        from datadog_api_client.v2.model.observability_pipeline_sensitive_data_scanner_processor_scope_all import (
            ObservabilityPipelineSensitiveDataScannerProcessorScopeAll,
        )

        return {
            "oneOf": [
                ObservabilityPipelineSensitiveDataScannerProcessorScopeInclude,
                ObservabilityPipelineSensitiveDataScannerProcessorScopeExclude,
                ObservabilityPipelineSensitiveDataScannerProcessorScopeAll,
            ],
        }
