from gorapass.models import Hikes

class ModelFilter:
    ATTRIBUTE_NAME = 'attribute_name'
    ATTRIBUTE_VALUE = 'attribute_value'
    FILTER_TYPE = 'filter_type'

    FILTER_KEYS = {
        ATTRIBUTE_NAME,
        ATTRIBUTE_VALUE,
        FILTER_TYPE,
    }

    @classmethod
    def filter_hikes(cls, hike_models, filters):
        for model_filter in filters:
            attribute = model_filter[ModelFilter.ATTRIBUTE_NAME]
            value = model_filter[ModelFilter.ATTRIBUTE_VALUE]
            match model_filter[ModelFilter.FILTER_TYPE]:
                case 'exact':
                    hike_models = [ hike
                                    for hike in hike_models
                                    if getattr(hike, attribute) == value ]
                case 'partial':
                    hike_models = [ hike
                                    for hike in hike_models
                                    if value.lower() in str(getattr(hike, attribute)).lower() ]
                case 'less_than':
                    hike_models = [ hike
                                    for hike in hike_models
                                    if getattr(hike, attribute) < value ]
                case 'greater_than':
                    hike_models = [ hike
                                    for hike in hike_models
                                    if getattr(hike, attribute) > value ]
                case _:
                    pass
            # Return early if we run out of matching hikes
            if len(hike_models) == 0:
                return hike_models

        return hike_models

    @classmethod
    def valid_hike_filters(cls, filters):
        for model_filter in filters:
            if set(model_filter.keys()) != ModelFilter.FILTER_KEYS:
                return False
            if not hasattr(Hikes, model_filter[ModelFilter.ATTRIBUTE_NAME]):
                return False

        return True
