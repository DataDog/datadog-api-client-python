# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class ObservabilityPipelineEnrichmentTableFileKeyItemField(ModelComposed):
    def __init__(self, **kwargs):
        """
        Specifies the source of the key value used for enrichment table lookups.
        Can be a plain field path string or an object specifying ``event`` , ``vrl`` , or ``secret``.

        :param event: The path to the field in the log event to use as the lookup key.
        :type event: str

        :param vrl: A VRL expression that returns the value to use as the lookup key.
        :type vrl: str

        :param secret: The name of the secret containing the lookup key value.
        :type secret: str
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
        from datadog_api_client.v2.model.observability_pipeline_enrichment_table_field_event_lookup import (
            ObservabilityPipelineEnrichmentTableFieldEventLookup,
        )
        from datadog_api_client.v2.model.observability_pipeline_enrichment_table_field_vrl_lookup import (
            ObservabilityPipelineEnrichmentTableFieldVrlLookup,
        )
        from datadog_api_client.v2.model.observability_pipeline_enrichment_table_field_secret_lookup import (
            ObservabilityPipelineEnrichmentTableFieldSecretLookup,
        )

        return {
            "oneOf": [
                str,
                ObservabilityPipelineEnrichmentTableFieldEventLookup,
                ObservabilityPipelineEnrichmentTableFieldVrlLookup,
                ObservabilityPipelineEnrichmentTableFieldSecretLookup,
            ],
        }
